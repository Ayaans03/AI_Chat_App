from sqlalchemy import ForeignKey,DateTime,func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.user import Base
from typing import List
from app.models.message import Message

# Conversation table act as junction table between user and message table
class Conversation(Base):
    __tablename__ = "Conversation"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    message: Mapped[List["Message"]] = relationship()