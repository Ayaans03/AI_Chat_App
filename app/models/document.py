from sqlalchemy import DateTime, func
from pgvector.sqlalchemy import Vector
from app.models.user import Base
from sqlalchemy.orm import Mapped, mapped_column
import numpy as np

class Document_Chunks(Base):
    __tablename__ = "Document_Chunks"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content : Mapped[str] = mapped_column()
    embedding : Mapped[np.array] = mapped_column(Vector(1536))
    created_at : Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())
