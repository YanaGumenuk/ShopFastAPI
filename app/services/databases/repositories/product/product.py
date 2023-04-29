from typing import Optional, List

from app.services.databases.models.product.product import Product
from app.services.databases.repositories.base import BaseCrud
from app.services.databases.schemas.product.product import (ProductCreateDTO,
                                                            ProductUpdateDTO,
                                                            ProductInDB)


class ProductCrud(BaseCrud):

    model = Product

    async def add_product(
            self,
            data: ProductCreateDTO
    ) -> Optional[ProductInDB]:
        return await self._create(data=data.__dict__)

    async def get_detail_product(
            self,
            product_id: int,
    ) -> Optional[ProductInDB]:
        return await self._get(
            field=self.model.id,
            value=product_id
        )
