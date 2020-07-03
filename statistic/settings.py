import functools
import pathlib

import yaml


BASE_DIR = pathlib.Path(__file__).parent.parent

# CONFIG_DEFAULT_PATH = pathlib.Path(BASE_DIR) / 'conf' / 'local.yaml'
#
#
# def get_config(path):
#     with open(path, encoding='utf-8') as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
#
# DEFAULT_CONFIG = get_config(CONFIG_DEFAULT_PATH)

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, PostgresDsn, validator, IPvAnyAddress


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    CONFIG_FILE_NAME: str

    # server settings
    SERVER_NAME: Optional[str] = ""
    SERVER_HOST: IPvAnyAddress
    SERVER_PORT: int

    # database
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB_NAME') or ''}",
        )

    # sources service
    SOURCES_HOST: IPvAnyAddress
    SOURCES_PORT: int

    class Config:
        env_file = pathlib.Path(BASE_DIR) / 'conf' / '.env'


async def get_settings(env_filepath: str = None):
    if env_filepath is not None:
        return Settings(_env_file=env_filepath)
    return Settings()
