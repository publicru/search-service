# coding: utf-8

"""
    Внутренний API для поиска по базе СМИ

    Позволяет искать документы и издания с использованием языка  запроосов public.ru. Не требует авторизации, поэтому должен быть доступен только из внутренней сети.   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.edition_api import EditionApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEditionApi(unittest.TestCase):
    """EditionApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.edition_api.EditionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_edition_edition_id_get(self):
        """Test case for edition_edition_id_get

        returns edition  # noqa: E501
        """
        pass

    def test_edition_prefix_search_post(self):
        """Test case for edition_prefix_search_post

        searches editions by prefix  # noqa: E501
        """
        pass

    def test_edition_search_post(self):
        """Test case for edition_search_post

        searches editions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
