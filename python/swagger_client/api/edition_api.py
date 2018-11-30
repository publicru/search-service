# coding: utf-8

"""
    Public Search API

    Searches documens and editions  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EditionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_edition_search_post(self, **kwargs):  # noqa: E501
        """searches editions  # noqa: E501

        By passing in the appropriate parameters, you can search for available editions in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v2_edition_search_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param str q: search for q in name, alias or url
        :param bool with_prev_name: when true, search in previous edition name as well
        :param str q_geo: search by geo name
        :param bool morph: when true, apply morphology to search terms
        :param str first_letter: filter by first letter of name
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.api_v2_edition_search_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_edition_search_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v2_edition_search_post_with_http_info(self, **kwargs):  # noqa: E501
        """searches editions  # noqa: E501

        By passing in the appropriate parameters, you can search for available editions in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.api_v2_edition_search_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str q: search for q in name, alias or url
        :param bool with_prev_name: when true, search in previous edition name as well
        :param str q_geo: search by geo name
        :param bool morph: when true, apply morphology to search terms
        :param str first_letter: filter by first letter of name
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'with_prev_name', 'q_geo', 'morph', 'first_letter']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_edition_search_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'with_prev_name' in params:
            query_params.append(('with_prev_name', params['with_prev_name']))  # noqa: E501
        if 'q_geo' in params:
            query_params.append(('q_geo', params['q_geo']))  # noqa: E501
        if 'morph' in params:
            query_params.append(('morph', params['morph']))  # noqa: E501
        if 'first_letter' in params:
            query_params.append(('first_letter', params['first_letter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/edition/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
