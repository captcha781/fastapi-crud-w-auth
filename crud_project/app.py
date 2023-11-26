from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from crud_project.config.index import config 
from crud_project.models.User import User


DESCRIPTION = """
    This API server is built for 
    CRUD operations with JWT 
    Authentication. So Please use with
    your own care, do not copy paste.
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.db = AsyncIOMotorClient(config.mongo_uri).fastapi_testing
    await init_beanie(app.db, document_models=[User])
    print("Server running successfully...")
    yield
    print("Shuting down server...")

app = FastAPI(
    title="CRUD Template",
    description=DESCRIPTION,
    lifespan=lifespan,
    contact={
        "name": "captcha781 ( Bhuvaneshwaran )",
        "email": "bhuvanesh19112001@gmail.com",
        "url": "https://github.com/captcha781"
    },
)
