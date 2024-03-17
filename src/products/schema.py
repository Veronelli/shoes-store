"""
Define the GraphQL schema for our API
"""

from typing import Optional
from graphene import Field, ObjectType, Int, ResolveInfo, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import get_db
from src.products.db_model import ProductDB


class Product(SQLAlchemyObjectType):
    """
    A class represents Product schema
    """

    class Meta:
        """
        Meta class to config schema
        """

        model = ProductDB
        interface = ObjectType


class QueryProduct(ObjectType):
    """
    A class represents query for products
    """

    products = Field(lambda: list[Product], limit=Int())

    def resolve_product(
        self, info: ResolveInfo, limit: Optional[int] = None
    ) -> list[Product]:
        """
        Resolve list product
        Args:
        -   self:(Self)
        -   info:(ResolveInfo): provides contextual information
            about the current GraphQL resolution process
        -   limit:(Optional[int]) limit list of products

        Returns:
        -   (List[Product]): list of products
        """
        query = Product.get_query(info)
        if limit:
            return query.limit(limit).all()
        return query.all()


class CreateProduct(ObjectType):
    product = Field(lambda: Product)

    class Arguments:
        """
        Argument class to fill data
        Attributes:
        -   name:(String*) name of product
        -   description:(String*) description of product
        -   specs:(Integer) spec id of product
        -   categories:(List[Integer]) categories id of product
        -   tags:(list[Integer]) tags id of product
        TODO:
        -   Create integration test for this cases
        -   Complete model after create their integration test.
        """

        name = String(require=True)
        description = String()

    def mutate(self, info: ResolveInfo, name: str, description: str) -> Product:
        """
        Create new product
        Args:
        -   info:(ResolveInfo) provides contextual information
        -   name:(str) name of product
        -   description:(str) description of product
        Returns:
        -   (Product): new product created

        TODO:
        -   fill with all product attributes
        """
        db = get_db()
        product = ProductDB(name=name, description=description)
        db.add(product)
        db.commit()
        db.refresh()
        return CreateProduct(product=product)
