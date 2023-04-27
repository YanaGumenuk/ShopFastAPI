from typing import TypeVar, Type, ClassVar
from fastapi import Depends

from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from asyncpg import UniqueViolationError

from app.core.session import get_session

Model = TypeVar("Model")


class BaseCrud:

    model: ClassVar[Type[Model]]

    def __init__(
            self,
            db: AsyncSession = Depends(get_session)
    ):
        self._session = db

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