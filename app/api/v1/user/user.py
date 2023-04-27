from typing import Union, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.services.databases.schemas.user.user import UserCreateDTO, UserInDB
from app.services.databases.repositories.user.user import UserCrud


router = APIRouter()


@router.post('/create')
async def user_create(
        user: UserCreateDTO,
        crud: UserCrud = Depends()
) -> Dict[str, Union[UserInDB, str]]:
    result = await crud.create_user(user)

    if result:
        return {'result': result,
                'message': 'Confirm your mail'}
    raise HTTPException(404, "Invalid values entered or user already exists")