import os
from dotenv import load_dotenv
from google.genai import Client, errors
from fastapi import HTTPException
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = Client(api_key=GEMINI_API_KEY)

def interaction(data):
    try:
        interact = client.interactions.create(
            model="gemini-2.5-flash",
            input=data
        )
        return interact
    except [errors.ClientError, errors.ServerError] as e:
        raise HTTPException(status_code=[i for i in range(400,600)])
    