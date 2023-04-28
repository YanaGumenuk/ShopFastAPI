from typing import Union, Dict
from fastapi import APIRouter, Depends, HTTPException
from app.services.databases.schemas.user.user import UserCreateDTO, UserInDB
from app.services.databases.repositories.user.user import UserCrud
from app.services.tasks.tasks import task_send_new_account

from app.services.security.jwt import generate_new_token

router = APIRouter()


@router.post('/create')
async def user_create(
        user: UserCreateDTO,
        crud: UserCrud = Depends()
) -> Dict[str, Union[UserInDB, str]]:
    result = await crud.create_user(user)
    token = generate_new_token(user.email)
    task_send_new_account.delay(
        email_to=user.email,
        username=user.username,
        token=token
    )

    if result:
        return {'result': result,
                'message': 'Confirm your mail'}
    raise HTTPException(404, "Invalid values entered or user already exists")