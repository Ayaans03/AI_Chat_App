
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Importing App componets

from app.main import app
from app.models.user import Base, User
from app.core.database import _engine_connect
from app.core.security import create_access_token

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.close()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session):

    def _get_db_override():
        try:
            yield db_session
        except:
            pass

    app.dependency_overrides[_engine_connect] = _get_db_override
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def test_user(db_session):
    user = User(
        email = "test@example.com",
        hased_password = "mocked_hased_password"
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture(scope="function")
def auth_client(client,test_user):
    token = create_access_token(data={"sub": test_user.email, "user_id": test_user.id})

    client.headers.update({"Authorization": f"Bearer {token}"})
    return client