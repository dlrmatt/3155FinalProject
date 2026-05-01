from typing import Optional
from pydantic import BaseModel, ConfigDict

class SystemTrainingMaterialBase(BaseModel):
    title: str
    description: Optional[str] = None
    topic: str
    category: str
    duration_minutes: int

class SystemTrainingMaterialCreate(SystemTrainingMaterialBase):
    pass

class SystemTrainingMaterialUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    topic: Optional[str] = None
    category: Optional[str] = None
    duration_minutes: Optional[int] = None

class SystemTrainingMaterial(SystemTrainingMaterialBase):
    material_id: int

    class ConfigDict:
        from_attributes = True