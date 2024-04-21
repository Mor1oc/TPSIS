from typing import Type

from sqlalchemy.orm import Session

from app.database.base import inject
from app.models import Product, Warehouse


@inject
def all_products(db: Session) -> list[Type[Product]]:
    return db.query(Product).join(Warehouse).all()


@inject
def find_product(product_name: str, db: Session) -> list[Type[Product]]:
    return db.query(Product).filter(Product.name == product_name).all()
