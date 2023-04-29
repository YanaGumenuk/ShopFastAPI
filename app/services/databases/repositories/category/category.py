from typing import Union, List, Optional

from app.services.databases.models.product.category import Category
from app.services.databases.repositories.base import BaseCrud
from app.services.databases.schemas.category.category import CategoryDTO, CategoryInDB


class CategoryCrud(BaseCrud):

    model = Category

    async def add_category(
            self,
            data: CategoryDTO
    ) -> Optional[CategoryInDB]:
        return await self._create(data=data.__dict__)

    async def get_list(
            self,
            limit: int,
            offset: int,
    ) -> List[Optional[CategoryInDB]]:

        return await self._get_list(
            limit=limit,
            offset=offset
        )


    async def detail_category(
            self,
            category_id: int
    ) -> Optional[CategoryInDB]:

        return await self._get(
            field=self.model.id,
            value=category_id,
        )
