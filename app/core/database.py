# Added the database connection engine so that it can we imported
from sqlalchemy import create_engine
from app.models.user import Base
from .config import settings

engine = create_engine(settings.postgres_connection_string)
Base.metadata.create_all(bind=engine)
print("Database initialized")