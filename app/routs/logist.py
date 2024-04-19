from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(
    prefix="/logist",
    tags=['Logist']
)


@router.get('/')
def new_orders():
    return FileResponse("templates/orders.html")


@router.get('/analysis')
def new_orders():
    return FileResponse("templates/analysis.html")
