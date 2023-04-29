from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException

from app.services.databases.repositories.category.category import CategoryCrud
from app.services.databases.schemas.category.category import CategoryDTO, CategoryInDB
from app.services.security.permissions import get_current_active_superuser

router = APIRouter()


@router.post('/create', dependencies=[Depends(get_current_active_superuser)])
async def category_create(
        data: CategoryDTO,
        crud: CategoryCrud = Depends()
) -> CategoryInDB:
    result = await crud.add_category(data=data)
    if result:
        return result
    raise HTTPException(404, "An invalid element was passed, "
                       "or a category with the specified name"
                       " already exists")


@router.get('/list')
async def get_list(
        offset: int = 0,
        limit: int = 20,
        crud: CategoryCrud = Depends()
) -> List[Optional[CategoryInDB]]:
    result = await crud.get_list(
        limit=limit,
        offset=offset
    )
    return result



@router.get('/detail/{cat_id}')
async def get_category(
        category_id: int,
        crud: CategoryCrud = Depends()
) -> CategoryInDB:
    result = await crud.detail_category(category_id=category_id)
    if result:
        return result
    raise HTTPException(404, 'Category not found')

