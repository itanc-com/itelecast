from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.posts import Post
from app.repository.post_interface import PostInterface


class PostRepository(PostInterface):

    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def insert(self, post: Post) -> Post:
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        return post
    
 
    async def get_all(self, limit: int | None = None) -> list[Post]:
        query = select(Post)
        if limit is not None:
            query = query.limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()
