from sqlmodel import Session
from models import Customer, Transaction
from db import engine

session = Session(engine)
customer = Customer(
    name="John Doe",
    email="john.doe@example.com",
    age=30,
    description="A sample customer",
)

session.add(customer)
session.commit()

for x in range(100):
    session.add(
        Transaction(
            amount=10 * x,
            description=f"Test Transaction {x}",
            customer_id=customer.id,
        )
    )
session.commit()
