from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promotion_code: str
    discount_type: str
    discount_value: float
    start_date: datetime
    end_date: datetime
    is_active: bool


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotion_code: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_active: Optional[bool] = None

    class PromotionResponse(PromotionBase):
        id: int


    class ConfigDict:
        from_attributes = True