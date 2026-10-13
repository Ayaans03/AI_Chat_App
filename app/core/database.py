# Added the database connection engine so that it can we imported
from sqlalchemy import create_engine
from app.models.user import Base
from .config import settings
from contextlib import contextmanager # allows to allocate and release resources

engine = create_engine(settings.postgres_connection_string)
Base.metadata.create_all(bind=engine)
print("Database initialized")

# helper function to open connect
@contextmanager
def _engine_connect():
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()