from .config import settings

JWT_SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.algorithm

# python -c "import secrets; print(secrets.token_hex(32))" To generate jwt_secret_key for 32 bytes
# python -c "import secrets; print(secrets.token_hex(64))" To generate jwt_secret_key for 64 bytes