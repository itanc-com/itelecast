import datetime as date
from abc import ABC, abstractmethod

from app.models.posts import Post


class PostInterface(ABC):
    @abstractmethod
    async def insert(self, post: Post) -> Post:
        raise NotImplementedError("insert method must be implemented by repository class")

    @abstractmethod
    async def update_scheduled_posts_job_id(self, current_date: date, new_job_id: str, limit: int) -> list[Post]:
        raise NotImplementedError("update_scheduled_posts_job_id method must be implemented by repository class")
