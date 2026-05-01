from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewsBase(BaseModel):
    customer_id: int
    order_id: int
    rating: int
    comment: str
    review_date: datetime


class ReviewsCreate(ReviewsBase):
    pass


class ReviewsUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None


class Review(ReviewsBase):
    id: int

    class ConfigDict:
        from_attributes = True