"""
Define the GraphQL schema for our API
"""

from graphene import ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.products.db_model import ProductDB


class Product(SQLAlchemyObjectType):
    """
    A class represents Product schema
    """

    class Meta:
        model = ProductDB
        interface = ObjectType


class QueryProduct(ObjectType):
    """
    A class represents query for products
    """

    ...
