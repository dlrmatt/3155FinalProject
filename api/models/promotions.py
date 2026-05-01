

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_code = Column(String(100), nullable=False)
    discount_type = Column(String(100), nullable=False)
    discount_value = Column(DECIMAL, nullable=False)
    start_date = Column(DATETIME, nullable=False)
    end_date = Column(DATETIME, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    customer = Column(Integer, ForeignKey("users.id"))
    order = Column(Integer, ForeignKey("orders.id"))
