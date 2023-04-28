from fastapi import APIRouter
from app.api.v1.user import user
from app.api.v1.login import login
from app.api.v1 import test_celery


router = APIRouter()


router.include_router(user.router,
                      prefix='/user',
                      tags=['User'])

router.include_router(login.router,
                      prefix='/login',
                      tags=['Login'])

router.include_router(test_celery.router,
                      tags=['Test_celery'])
