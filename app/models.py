from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, JSON
from sqlalchemy.sql import func
from database import Base  # Ensure the correct import

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    document_name = Column(String(255), nullable=False)
    file_extension = Column(String(10), nullable=False)
    file_size = Column(Integer, nullable=False)
    storage_path = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())
    collection_details = Column(JSON, nullable=True)