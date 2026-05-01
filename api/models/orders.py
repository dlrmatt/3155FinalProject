from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tracking_number = Column(String(100), unique=True, nullable=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(DECIMAL(8, 2), nullable=False, server_default='0.0')
    order_status = Column(String(100), nullable=True)
    order_type = Column(String(100), nullable=False)
    delivery_address = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    #  nullable for guest user
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    payment = Column(Integer, ForeignKey("payments.id"))
    promotion = Column(Integer, ForeignKey("promotions.id"))

    guest_email = Column(String(100), nullable=True)
    guest_name = Column(String(100), nullable=True)
    guest_address = Column(String(100), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")

    @property
    def menu_item_id(self) -> list[int]:
        return [detail.menu_item_id for detail in self.order_details]