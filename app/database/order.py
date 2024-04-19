from sqlalchemy.orm import Session

from app.database.base import inject
from app.models import Order


@inject
def all_orders(db: Session):
    return db.query(Order).all()


@inject
def all_new_orders(db: Session):
    return db.query(Order).filter(Order.new_order).all()


@inject
def orders_by_id(user_id: int, db: Session):
    return db.query(Order).filter(Order.client_id == user_id).all()


@inject
def create_order(order_data: dict, db: Session):
    order = Order(**order_data)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
