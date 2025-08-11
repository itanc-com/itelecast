from httpx import AsyncClient

from app.bot.telegram_service_interface import Telegram_Service_Interface


class TelegramService(Telegram_Service_Interface):
    def __init__(self, bot_token: str, client: AsyncClient):
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.client = client
        print("HTTPX Client:", self.client)

    async def send_message_to_channel(self, channel_id: str, text: str) -> dict:
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": channel_id,
            "text": text
        }
        response = await self.client.post(url, data=payload)
        response.raise_for_status() # Raises HTTPError
        return await response.json()
    
    async def get_me(self) -> dict:
        url = f"{self.base_url}/getMe"
        response = await self.client.get(url)
        response.raise_for_status() # Raises HTTPError
        return await response.json()
    
