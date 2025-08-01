from abc import ABC, abstractmethod


class Telegram_Service_Interface(ABC):
    @abstractmethod
    async def send_message_to_channel(self, channel_id: str, text: str) -> dict:
        raise NotImplementedError("send_message_to_channel method must be implemented by subclass")

    @abstractmethod
    async def get_me(self) -> dict:
        raise NotImplementedError("get_me method must be implemented by subclass")