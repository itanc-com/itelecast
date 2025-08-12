from app.common.exceptions import InvalidRequestException
from app.core.pydantic.settings import settings
from app.models.posts import Post
from app.repository.post_repository import PostRepository


class SaveMessageToQueue:
    def __init__(self, post_repository: PostRepository) -> None:
        self.post_repository = post_repository

    async def execute(self, text: str) -> dict:
        if not text:
            raise InvalidRequestException(message="Invalid text")

        #! get channel_id from database or array or channel in later version
        if not settings.channel_id:
            raise InvalidRequestException(message="Channel ID is not set")

        new_post = Post()
        new_post.content = text
        new_post.channel_id = settings.channel_id  # Assuming channel_id is part of Post model
        
        response = await self.post_repository.insert(new_post)
        return response