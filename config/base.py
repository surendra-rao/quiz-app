import os
from typing import ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import Optional


class Settings(BaseSettings):
    # Check if running in Docker and choose the appropriate .env file
    env_file: ClassVar[str] = (
        "./secrets/.env.docker" if os.getenv("DOCKER_ENV") else "./secrets/.env"
    )
    model_config = SettingsConfigDict(env_file=env_file, extra="allow")

    postgres_database: Optional[str] = None
    postgres_username: Optional[str] = None
    postgres_password: Optional[str] = None
    postgres_host: Optional[str] = None
    postgres_port: Optional[int] = None


settings = Settings()