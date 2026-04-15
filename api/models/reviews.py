from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review = Column(String(100), nullable=False)
    score = Column(Integer, nullable=False)

    customer = Column(Integer, ForeignKey("customers.id"))
    order = Column(Integer, ForeignKey("orders.id"))
