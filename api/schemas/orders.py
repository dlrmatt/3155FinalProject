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

    customer_id: int
    tracking_number: str
    order_date: datetime
    total_price: float
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
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
