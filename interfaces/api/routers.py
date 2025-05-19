from fastapi import APIRouter

from interfaces.api.v1 import routers

router = APIRouter(prefix="/api")

router.include_router(routers.router)
