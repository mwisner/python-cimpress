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
    def it_creates(self):
        data = [
            'http://loremflickr.com/320/240'
        ]

        response = self.client.v2_documents.create(data=data,
                                                   sku='VIP-45694',
                                                   scale='stretchToFit',
                                                   method='urls')

        from pprint import pprint
        pprint(response)

        #assert len(response)

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
        from pprint import pprint
        pprint(product)
        assert product.get('Prices')

    @istest
    def it_gets_product_surfaces(self):
        products = self.client.v1_products.list_all()
        assert len(products)

        product = self.client.v1_products.get_product_surfaces(products[0].get('Sku'))

        assert product.get('Surfaces')


