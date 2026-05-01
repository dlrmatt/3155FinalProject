from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import system_training_material as controller
from ..schemas import system_training_material as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['System_Training_Materials'],
    prefix="/system_training_materials"
)

@router.post("/", response_model=schema.SystemTrainingMaterial)
def create(request: schema.SystemTrainingMaterialCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.SystemTrainingMaterial])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{material_id}", response_model=schema.SystemTrainingMaterial)
def read_one(material_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, material_id=material_id)


@router.put("/{material_id}", response_model=schema.SystemTrainingMaterial)
def update(material_id: int, request: schema.SystemTrainingMaterialUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, material_id=material_id)


@router.delete("/{material_id}")
def delete(material_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, material_id=material_id)