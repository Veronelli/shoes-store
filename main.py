"""
Root configuration
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Root of endpoints, to know the health of the project

    Returns:
        dict: message attribute with 'Hello World'
    """
    return {"message": "Hello World"}
