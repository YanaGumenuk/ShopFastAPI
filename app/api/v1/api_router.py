from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.get('/test')
async def test() -> Dict[str, str]:
    return {'message': 'test succesfull'}
