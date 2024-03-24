"""
Root configuration
"""

from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from fastapi import FastAPI
from src.products.schema import (
    QueryProduct,
    CreateProduct,
    DeleteProduct,
    UpdateProduct,
)
from src.database import get_db
from starlette_graphene3 import GraphQLApp


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
app.add_route(
    "/product",
    GraphQLApp(
        schema=QueryProduct, mutations=[UpdateProduct, CreateProduct, DeleteProduct]
    ),
)


@app.get("/")
async def root():
    """
    Root of endpoints, to know the health of the project

    Returns:
        dict: message attribute with 'Hello World'
    """
    return {"message": "Hello World"}
