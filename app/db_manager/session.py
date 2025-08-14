from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.pydantic.settings import settings

from .session_manager import SessionManager

engine_options = {
    "echo": settings.echo_sql,
    "connect_args": {"check_same_thread": False} if settings.database_uri.startswith("sqlite") else {},
}

sessionmanager = SessionManager(settings.database_uri, engine_options)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmanager.session() as session:
        yield session