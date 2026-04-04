from models import Invoice
from fastapi import APIRouter

router = APIRouter()


@router.post("/invoice", tags=["invoices"])
async def create_invoice(invoice_data: Invoice):
    return invoice_data
