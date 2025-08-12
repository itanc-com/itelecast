from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI
from httpx import AsyncClient

from app.core.fastapi.app_state import AppStates, set_app_state
from app.db_manager.base import Base
from app.db_manager.session import sessionmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Startup
    
    set_app_state(app, AppStates.APP_START_TIME, datetime.now(timezone.utc).replace(microsecond=0))
    
    httpx_client = AsyncClient()
    set_app_state(app, AppStates.HTTPX_CLIENT, httpx_client)

    
    async with sessionmanager.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield  # App runs between this and the end

    # Shutdown
    await httpx_client.aclose()
    await sessionmanager.close()
