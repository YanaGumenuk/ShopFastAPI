from app.services.databases.repositories.base import BaseCrud
from app.services.databases.models.user.user import User
from app.services.databases.schemas.user.user import UserCreateDTO, UserInDB
from app.services.security.password_security import get_password_hash


class UserCrud(BaseCrud):

    model = User

    async def create_user(
            self,
            data: UserCreateDTO
    ) -> UserInDB:
        new_user_data = data.__dict__
        password = new_user_data.pop('password')
        new_user_data["hashed_password"] = get_password_hash(password)
        return await self._create(new_user_data)