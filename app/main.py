from fastapi import FastAPI

from app.routers.v1 import users as users_v1

app = FastAPI()


app.include_router(users_v1.router, prefix="/v1")
