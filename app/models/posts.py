import enum

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, Integer, String, Text, func

from app.db_manager.base import Base


class StatusType(enum.Enum):
    PENDING = "pending"       # Message is pending, not yet processed
    QUEUED = "queued"        # Message is in queue and get Job_Id, and will be processed soon
    SENT = "sent"             # Message sent successfully
    FAILED = "failed"         # Sending failed
    
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(BigInteger, nullable=False)  # Telegram channel ID
    content = Column(Text, nullable=False)
    media_url = Column(Text, nullable=True)  # if sending photo/video
    media_type = Column(String(20), nullable=True)  # 'photo', 'video', etc.
    formatting = Column(String(20), nullable=True)  # 'MarkdownV2', 'HTML'
    disable_web_page_preview = Column(Boolean, default=False)
    disable_notification = Column(Boolean, default=False)
    date_created = Column(DateTime, default=func.now(), nullable=False)
    date_scheduled = Column(DateTime, default=func.now(), nullable=False)
    job_id = Column(BigInteger, default=None, nullable=True)
    status = Column(Enum(StatusType), default=StatusType.PENDING, nullable=False) # 'pending', 'processing', 'sent', 'failed'
    #telegram_message_id = Column(BigInteger, nullable=True)
    #error_message = Column(Text, nullable=True)
    
    
    
    

