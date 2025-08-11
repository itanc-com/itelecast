from fastapi import APIRouter, Depends, HTTPException

from app.api.service.send_message_to_queue import SendMessageToQueue
from app.bot.telegram_service_interface import Telegram_Service_Interface
from app.core.fastapi.depends import get_bot_service

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
    responses={404: {"description": "Resource not found"}},
    )

@router.post("/")
async def post_new_message(text: str, bot_service: Telegram_Service_Interface = Depends(get_bot_service)):
    """
    Send a new message to the Telegram bot.
    """
    try:
        send_message = SendMessageToQueue(bot_service)
        response = await send_message.execute(text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
 
