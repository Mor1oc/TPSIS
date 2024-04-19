from fastapi import APIRouter
from starlette.responses import FileResponse
from app.database.order import orders_by_id

router = APIRouter(
    prefix="/client",
    tags=['Client']
)


@router.get('/')
def user_orders():
    return FileResponse("templates/client.html")


@router.get('/api/orders/{user_id}')
def all_user_orders(user_id: int):
    return orders_by_id(user_id)
