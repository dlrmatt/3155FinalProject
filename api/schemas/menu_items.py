from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    item_name: str
    price: float
    food_category: str
    calories: int
    


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    price: Optional[float] = None
    food_category: Optional[str] = None
    calories: Optional[int] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True