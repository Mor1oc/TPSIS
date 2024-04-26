from fastapi import APIRouter, HTTPException, requests
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


@router.put('/api/orders')
def calculate_route(order_data):
    response = requests.post('https://api.routing.yandex.net/v2/route'
                             '? apikey=<string>'
                             '& waypoints=<lat1,lon1|lat2,lon2|...>'
                             '& [mode=<string>]'
                             '& [departure_time=<integer>]'
                             '& [avoid_tolls=<boolean>]'
                             '& [avoid_zones=<lat1,lon1|lat2,lon2|...>&avoid_zones=<lat1,lon1|lat2,lon2|...>]'
                             '& [traffic=<string>]'
                             '& [weight=<float>]'
                             '& [axle_weight=<float>]'
                             '& [max_weight=<float>]'
                             '& [height=<float>]'
                             '& [width=<float>]'
                             '& [length=<float>]'
                             '& [payload=<float>]'
                             '& [eco_class=<integer>]'
                             '& [has_trailer=<boolean>]'
                             , json=order_data)
    if response.status_code == 200:
        route_info = response.json()
        return route_info
    else:
        return {"error": "Не удалось получить маршрут"}


@router.get('/analysis')
def analysis():
    return FileResponse("templates/analysis.html")


@router.get('/api/analysis')
def orders_analysis():
    return all_orders()
