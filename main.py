"""
Root configuration
"""

from fastapi import FastAPI
from src.products.schema import graphql_app

app = FastAPI()

app.add_route("/graphql", graphql_app)


@app.get("/")
async def root():
    """
    Root of endpoints, to know the health of the project

    Returns:
        dict: message attribute with 'Hello World'
    """
    return {"message": "Hello World"}
