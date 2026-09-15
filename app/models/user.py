from sqlalchemy.orm import relationship,DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from typing import List
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(30))
    hased_password: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    conversation: Mapped[List["Conversation"]] = relationship()