from sqlalchemy import ForeignKey, func, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.models.user import Base

class Message(Base):
    __tablename__ = "Message"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    role : Mapped[str] = mapped_column(String(30))
    content : Mapped[str] = mapped_column()
    created_at : Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    conversation_id : Mapped[int] = mapped_column(ForeignKey("Conversation.id"))