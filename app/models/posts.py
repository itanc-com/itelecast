from sqlalchemy import Column, DateTime, Integer, Text, func

from app.db.base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    media_url = Column(Text, nullable=True)
    date_created = Column(DateTime, default=func.now(), nullable=False)
    date_scheduled = Column(DateTime, nullable=True)
    date_published = Column(DateTime, nullable=True)
    telegram_message_id = Column(Text, nullable=True)
    formatting = Column(Integer, nullable=True)  # Use FormattingType enum values