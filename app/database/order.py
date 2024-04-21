from typing import Optional, Type

from sqlalchemy.orm import Session

from app.database.base import inject
from app.enums.order_status import OrderStatus
from app.models import Order


@inject
def all_orders(db: Session) -> list[Type[Order]]:
    return db.query(Order).all()


@inject
def all_new_orders(db: Session) -> list[Type[Order]]:
    return db.query(Order).filter(Order.new_order).all()


@inject
def orders_by_id(client_id: int, db: Session) -> Optional[list[Type[Order]]]:
    if client_id in db.query(Order).all():
        return db.query(Order).filter(Order.client_id == client_id).all()
    return None


@inject
def change_status(order_id: int, new_status: OrderStatus, db: Session) -> Optional[Order]:
    order = db.query(Order).get(order_id)
    if order:
        order.order_status = new_status.value
        db.commit()
        db.refresh(order)
        return order
    return None


@inject
def create_order(order_data: dict, db: Session) -> Order:
    order = Order(**order_data)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
