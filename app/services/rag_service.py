from fastapi import HTTPException
from app.models.document import Document_Chunks
from sqlalchemy import select
from app.core.database import _engine_connect
from app.core.google_genai import client
from google.genai import types

def get_top_3_documents_chuncks(embeddings: list[float]):
    try:
        with _engine_connect() as Connection:
            result = Connection.execute(select(Document_Chunks.content).order_by(Document_Chunks.embedding.cosine_distance(embeddings)).limit(3))
            return result
    except HTTPException as e:
        raise e

def embed_uaer_prompt_to_get_content(text: str):
    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents= text,
            config= types.EmbedContentConfig(output_dimensionality=1536)
        )
        for embeddings in result.embeddings:
            embed = embeddings.values

        output = get_top_3_documents_chuncks(embed)
        cursorResult_to_list = [dict(row) for row in output.mappings()]

        final_result = "".join(data["content"] for data in cursorResult_to_list)
        return final_result

    except HTTPException as e:
        raise e