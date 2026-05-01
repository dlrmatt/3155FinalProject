from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import system_training_material as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_material = model.SystemTrainingMaterial(
        title=request.title,
        description=request.description,
        topic=request.topic,
        category=request.category,
        duration_minutes=request.duration_minutes,
    )

    try:
        db.add(new_material)
        db.commit()
        db.refresh(new_material)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_material


def read_all(db: Session):
    try:
        result = db.query(model.SystemTrainingMaterial).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, material_id):
    try:
        material = db.query(model.SystemTrainingMaterial).filter(
            model.SystemTrainingMaterial.material_id == material_id
        ).first()

        if not material:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return material


def update(db: Session, material_id, request):
    try:
        material = db.query(model.SystemTrainingMaterial).filter(
            model.SystemTrainingMaterial.material_id == material_id
        )

        if not material.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_data = request.dict(exclude_unset=True)
        material.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return material.first()


def delete(db: Session, material_id):
    try:
        material = db.query(model.SystemTrainingMaterial).filter(
            model.SystemTrainingMaterial.material_id == material_id
        )

        if not material.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        material.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)