"""
Declare Model for Data Base
"""

from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship

BaseDB = declarative_base()


class SpecDB(BaseDB):  # type: ignore
    """
    A class represents a spec for data base

    Attributes:
    -   id:(Integer) id of Spec
    -   name:(String) name of Spec
    """

    __tablename__ = "Specs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id"))


class CategoryDB(BaseDB):  # type: ignore
    """
    A class represents a Category for data base
    Attribute:
    -   id:(Integer) id of Category
    -   name:(String) name of Category
    """

    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category.id"))


class TagDB(BaseDB):  # type: ignore
    """
    A class represents a Tag for data base
    Attribute:
    -   id:(Integer) id of Tag
    -   name:(String) name of Tag
    """

    __tablename__ = "Tags"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tag_id = Column(Integer, ForeignKey("tag.id"))


class ProductDB(BaseDB):  # type: ignore
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

    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(
        String,
        index=True,
    )
    visibility = Column(Boolean, default=False)
    specs: Mapped[Optional[list[SpecDB]]] = relationship(backref="spec")
    category: Mapped[Optional[CategoryDB]] = relationship(backref="category")
    tags: Mapped[Optional[list[TagDB]]] = relationship(backref="tag")
