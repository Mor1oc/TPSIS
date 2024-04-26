from datetime import datetime

from sqlalchemy import Column, Table, String, Integer, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base
from app.enums.order_status import OrderStatus


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    code = Column(String, nullable=False)
    price = Column(Float, nullable=False)


class Warehouse(Base):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product')


class CarType(Base):
    __tablename__ = 'car_type'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)


car_carrier = Table('car_carrier', Base.metadata,
                    Column('car_id', Integer, ForeignKey('cars.id')),
                    Column('carrier_id', Integer, ForeignKey('carriers.id')))


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey('car_type.id'))
    type = relationship('CarType')
    capacity = Column(Integer, nullable=False)
    volume = Column(Integer, nullable=False)


class Carrier(Base):
    __tablename__ = 'carriers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    cars = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', secondary=car_carrier, backref='carriers')


orders_products = Table('orders_products', Base.metadata,
                        Column('order_id', Integer, ForeignKey('orders.id')),
                        Column('product_id', Integer, ForeignKey('products.id')))


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=None)
    delivery_date = Column(DateTime, default=None)
    status_order = Column(String, default=OrderStatus.new.value)
    new_order = Column(Boolean, default=True)
    distance = Column(Float, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', backref='orders')
    carrier_id = Column(Integer, ForeignKey('carriers.id'))
    carrier = relationship('Carrier')
    products = relationship('Product', secondary=orders_products, backref='orders')
