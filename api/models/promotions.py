from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotionCode = Column(String(100), nullable=False)
    expirationDate = Column(DATETIME, nullable=False)
    discount = Column(Integer, nullable=False)

    customer = Column(Integer, ForeignKey("customers.id"))
    order = Column(Integer, ForeignKey("orders.id"))
