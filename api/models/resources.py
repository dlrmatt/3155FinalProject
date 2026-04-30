from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    quantity = Column(Integer, index=True, nullable=False, server_default='0.0')

    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), unique=True)
