from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentBase(BaseModel):
    document_name: str
    file_extension: str
    file_size: int
    storage_path: str
    collection_details: Optional[dict] = None

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True 
