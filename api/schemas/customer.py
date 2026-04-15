from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Customers(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomersCreate(CustomerBase):
    pass


class CustomersUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customers(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True