from datetime import datetime

from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    email: str


class Product(BaseModel):
    id: int
    name: str
    type: str
    code: str
    price: float


class Warehouse(BaseModel):
    id: int
    quantity: int
    product: Product


class CarType(BaseModel):
    id: int
    type: str


class Car(BaseModel):
    id: int
    type: CarType
    capacity: int
    volume: int


class Carrier(BaseModel):
    id: int
    name: str
    phone: str
    cost: int
    cars: list[Car]


class Order(BaseModel):
    id: int
    quantity: int
    order_date: datetime
    delivery_date: datetime
    status_order: str
    new_order: bool
    distance: float
    client: Client
    carrier: Carrier
    products: list[Product]


class UserOut(BaseModel):
    login: str
    mail: str


class User(UserOut):
    password: str
