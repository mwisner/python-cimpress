import os
import unittest

from nose.tools import istest

from cimpress.authentication import get_api_token


class ProductsTest(unittest.TestCase):

    @istest
    def is_token_legit(self):
        client_id = os.environ.get('CIMPRESS_CLIENT_ID')
        username = os.environ.get('CIMPRESS_USERNAME')
        password = os.environ.get('CIMPRESS_PASSWORD')

        token = get_api_token(client_id, username, password)
        assert token
