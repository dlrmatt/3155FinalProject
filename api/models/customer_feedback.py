from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    comment = Column(String(100), nullable=False)
    feedback_date = Column(DATETIME, nullable=False)

    customer_id = Column(Integer, ForeignKey("users.id"))