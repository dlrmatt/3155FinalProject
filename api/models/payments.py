from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payments(Base):
    __tablename__ = "payments"

    amount = Column(DECIMAL, nullable=False)
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_info = Column(String(100), nullable=False)
    payment_status = Column(String(100), nullable=False)
    payment_method = Column(String(100), nullable=False)
    payment_date = Column(DATETIME, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"))