"""
Modeling schema to interact to DB

TODO:
-   continue implementing GraphQL to understand
"""

from dataclasses import dataclass
from typing import List, Optional
from strawberry import Schema, type, field
from strawberry.asgi import GraphQL


@dataclass
@type
class Product:
    """
    A class represents a product modeling for data base

    Attributes:
    -   id:(Integer) id of product
    -   name:(String*) name of product
    -   description:(String*) description of product
    -   spec:(SpecDB) specs of product
    -   category:(CategoryDB) category of product
    -   tags: (list[TagDB]) tag list of product
    -   visibility:(bool) allow to show to customers
    """

    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    visibility: Optional[bool] = None
    spec: Optional[int] = None
    tags: Optional[int] = None
    cateogry: Optional[int] = None


@type
class Query:
    """
    A class to make a query
    """

    @field
    def products(self) -> List[Product]:
        """
        Field of products list

        Returns:
        -   List[Product]: List of products
        """
        product = Product(
            id=1, name="Product 1", description="Descrition about product 2"
        )

        return [product]


schema = Schema(query=Query)
graphql_app = GraphQL(schema)
