from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tracking_number = Column(String(100), unique=True, nullable=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    order_status = Column(String(100), nullable=True)
    order_type = Column(String(100), nullable=False)
    delivery_address = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    payment = Column(Integer, ForeignKey("payments.id"))
    promotion = Column(Integer, ForeignKey("promotions.id"))

    order_details = relationship("OrderDetail", back_populates="order")
