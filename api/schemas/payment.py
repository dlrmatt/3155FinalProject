from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Payment(BaseModel):
    order_id: int
    amount: float
    payment_method: str
    payment_status: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True