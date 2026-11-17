from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key : str
    postgres_connection_string : str
    jwt_secret_key : str
    algorithm : str
    access_token_expire_minutes : int
    refresh_token_expire_hours: int
    redis_connection_string: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()