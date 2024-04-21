from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse

from app.database.order import change_status, all_new_orders, all_orders
from app.enums.order_status import OrderStatus

router = APIRouter(
    prefix="/logist",
    tags=['Logist']
)


@router.get('/')
def orders():
    return FileResponse("templates/orders.html")


@router.get('/api/orders')
def new_orders():
    return all_new_orders()


@router.put('/api/orders/{order_id}')
def change_order_status(order_id: int, new_status: OrderStatus):
    changed_order = change_status(order_id, new_status)
    if changed_order:
        return changed_order
    return HTTPException(status_code=404, detail="Такого заказа нет")


@router.get('/analysis')
def analysis():
    return FileResponse("templates/analysis.html")


@router.get('/api/analysis')
def orders_analysis():
    return all_orders()
