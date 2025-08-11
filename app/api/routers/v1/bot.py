from fastapi import APIRouter, Depends, HTTPException

from app.api.service.get_bot_info import GetBotInfo
from app.bot.telegram_service_interface import Telegram_Service_Interface
from app.core.fastapi.depends import get_bot_service

router = APIRouter(
    prefix="/bot",
    tags=["Bot"],
    responses={500: {"description": "Internal Server Error"}},
)

@router.get("/info")
async def get_bot_info(bot_service: Telegram_Service_Interface = Depends(get_bot_service)):
    """
    Get information about the bot.
    """

    try:
        return await GetBotInfo(bot_service).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))