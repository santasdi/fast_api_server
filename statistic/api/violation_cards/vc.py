from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_config

router = APIRouter()


@router.get("/config")
async def get_vc_stats(config: dict = Depends(get_config, use_cache=True)):
    return config


@router.get("/next_config")
async def get_vc_stats(config: dict = Depends(get_config)):
    return config
