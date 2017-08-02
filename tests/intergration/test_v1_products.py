import os
import unittest

from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest

from cimpress.client import Client


class ProductsTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(
            os.environ.get('CIMPRESS_TOKEN'), 'sandbox')

    @istest
    def it_lists_products(self):
        response = self.client.v1_products.list_products()

        assert len(response)
