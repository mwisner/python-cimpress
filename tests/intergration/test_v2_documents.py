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

        assert 'DocumentReferenceUrl' in response
