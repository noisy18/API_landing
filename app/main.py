from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.requests import router as request_router

app = FastAPI(
    title="GearsAcademy",
)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(request_router)