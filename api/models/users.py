from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
