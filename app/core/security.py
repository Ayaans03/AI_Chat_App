from .config import settings
from passlib.hash import sha256_crypt
import jwt
from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from app.schemas.auth import User

JWT_SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.algorithm
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="./login")

def hash_password(password):
    hash = sha256_crypt.hash(password)
    return hash

def verify_password(password, hashed_password):
    verify = sha256_crypt.verify(password, hashed_password)
    return verify

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    
    """
    python -c "import secrets; print(secrets.token_hex(32))" To generate jwt_secret_key for 32 bytes
    python -c "import secrets; print(secrets.token_hex(64))" To generate jwt_secret_key for 64 bytes
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) +  expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_token(token):
    decode = jwt.decode(token, JWT_SECRET_KEY, algorithms=ALGORITHM)
    return decode

def create_referesh_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
            expire = datetime.now(timezone.utc) +  expires_delta 
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire, "token_type":"refresh"})
    encode_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers= {"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = decode_token(token)
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        return email
    except InvalidTokenError:
        raise credentials_exception
