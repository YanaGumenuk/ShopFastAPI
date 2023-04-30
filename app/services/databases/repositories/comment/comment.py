from typing import Optional

from app.services.databases.models.product.comment import Comment
from app.services.databases.repositories.base import BaseCrud
from app.services.databases.schemas.comment.comment import CommentDTO, CommentInDB


class CommentCrud(BaseCrud):

    model = Comment

    async def add_comment(
            self,
            user_id: str,
            data: CommentDTO
    ) -> Optional[CommentInDB]:
        new_comment = data.__dict__
        new_comment["user_id"] = user_id
        return await self._create(data=new_comment)
