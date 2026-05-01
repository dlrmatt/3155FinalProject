from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class FoodCategory(str, Enum):
    vegan = "vegan"
    vegetarian = "vegetarian"
    glutenfree = "glutenfree"


class MenuItemBase(BaseModel):
    item_name: str
    description: Optional[str] = None
    price: float
    food_category: FoodCategory
    calories: int
    is_available: bool


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    price: Optional[float] = None
    food_category: Optional[str] = None
    calories: Optional[int] = None


class MenuItem(MenuItemBase):
    menu_item_id: int

    class ConfigDict:
        from_attributes = True