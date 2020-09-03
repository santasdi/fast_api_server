from functools import lru_cache
from pydantic import BaseSettings, IPvAnyAddress


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str

    SERVER_NAME: str
    SERVER_HOST: IPvAnyAddress

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        case_sensitive = True


@lru_cache
def get_settings(env_file_path: str):
    return Settings(_env_file=env_file_path)
