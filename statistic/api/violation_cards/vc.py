from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/yesterday")
async def get_vc_stats(id: int):
    return {'id': id}