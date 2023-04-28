from typing import TypeVar, Type, ClassVar, Any, Optional, List
from fastapi import Depends

from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from asyncpg import UniqueViolationError
from sqlalchemy import update, select, delete

from app.core.session import get_session

Model = TypeVar("Model")


class BaseCrud:

    model: ClassVar[Type[Model]]

    def __init__(
            self,
            db: AsyncSession = Depends(get_session)
    ):
        self._session = db

    async def _get(
            self,
            field: Any,
            value: Any,
    ) -> Optional[Model]:

        stmt = (
            select(self.model)
            .where(field == value)
        )

        result = await self._session.scalar(stmt)
        return result

    async def _create(
            self,
            data: dict
    ) -> Model:
        try:
            new_obj = self.model(**data)
            self._session.add(new_obj)
            await self._session.commit()
            await self._session.refresh(new_obj)
            return new_obj
        except UniqueViolationError:
            return None
        except IntegrityError:
            return None
        except UnmappedInstanceError:
            return None

    async def _update(
            self,
            field: Any,
            value: Any,
            data: dict
    ) -> Model:
        stmt = (
            update(self.model)
            .where(field == value)
            .values(**data)
            .returning(self.model)
        )
        try:
            result = await self._session.scalar(stmt)
            await self._session.commit()
            await self._session.refresh(result)
            return result
        except UnmappedInstanceError:
            return None
        except IntegrityError:
            return None

    async def _get_list(
            self,
            limit: int,
            offset: int,
            field: Any = None,
            value: Any = None,
    ) -> Optional[List[Model]]:

        if field and value:
            stmt = (
                select(self.model)
                .where(field == value)
                .offset(offset)
                .limit(limit)
            )
        else:
            stmt = (
                select(self.model)
                .offset(offset)
                .limit(limit)
            )
        result = await self._session.scalars(stmt)
        return result.all()

    async def _delete(
            self,
            field: Any,
            model_id: int,
    ) -> bool:
        stmt = (
            delete(self.model)
            .where(field == model_id)
        )

        result = await self._session.execute(stmt)
        await self._session.commit()
        if result.rowcount:
            return True
        return None

    async def _update(
            self,
            field: Any,
            value: Any,
            data: dict
    ) -> Model:
        stmt = (
            update(self.model)
            .where(field == value)
            .values(**data)
            .returning(self.model)
        )
        try:
            result = await self._session.scalar(stmt)
            await self._session.commit()
            await self._session.refresh(result)
            return result
        except UnmappedInstanceError:
            return None
        except IntegrityError:
            return None