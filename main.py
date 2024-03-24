"""
Root configuration
"""

from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from fastapi import FastAPI
from src.database import get_db


@asynccontextmanager  # type: ignore
async def lifespan(app: FastAPI) -> AsyncGenerator[FastAPI, Any]:
    """
    Definition of lifestan to create a connection to the server
    Args:
    -   app:(FastAPI) instance of fastapi
    """
    await get_db.connect()  # type: ignore
    yield
    await get_db.disconnect()  # type: ignore


app = FastAPI()


@app.get("/")
async def root():
    """
    Root of endpoints, to know the health of the project

    Returns:
        dict: message attribute with 'Hello World'
    """
    return {"message": "Hello World"}
