from fastapi import FastAPI

from interfaces.api import routers

app = FastAPI()

app.include_router(routers.router)
