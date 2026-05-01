from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
# for deliver and takeout feature
class OrderType(str, Enum):
    delivery = "delivery"
    takeout = "takeout"

class OrderBase(BaseModel):

    customer_id: Optional[int] = "null"
    guest_name: str
    guest_email: str
    guest_address: str
    description: Optional[str] = None
    order_status: str
    order_type: OrderType
    delivery_address: Optional[str] = None

class OrderCreate(OrderBase):
    menu_item_id: list[int]
    promotion_id: Optional[int] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    order_type: Optional[OrderType] = None
    delivery_address: Optional[str] = None

class Order(OrderBase):
    id: int
    tracking_number: str
    total_price: float
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

class TailoredOrder(BaseModel):
    id: int
    order_date: datetime
    order_type: OrderType
    menu_item_id: list[int]
    description: Optional[str] = None

    class ConfigDict:
        from_attributes = True
