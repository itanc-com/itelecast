from abc import ABC, abstractmethod

from app.models.posts import Post


class PostInterface(ABC):
    @abstractmethod
    async def insert(self, post: Post) -> Post:
        raise NotImplementedError("insert method must be implemented by repository class")

    @abstractmethod
    async def get_all(self, limit: int | None = None) -> list[Post]:
        raise NotImplementedError("get_all method must be implemented by repository class")

