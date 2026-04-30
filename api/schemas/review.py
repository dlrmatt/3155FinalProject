from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    customer_id: int
    order_id: int
    rating: int
    comment: str
    review_date: datetime


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True