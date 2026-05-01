from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import sales_data as controller
from ..schemas import sales_data as schema
from datetime import date

router = APIRouter(
    prefix="/sales_data",
    tags=["Sales_Data"]
)

@router.get("/all", response_model=schema.SalesData)
def get_revenue(db: Session = Depends(get_db)):
    return controller.get_total_revenue(db=db)

@router.get("/date", response_model=schema.SalesData)
def get_revenue_by_date(
    target_date: date,
    db: Session = Depends(get_db)
):
    return controller.get_total_revenue_by_date(db=db, target_date=target_date)