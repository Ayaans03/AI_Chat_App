from .config import settings
import redis
from fastapi import HTTPException, status, Depends
from app.core.security import get_current_user

REDIS_CONNECTION_STRING = settings.redis_connection_string
MAX_REQUEST = 20
TIME_WINDOW = 60*60 # i hour

redis_db = redis.from_url(REDIS_CONNECTION_STRING)

def rate_limiting(Token: tuple = Depends(get_current_user)):
    key = f"rate_limit:{Token[1]}"
    count = redis_db.incr(key)
    if count == 1:
        redis_db.expire(key,TIME_WINDOW)
    if count > MAX_REQUEST:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail= "Total Request has been exceed, Please try again later")