from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cardInfo = Column(String(100), nullable=False)
    transactionStatus = Column(String(100), nullable=False)
    paymentType = Column(String(100), nullable=False)    
