from models import (
    Customer,
    CustomerCreate,
    CustomerPlan,
    CustomerUpdate,
    Plan,
    StatusEnum,
)
from db import SessionDep
from fastapi import APIRouter, Query, status, HTTPException
from sqlmodel import select

router = APIRouter()


@router.post("/customer", response_model=Customer, tags=["customer"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):

    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)

    # This is an async function for ubpdating the id (simulating what happens with a DB)
    # customer_list.append(customer)
    # customer.id = len(customer_list)
    return customer


@router.get("/customer", response_model=list[Customer], tags=["customer"])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all()


@router.get(
    "/customer/{customer_id}", response_model=Customer | None, tags=["customer"]
)
async def read_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    return customer


@router.delete("/customer/{customer_id}", tags=["customer"])
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    session.delete(customer)
    session.commit()
    return {"detail": "ok"}


@router.patch(
    "/customer/{customer_id}",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    tags=["customer"],
)
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
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db


@router.post("/customer/{customer_id}/plans/{plan_id}", tags=["customer"])
async def subscribe_customer_to_plan(
    customer_id: int,
    plan_id: int,
    session: SessionDep,
    plan_status: StatusEnum = Query(),
):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)

    if not customer_db or not plan_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer or Plan not found"
        )

    customer_plan_db = CustomerPlan(
        customer_id=customer_db.id, plan_id=plan_db.id, status=plan_status
    )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db


@router.get("/customer/{customer_id}/plans", tags=["customer"])
async def list_customer_subscriptions(
    customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()
):
    customer_db = session.get(Customer, customer_id)

    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    query = (
        select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plan_status)
    )
    plans = session.exec(query).all()
    return plans
