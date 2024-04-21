from fastapi import APIRouter
from starlette.responses import FileResponse

from app.database.product import all_products, find_product

router = APIRouter(
    prefix="/warehouse",
    tags=['Warehouse']
)


@router.get('/')
def warehouse():
    return FileResponse('templates/warehouse.html')


@router.get('/api/products')
def products():
    return all_products()


@router.get('/api/search')
def get_product(product_name: str):
    product = find_product(product_name)
    if product:
        return product
    return {"message": "Товар не найден"}
