from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.services.security.permissions import get_current_active_superuser
from app.services.databases.schemas.product.product import ProductCreateDTO, ProductInDB

from app.services.databases.repositories.product.product import ProductCrud


router = APIRouter()


@router.post('/create', dependencies=[Depends(get_current_active_superuser)])
async def create_product(
        data: ProductCreateDTO,
        crud: ProductCrud = Depends()
) -> Optional[ProductInDB]:
    result = await crud.add_product(data=data)
    if result:
        return result
    raise HTTPException(404, 'Invalid data entered, category_id may be missing')


@router.get('/get_product/{product_id}')
async def get_product(
        product_id: int,
        crud: ProductCrud = Depends()
) -> ProductInDB:
    result = await crud.get_detail_product(product_id)
    if result:
        return result
    raise HTTPException(404, "Product does not exists")