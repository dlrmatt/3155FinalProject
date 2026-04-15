from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trackingNumber = Column(String(100), unique=True, nullable=True)
    orderDate = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    totalPrice = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    orderStatus = Column(String(100), nullable=True)

    customer = Column(Integer, ForeignKey("customers.id"))
    payment = Column(Integer, ForeignKey("payments.id"))
    promotion = Column(Integer, ForeignKey("promotions.id"))
