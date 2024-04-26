from app.enums.order_status import OrderStatus
from app.main import app

import pytest
from fastapi.testclient import TestClient

from app.models import Order


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


# Logist


def test_orders(client):
    response = client.get("/logist/")
    assert response.status_code == 200


def test_new_orders(client):
    response = client.get("/logist/api/orders")
    assert response.status_code == 200


def test_change_order_status(client):
    order_id = 1
    new_status = OrderStatus.execution
    response = client.put(f"/logist/api/orders/{order_id}", json={"new_status": new_status})
    assert response.status_code == 200


def test_change_order_status_invalid_id(client):
    invalid_order_id = 9999
    new_status = OrderStatus.problems
    response = client.put(f"/logist/api/orders/{invalid_order_id}", json={"new_status": new_status})
    assert response.status_code == 404


def test_analysis(client):
    response = client.get("/logist/analysis")
    assert response.status_code == 200


def test_orders_analysis(client):
    response = client.get("/logist/api/analysis")
    assert response.status_code == 200


# Client


def test_user_orders(client):
    response = client.get("/client/")
    assert response.status_code == 200


def test_get_all_user_orders(client):
    client_id = 1
    response = client.get(f"/client/api/orders/{client_id}")
    assert response.status_code == 200


def test_get_all_user_orders_no_orders(client):
    client_id = 2
    response = client.get(f"/client/api/orders/{client_id}")
    assert response.status_code == 200


def test_create_new_order(client):
    new_order_data = {
        'quantity': 10,
        'distance': 50.5,
        'client_id': 1,
        'carrier_id': 2,
        "products": [
            {
                "name": "Блендер POLARIS",
                "type": "МБТ",
                "code": "PHB 1065",
                "price": 99.87
            }
        ]
    }
    new_order = Order(**new_order_data)
    response = client.post("/client/api/orders/create", json=new_order.dict())
    assert response.status_code == 200


def test_create_new_order_invalid_data(client):
    invalid_order_data = {
        'quantity': 'abc',
        'order_date': '2022-01-01',
        'delivery_date': '2022-01-10 12:00:00',
        'status_order': 'new_status',
        'new_order': 'True',
        'distance': '100.5',
        'client_id': 'abc',
        'carrier_id': 3,
        'products': [
            {
                'name': 'Некорректный товар',
                'type': 'Тип товара',
                'code': 'Код товара',
                'price': 'abc'
            }
        ]
    }
    invalid_order = Order(**invalid_order_data)
    response = client.post("/client/api/orders/create", json=invalid_order.dict())
    assert response.status_code == 400


# Warehouse


def test_warehouse(client):
    response = client.get("/warehouse/")
    assert response.status_code == 200


def test_products(client):
    response = client.get("/warehouse/api/products")
    assert response.status_code == 200


def test_get_product(client):
    product_name = "Блендер POLARIS"
    response = client.get(f"/warehouse/api/search?product_name={product_name}")
    assert response.status_code == 200


def test_get_product_not_found(client):
    product_name = "Invalid Product"
    response = client.get(f"/warehouse/api/search?product_name={product_name}")
    assert response.status_code == 404


# Auth


def test_authorization(client):
    response = client.get("/auth/")
    assert response.status_code == 200


def test_registration(client):
    response = client.get("/reg/")
    assert response.status_code == 200
