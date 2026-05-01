from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class PaymentMethod(str, Enum):
    gift_card = "gift_card"
    credit_card = "credit_card"
    debit_card = "debit_card"

class Payment(BaseModel):
    order_id: int
    amount: float
    card_info: str
    payment_method: PaymentMethod


class PaymentCreate(Payment):
    pass


class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    amount: Optional[float] = None
    payment_method: Optional[PaymentMethod] = None
    payment_status: Optional[str] = None


class Payment(Payment):
    id: int
    payment_status: str
    payment_date: datetime
    class ConfigDict:
        from_attributes = True