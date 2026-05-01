from datetime import datetime
from collections import Counter
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
import uuid
from ..models import menu_items as menu_model
from ..models import order_details as order_detail_model
from ..models import promotions as promotion_model
from ..models import resources as resource_model

def create(db: Session, request):
    total_price = 0.0
    tracking_number = "ORD-" + str(uuid.uuid4())[:8]
    unique_ids = list(set(request.menu_item_id))
    menu_items_list = db.query(menu_model.MenuItem).filter(menu_model.MenuItem.menu_item_id.in_(unique_ids)).all()
    item_lookup = {item.menu_item_id: item for item in menu_items_list}
    for item_id in request.menu_item_id:
        menu_item = item_lookup.get(item_id)
        if menu_item:
            total_price += float(menu_item.price)

    if request.promotion_id:
        promotion = db.query(promotion_model.Promotions).filter(promotion_model.Promotions.id == request.promotion_id).first()       
        if promotion:
            total_price -= float(promotion.discount_value)
    
    new_order = model.Order(
        customer_id=request.customer_id,
        tracking_number=tracking_number,
        total_price=total_price,
        order_date=datetime.now(),
        description=request.description,
        order_type=request.order_type,
        delivery_address=request.delivery_address,
        order_status=request.order_status,
        guest_email=request.guest_email,
        guest_name=request.guest_name,
        guest_address=request.guest_address,
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    item_counts = Counter(request.menu_item_id)

    for item_id, qty in item_counts.items():

        new_detail = order_detail_model.OrderDetail(
            order_id=new_order.id,
            menu_item_id=item_id,
            quantity=qty
        )
        try:
            db.add(new_detail)
            db.commit()
            db.refresh(new_detail)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

        inventory_item = db.query(resource_model.Resource).filter(
            resource_model.Resource.menu_item_id == item_id
        ).first()

        if inventory_item:
            if inventory_item.quantity < qty:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Not enough stock for menu item {item_id}. Only {inventory_item.quantity} left!"
                )
            inventory_item.quantity -= qty

            if inventory_item.quantity == 0:
                out_of_stock_item = db.query(menu_model.MenuItem).filter(
                    menu_model.MenuItem.menu_item_id == item_id
                ).first()

                if out_of_stock_item:
                    out_of_stock_item.is_available = False
            db.commit()
            db.refresh(inventory_item)
    
    return new_order

def read_by_date(db: Session,start_date: datetime, end_date: datetime):
    try:
        result = db.query(model.Order).filter(model.Order.order_date >= start_date, model.Order.order_date <= end_date).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no orders found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
