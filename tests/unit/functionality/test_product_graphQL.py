"""
Test integration using GraphQL in product module
"""

import pytest
from pytest_mock import MockerFixture
from src.products.repository import get_product_list


@pytest.mark.asyncio
async def test_get_products_from_graphql(mocker: MockerFixture):
    """
    Test obtain a list of product, integrated with graphQL

    Fixtures:
    -   mocker: object that allow to modify the normal behavior
    """
    products = await get_product_list()

    assert len(products) > 0
