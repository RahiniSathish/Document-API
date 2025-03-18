from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import os
import shutil
from database import SessionLocal
import crud, schemas

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/", response_model=schemas.DocumentResponse)
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

    file_metadata = schemas.DocumentCreate(
        document_name=file.filename,
        file_extension=file.filename.split(".")[-1],
        file_size=os.path.getsize(file_location),
        storage_path=file_location,
        collection_details={"status": "Pending"}
    )

    return crud.create_document(db=db, document=file_metadata)

@router.get("/documents/", response_model=list[schemas.DocumentResponse])
def get_all_documents(db: Session = Depends(get_db)):
    return crud.get_documents(db)