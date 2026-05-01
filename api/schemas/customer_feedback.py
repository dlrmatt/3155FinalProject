from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerFeedbackBase(BaseModel):
    customer_id: int
    comment: str


class CustomerFeedbackCreate(CustomerFeedbackBase):
    pass


class CustomerFeedbackUpdate(BaseModel):
    comment: Optional[str] = None


class CustomerFeedback(CustomerFeedbackBase):
    id: int
    feedback_date: datetime

    class ConfigDict:
        from_attributes = True