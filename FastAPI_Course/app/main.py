import zoneinfo
from fastapi import FastAPI, Request
from datetime import datetime
import time
from db import create_db_and_tables
from .routers import customers, transactions, invoices, plans

app = FastAPI(lifespan=create_db_and_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)


@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in {process_time:.4f} seconds")
    return response


@app.middleware("http")
async def log_request_headers(request: Request, call_next) -> Request:
    """
    Middleware to list the headers of any request.
    Parameters:
    - request: incoming request.
    """
    print(f"Request headers: {request.headers}")
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


country_timezones = {
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def get_time_by_iso_code(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return {"error": "Country code not found"}
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"timestamp": datetime.now(tz)}


@app.get("/time/{iso_code}/{format}")
async def time_format(iso_code: str, format: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return {"error": "Country code not found"}
    tz = zoneinfo.ZoneInfo(timezone_str)

    if format == "12":
        return {"timestamp": datetime.now(tz).strftime("%I:%M:%S %p")}
    elif format == "24":
        return {"timestamp": datetime.now(tz).strftime("%H:%M:%S")}
    else:
        return {"timestamp": datetime.now(tz)}
