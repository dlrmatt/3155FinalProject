from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class UserRole(str, Enum):
    customer = "customer"
    staff = "staff"
    manager = "manager"

class UserBase(BaseModel):
    name: str
    email: str
    role: UserRole
    phone: str
    address: str

class UsersCreate(UserBase):
    pass


class UsersUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class User(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True