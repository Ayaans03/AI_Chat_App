from .config import settings
from passlib.hash import sha256_crypt
import jwt
from datetime import datetime, timezone, timedelta

JWT_SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.algorithm

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
