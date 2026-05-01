from email.policy import default

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=True)
    description = Column(String(500), nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    food_category = Column(String(100), nullable=True)
    calories = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=False, nullable=False)
