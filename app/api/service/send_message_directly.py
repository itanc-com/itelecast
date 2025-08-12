from app.bot.telegram_service_interface import Telegram_Service_Interface
from app.common.exceptions import InvalidRequestException
from app.core.pydantic.settings import settings


class SendMessageDirectly:
    def __init__(self, bot_service: Telegram_Service_Interface) -> None:
        self.bot_service = bot_service

    async def execute(self, text: str) -> dict:
        if not text:
            raise InvalidRequestException(message="Invalid text")

        #! get channel_id from database or array or channel in later version
        if not settings.channel_id:
            raise InvalidRequestException(message="Channel ID is not set")
        response = await self.bot_service.send_message_to_channel(channel_id=settings.channel_id, text=text)
        return response
 