from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.service.save_message import SaveMessageToQueue
from app.api.service.send_message_directly import SendMessageDirectly
from app.bot.telegram_service_interface import Telegram_Service_Interface
from app.core.fastapi.depends import get_bot_service, get_post_repository
from app.repository.post_interface import PostInterface

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
     responses={404: {"description": "Resource not found"}, 500: {"description": "Internal Server Error"}},
    )



@router.post("/")
async def post_new_message(text: str, post_repository: Annotated[PostInterface, Depends(get_post_repository)]):
    """
    Send a new message to the Message Queue.
    """
    
    try:
        save_message = SaveMessageToQueue(post_repository)
        response = await save_message.execute(text)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
 
 
 
 
@router.post("/send",
            summary="Send message directly to Telegram channel",
            description="Sends a message immediately to the Telegram channel, bypassing the message queue",
            response_description="Message delivery confirmation"
            )
async def post_message_to_channel(text: str, bot_service: Telegram_Service_Interface = Depends(get_bot_service)):
    """
    Send a new message to the telegram channel directly.
    """
    
    
    print("Message sdasfasfasfafafasfasf")
     
     
    try:
        send_message = SendMessageDirectly(bot_service)
        response = await send_message.execute(text)
        print(f"Message sent successfully: {response}")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
