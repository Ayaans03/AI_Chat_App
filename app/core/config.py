from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key : str
    postgres_connection_string : str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()