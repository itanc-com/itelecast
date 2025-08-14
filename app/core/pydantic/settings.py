from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    LOCAL = "local"
    TESTING = "testing"
    
class Settings(BaseSettings):
    environment: EnvironmentType
    bot_http_api_token: str
    bot_username: str
    channel_id: str
    database_uri: str

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file="./app/.env",
        env_file_encoding="utf-8",
    )

    @property
    def echo_sql(self) -> bool:
        """Enable SQL echo for development environment"""
        return self.environment == EnvironmentType.DEVELOPMENT


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
