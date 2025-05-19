from fastapi import APIRouter

endpoints_router = APIRouter()


@endpoints_router.get(path="/")
async def root():
    return {"Hello: World"}
