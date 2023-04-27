from typing import Union, Dict, Optional
from datetime import timedelta
from fastapi import HTTPException

from app.core.settings import settings
from app.services.databases.repositories.base import BaseCrud
from app.services.databases.models.user.user import User
from app.services.databases.schemas.user.user import UserCreateDTO, UserInDB
from app.services.security.password_security import get_password_hash, verify_password

from app.services.security.jwt import create_access_token


class UserCrud(BaseCrud):

    model = User

    async def get(
            self,
            user_id: int = None,
            email: str = None
    ) -> Optional[UserInDB]:
        if user_id:
            return await self._get(
                field=self.model.id,
                value=user_id
            )
        return await self._get(
            field=self.model.email,
            value=email
        )

    async def create_user(
            self,
            data: UserCreateDTO
    ) -> UserInDB:
        new_user_data = data.__dict__
        password = new_user_data.pop('password')
        new_user_data["hashed_password"] = get_password_hash(password)
        return await self._create(new_user_data)

    async def authenticate(
            self,
            email: str,
            password: str
    ) -> Dict[str, str]:
        user = await self.get(email=email)

        if not user or not verify_password(password,
                                           user.hashed_password):
            raise HTTPException(
                status_code=404,
                detail="Incorrect email or password.")

        elif not await self.is_active(user):
            raise HTTPException(status_code=400,
                                detail="Inactive user")

        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {
            "access_token": create_access_token(
                data={"user_id": user.id},
                expires_delta=access_token_expires),
            "token_type": "bearer"}

    async def activate_user(
            self,
            user_id: int
    ) -> Union[UserInDB, bool]:
        data = {'is_active': True}
        return await self._update(
            field=self.model.id,
            value=user_id,
            data=data
        )

    async def is_active(
            self,
            user: UserInDB
    ) -> bool:
        return user.is_active

    async def is_superuser(
            self,
            user: UserInDB
    ) -> bool:
        return user.is_superuser