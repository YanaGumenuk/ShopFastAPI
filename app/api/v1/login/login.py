from typing import Dict, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.services.databases.schemas.tokens.tokens import Token
from app.services.security.jwt import verify_new_token

from app.services.databases.repositories.user.user import UserCrud

router = APIRouter()


@router.post('/token')
async def login_access_token(
        crud: UserCrud = Depends(),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    return await crud.authenticate(
        email=form_data.username,
        password=form_data.password)

@router.get('/register/{token}')
async def activate_user(
        token: str,
        crud: UserCrud = Depends()
) -> Dict[str, Union[bool, str]]:
    email = verify_new_token(token).get('email')
    user = await crud.get(email=email)
    if user:
        await crud.activate_user(user_id=user.id)
        return {"success": True,
                'detail': f'User {user.username} has registered by email: {user.email} '}
    raise HTTPException(404, 'Registration time expired')