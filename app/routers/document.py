from fastapi import APIRouter
from app.services.document_service import chunk_embedding_insert
from fastapi import HTTPException
from app.schemas.document import Document

router = APIRouter(
    prefix="",
    tags= ["document"]
)

@router.post("/document")
def chunk_embbed_store(data: Document):
    try:
        request = chunk_embedding_insert(data.text)
        return request
    except HTTPException as e:
        raise e