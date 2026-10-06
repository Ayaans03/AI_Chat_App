from .config import settings
from passlib.hash import sha256_crypt
import jwt

JWT_SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.algorithm

def hash_password(password):
    hash = sha256_crypt.hash(password)
    return hash

def jwt_encoding(payload):
    
    """
    python -c "import secrets; print(secrets.token_hex(32))" To generate jwt_secret_key for 32 bytes
    python -c "import secrets; print(secrets.token_hex(64))" To generate jwt_secret_key for 64 bytes
    """

    encode = jwt.encode({"some": payload}, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encode

def jwt_decode(encoded):
    decode = jwt.decode(encoded, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return decode

