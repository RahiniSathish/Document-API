from sqlalchemy.orm import Session
import models, schemas

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(**document.model_dump())  
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_documents(db: Session):
    return db.query(models.Document).all()
