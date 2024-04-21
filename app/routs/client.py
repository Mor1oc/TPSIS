from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse
from app.database.order import orders_by_id, create_order

router = APIRouter(
    prefix="/client",
    tags=['Client']
)


@router.get('/')
def user_orders():
    return FileResponse("templates/client.html")


@router.get('/api/orders/{client_id}')
def get_all_user_orders(client_id: int):
    orders = orders_by_id(client_id)
    if orders:
        return orders_by_id(client_id)
    return {"message": "У вас нет заказов"}


@router.post('/api/orders/create')
def create_new_order(new_order: dict):
    order = create_order(new_order)
    if order:
        return order
    else:
        return {"message": "Не получилось создать заказ"}
