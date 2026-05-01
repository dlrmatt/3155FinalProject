from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from ..models import payments as payment_model
from datetime import date


def get_total_revenue(db: Session):
    total = db.query(func.sum(payment_model.Payments.amount)).filter(
        payment_model.Payments.payment_status == "Paid"
    ).scalar()
    return {"total_revenue": total or 0.0}


def get_total_revenue_by_date(db: Session, target_date: date):
    total = db.query(func.sum(payment_model.Payments.amount)).filter(
        payment_model.Payments.payment_status == "Paid",
        func.date(payment_model.Payments.payment_date) == target_date
    ).scalar()

    return {"total_revenue": total or 0.0}