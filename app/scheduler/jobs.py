from app.db_manager.session import sessionmanager
from app.repository.post_repository import PostRepository
from app.utils.datetime import generate_time_id, get_utc_now


async def send_scheduled_messages():
    """
    This function retrieves posts that are scheduled to be sent and
    updates their job_id.
    """
    job_id = generate_time_id()
    async with sessionmanager.session() as session:
        try:
            post_repository = PostRepository(session)

            # Get posts that need to be sent
            current_date = get_utc_now()
            posts = await post_repository.update_scheduled_posts_job_id(
                current_date=current_date, 
                new_job_id=job_id, 
                limit=100
            )
            
            # Here you would implement your message sending logic
            print(f"Processing {len(posts)} scheduled messages with job_id: {job_id}")
            
            # Example: Send each post (implement your actual sending logic)
            for post in posts:
                # Your message sending logic here
                print(f"Sending post: {post.id}")
                
        except Exception as e:
            print(f"Error in send_scheduled_messages_async: {e}")
            # Log the error properly in production
            raise



async def SampleJob():
    print("Sample job executed...") 