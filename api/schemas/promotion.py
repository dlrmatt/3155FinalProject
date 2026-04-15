from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Promotion(BaseModel):
    name: str
    description: str
    discount_percentage: float
    start_date: datetime
    end_date: datetime


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    discount_percentage: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True