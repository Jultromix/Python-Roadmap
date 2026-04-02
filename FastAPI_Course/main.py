import zoneinfo
from fastapi import FastAPI, HTTPException, status
from datetime import datetime

from models import Customer, Transaction, Invoice, CustomerCreate, CustomerUpdate
from db import SessionDep, create_db_and_tables
from sqlmodel import select

app = FastAPI(lifespan=create_db_and_tables)


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
async def create_customer(customer_data: CustomerCreate, session: SessionDep):

    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)

    # This is an async function for ubpdating the id (simulating what happens with a DB)
    # customer_list.append(customer)
    # customer.id = len(customer_list)
    return customer


@app.get("/customer", response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()


@app.get("/customer/{customer_id}", response_model=Customer | None)
async def read_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    return customer


@app.delete("/customer/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    session.delete(customer)
    session.commit()
    return {"detail": "ok"}


@app.patch("/customer/{customer_id}", response_model=Customer)
async def update_customer(
    customer_id: int,
    session: SessionDep,
    customer_data: CustomerUpdate,
):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    customer_db.name = customer_data.name
    customer_db.age = customer_data.age
    customer_db.email = customer_data.email
    customer_db.description = customer_data.description
    session.commit()
    return {"detail": "ok"}


@app.post("/transaction")
async def create_transaction(transaction_data: Transaction):
    return transaction_data


@app.post("/invoice")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
