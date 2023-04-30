from fastapi import APIRouter, Depends, HTTPException

from app.services.databases.repositories.comment.comment import CommentCrud
from app.services.databases.schemas.comment.comment import CommentDTO, CommentInDB
from app.services.databases.schemas.user.user import UserInDB
from app.services.security.permissions import get_current_active_user


router = APIRouter()


@router.post('/create')
async def create_comment(
        data: CommentDTO,
        user: UserInDB = Depends(get_current_active_user),
        crud: CommentCrud = Depends(),
) -> CommentInDB:
    if not (user.is_active or user.is_superuser):
        raise HTTPException(404, 'User is not active or admin')
    result = await crud.add_comment(
        user_id=user.id,
        data=data
    )
    if result:
        return result
    raise HTTPException(404, 'Product id does not exists')
