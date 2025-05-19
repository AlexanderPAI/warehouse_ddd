from fastapi import APIRouter

from interfaces.api.v1.endpoints import endpoints_router

router = APIRouter(prefix="/v1")

router.include_router(endpoints_router)
