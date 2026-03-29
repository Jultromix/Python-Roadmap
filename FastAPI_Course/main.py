import zoneinfo
from fastapi import FastAPI
from datetime import datetime
from models import Customer, Transaction, Invoice


app = FastAPI()


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
async def time(iso_code: str):
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


@app.post("/customer")
async def create_customer(customer_data: Customer):
    return {"customer": customer_data}


@app.post("/transaction")
async def create_transaction(transaction_data: Transaction):
    return {"transaction": transaction_data}


@app.post("/invoice")
async def create_invoice(invoice_data: Invoice):
    return {"invoice": invoice_data}
