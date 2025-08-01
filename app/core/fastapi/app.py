from fastapi import FastAPI

from app.core.fastapi.app_lifespan import lifespan
from app.core.pydantic.settings import EnvironmentType, settings

app: FastAPI = FastAPI(
    title="Itelecast API",
    description="Enabling automatic scheduling and publishing of messages to a Telegram channel.",
    version="1.0.0",
    docs_url=None if settings.environment == EnvironmentType.PRODUCTION else "/docs",
    redoc_url=None if settings.environment == EnvironmentType.PRODUCTION else "/redoc",
    lifespan=lifespan,
)
