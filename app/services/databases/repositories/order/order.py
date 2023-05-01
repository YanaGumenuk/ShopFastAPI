from typing import Optional, List

from app.services.databases.models.order.order import Order
from app.services.databases.repositories.base import BaseCrud
from app.services.databases.schemas.order.order import OrderInDB, OrderDTO


class OrderCrud(BaseCrud):

    model = Order

    async def add_order(
            self,
            data: OrderDTO
    ) -> Optional[OrderInDB]:

        return await self._create(data=data.__dict__)

    async def get_detail_order(
            self,
            order_id: int
    ) -> Optional[OrderInDB]:
        return await self._get_relation_detail_one(
            relation_field=self.model.items,
            filter_field=self.model.id,
            filter_value=order_id
        )

