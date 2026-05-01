from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import datetime

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.get("/tailored", response_model=list[schema.TailoredOrder])
def tailored_order_view(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/date", response_model=list[schema.Order])
def read_by_date(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return controller.read_by_date(db=db, start_date=start_date, end_date=end_date)

@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
