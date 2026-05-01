from sqlalchemy import Column, Integer, String, Boolean
from ..dependencies.database import Base

class SystemTrainingMaterial(Base):
    __tablename__ = "system_training_materials"

    material_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(500), nullable=True)
    topic = Column(String(100), nullable=False)
    category = Column(String(100), nullable=True)
    duration_minutes = Column(Integer, nullable=False)