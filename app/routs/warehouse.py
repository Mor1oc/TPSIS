from fastapi import APIRouter

router = APIRouter(
    prefix="/warehouse",
    tags=['Warehouse']
)


@router.get('/')
def warehouse_orders():
    return {"message": ""}
