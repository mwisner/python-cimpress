import os
import unittest

from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest
from ..utils import get_client_with_token


class ProductsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = get_client_with_token()

    @istest
    def it_lists_products(self):
        response = self.client.v1_products.list_all()
        assert len(response)

    @istest
    def it_lists_product_prices(self):
        response = self.client.v1_products.list_all_prices()
        assert len(response)

    @istest
    def it_gets_product(self):
        products = self.client.v1_products.list_all()
        assert len(products)
        product = products[0]
        product = self.client.v1_products.get_product(product.get('Sku'))
        assert product.get('Prices')

    @istest
    def it_gets_product_surfaces(self):
        products = self.client.v1_products.list_all()
        assert len(products)

        product = self.client.v1_products.get_product_surfaces(products[0].get('Sku'))

        assert product.get('Surfaces')


