from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from statistic.routes import api_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credetials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api/v1")
