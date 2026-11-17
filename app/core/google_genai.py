from google.genai import Client
from app.core.config import settings

client = Client(api_key=settings.gemini_api_key)