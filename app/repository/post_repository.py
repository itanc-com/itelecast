import datetime as date

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

    async def update_scheduled_posts_job_id(self, current_date: date, new_job_id: str, limit: int) -> list[Post]:
        """
        Update the job_id of posts that are scheduled on or before the current_date (up to limit)
        """
        query = select(Post).where(Post.date_scheduled <= current_date).limit(limit)
        result = await self.session.execute(query)
        posts = result.scalars().all()
        
        for post in posts:
            post.job_id = new_job_id
    
        await self.session.commit()  # Single commit for better performance
    
        # Refresh all posts to get updated state
        for post in posts:
            await self.session.refresh(post)
            
        return posts