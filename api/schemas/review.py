from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Review(BaseModel):
    rating: int
    comment: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True