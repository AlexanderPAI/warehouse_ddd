from fastapi import APIRouter

from interfaces.api.v1 import endpoints

router = APIRouter(prefix="/v1")

router.include_router(endpoints.router)
