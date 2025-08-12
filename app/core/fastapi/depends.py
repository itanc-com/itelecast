from typing import Annotated

import httpx
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

#from sqlalchemy.ext.asyncio import AsyncSession
from app.bot.telegram_service import TelegramService
from app.bot.telegram_service_interface import Telegram_Service_Interface
from app.core.fastapi.app import app
from app.core.fastapi.app_state import AppStates, get_app_state
from app.core.pydantic.settings import settings
from app.db_manager.session import get_db_session
from app.repository.post_interface import PostInterface
from app.repository.post_repository import PostRepository

#from app.db.session import get_db_session


def get_httpx_client() -> httpx.AsyncClient:
    """
    Retrieve the shared instance of httpx.AsyncClient from the application state.

    Returns:
        httpx.AsyncClient: The asynchronous HTTP client stored in the application's state.
    """
    return get_app_state(app, AppStates.HTTPX_CLIENT)


def get_bot_service(
    httpx_client: Annotated[httpx.AsyncClient, Depends(get_httpx_client)],
) -> Telegram_Service_Interface:
    return TelegramService(bot_token=settings.bot_http_api_token,client=httpx_client)


def get_post_repository(
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
) -> PostInterface:
    return PostRepository(db_session)

