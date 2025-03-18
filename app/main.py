from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes import router
from .database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔹 Creating database tables if they don’t exist...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables should now exist!")
    yield

app = FastAPI(title="Document Management API", lifespan=lifespan)

app.include_router(router)