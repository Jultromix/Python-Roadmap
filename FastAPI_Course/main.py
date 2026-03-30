import zoneinfo
from fastapi import FastAPI
from datetime import datetime
from models import Customer, Transaction, Invoice, CustomerCreate


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


customer_list: list[Customer] = []


@app.post("/customer", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):

    customer = Customer.model_validate(customer_data.model_dump())
    # This is an async function for ubpdating the id (simulating what happens with a DB)
    customer_list.append(customer)
    customer.id = len(customer_list)
    return customer


@app.get("/customer", response_model=list[Customer])
async def list_customers():
    return customer_list


@app.get("/customer/{customer_id}", response_model=Customer | None)
async def list_customers_by_id(customer_id: int):

    customers = [customer for customer in customer_list if customer.id == customer_id]
    return customers[0] if customers else None


@app.post("/transaction")
async def create_transaction(transaction_data: Transaction):
    return transaction_data


@app.post("/invoice")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
