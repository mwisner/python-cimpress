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
        response = self.client.v1_products.list_products()
        assert len(response)
