from functools import lru_cache
from fastapi import Depends

from ...settings import Settings

__all__ = [
    'get_config',
    'get_settings'
]


async def get_config():
    import random
    print(random.randint(0, 1000))
    return DEFAULT_CONFIG


@lru_cache
async def get_settings(env_file_path: str):
    return Settings(_env_file=env_file_path)

