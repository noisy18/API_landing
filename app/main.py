from fastapi import FastAPI

from app.api.requests import router as request_router

app = FastAPI()

app.include_router(request_router)