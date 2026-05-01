from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class SalesData(Base):
    __tablename__ = "sales_data"

    total_revenue = Column(DECIMAL(12, 2), nullable=False, server_default='0.0')
