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
    totalPrice = 0.0
    trackingNumber = "ORD-" + str(uuid.uuid4())[:8]

    menu_items_list = db.query(menu_model.MenuItem).filter(menu_model.MenuItem.id.in_(request.menu_item_id)).all()
    for menu_item in menu_items_list:
        totalPrice += menu_item.price

    if request.promotion_id:
        promotion = db.query(promotion_model.Promotions).filter(promotion_model.Promotions.id == request.promotion_id).first()       
        if promotion:
            totalPrice -= promotion.discount
    
    new_order = model.Order(
        customer_id=request.customer_id,
        tracking_number=trackingNumber,
        total_price=totalPrice
    )

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    for menu_item in menu_items_list:
        new_detail = order_detail_model.OrderDetail(
            order_id=new_order.id,
            menu_item_id=menu_item.id,
            quantity=1
        )
        try:
            db.add(new_detail)
            db.commit()
            db.refresh(new_detail)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
        inventory_item = db.query(resource_model.Resource).filter(
            resource_model.Resource.name == menu_item.item_name).first()    

        if inventory_item:
            inventory_item.amount -= 1
            db.commit()
            db.refresh(inventory_item)
    
    return new_order


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
