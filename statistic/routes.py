from fastapi import APIRouter

from .api.violation_cards import vc


api_router = APIRouter()
api_router.include_router(
    vc.router, prefix="/violation_cards", tags=["violation_cards"]
)