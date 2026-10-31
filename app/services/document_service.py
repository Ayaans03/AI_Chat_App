from google.genai import types
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.document import Document_Chunks
from app.core.database import engine
from app.core.google_genai import client

def _chunk_and_overlap_text(text: str):
    chunk_size = 500
    overlap = 50
    size = chunk_size - overlap

    chunks = []

    for i in range(0, len(text), size):
        chunks.append(text[i:i+chunk_size])

    return chunks

def chunk_embedding_insert(text: str):
    chunks = _chunk_and_overlap_text(text)
    if not chunks:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Text document cannot be empty")

    try:
        document_db = []
        session = Session(engine)
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=chunks,
            config= types.EmbedContentConfig(output_dimensionality=1536)
        )

        embed = [embedding.values for embedding in result.embeddings]

        for chunk_text, embed_value in list(zip(chunks, embed)):
            result = Document_Chunks(
                content = chunk_text,
                embedding = embed_value
            )

            document_db.append(result)
        session.add_all(document_db)
        session.commit()
    except HTTPException as e:
        raise e