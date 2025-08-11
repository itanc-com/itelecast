from app.bot.telegram_service_interface import Telegram_Service_Interface


class GetBotInfo:
    def __init__(self, bot_service: Telegram_Service_Interface) -> None:
        self.bot_service = bot_service

    async def execute(self) -> dict:
        return await self.bot_service.get_me()
 