from app.models.user import User
from fastapi.testclient import TestClient

def test_register_user(client, db_session):
    test_data = {"email":"demo@gmail.com", "password":"test@1234"}
    response = client.post("/auth/register", json = test_data)
    assert response.status_code == 200
    assert response.json() == {"Message": "User is been registered"}

    db_session.expire_all()
    user_in_db = db_session.query(User).filter_by(email = "demo@gmail.com").first()
    assert user_in_db is not None