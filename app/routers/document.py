from fastapi import APIRouter, BackgroundTasks
from app.services.document_service import chunk_embedding_insert
from fastapi import HTTPException
from app.schemas.document import Document

router = APIRouter(
    prefix="",
    tags= ["document"]
)

@router.post("/document")
def chunk_embbed_store(data: Document, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(chunk_embedding_insert,data.text)
        return {"Message": "Chunking, Emdedding and insertion to DB process has started.."}
    except HTTPException as e:
        raise e