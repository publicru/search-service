# coding: utf-8

"""
    Внутренний API для поиска по базе СМИ

    Позволяет искать документы и издания с использованием языка  запроосов public.ru. Не требует авторизации, поэтому должен быть доступен только из внутренней сети.   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DocApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def doc_doc_id_get(self, doc_id, **kwargs):  # noqa: E501
        """returns a document  # noqa: E501

        Returns document specified by docId, optionally with highlighted hits   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.doc_doc_id_get(doc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int doc_id: ID of document to return (required)
        :param str q_body: If specified, it will be used for highlighting hits in the body. If missing, no highlighting will be done.
        :return: Doc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.doc_doc_id_get_with_http_info(doc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.doc_doc_id_get_with_http_info(doc_id, **kwargs)  # noqa: E501
            return data

    def doc_doc_id_get_with_http_info(self, doc_id, **kwargs):  # noqa: E501
        """returns a document  # noqa: E501

        Returns document specified by docId, optionally with highlighted hits   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.doc_doc_id_get_with_http_info(doc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int doc_id: ID of document to return (required)
        :param str q_body: If specified, it will be used for highlighting hits in the body. If missing, no highlighting will be done.
        :return: Doc
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doc_id', 'q_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method doc_doc_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doc_id' is set
        if ('doc_id' not in params or
                params['doc_id'] is None):
            raise ValueError("Missing the required parameter `doc_id` when calling `doc_doc_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doc_id' in params:
            path_params['docId'] = params['doc_id']  # noqa: E501

        query_params = []
        if 'q_body' in params:
            query_params.append(('q_body', params['q_body']))  # noqa: E501

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
            '/doc/{docId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Doc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_documents(self, **kwargs):  # noqa: E501
        """searches documents  # noqa: E501

        By passing in the appropriate options, you can search for available documents in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_documents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str es_ids: filter by editions series, a comma separated list of edition series IDs
        :param str e_ids: filter by editions, a comma separated list of edition IDs
        :param str author_ids: filter by authors, a comma separated list of author IDs
        :param str doc_ids: filter by documents, a comma separated list of document IDs
        :param str gen_ids: filter by semantic genre, a comma separated list of genre IDs
        :param date pd_from: filter by pub_date, lower bound
        :param date pd_to: filter by pub_date, upper bound
        :param date ld_from: filter by load_date, lower bound
        :param date ld_to: filter by load_date, upper bound
        :param int _from: offset from the beginning of document set
        :param int size: number of documents to return
        :param int doc_type_mask: filter by document type
        :param int morph: use russian morphology
        :param str q_body: query body
        :param str q_title: query title
        :param str q_author: query author
        :param str q_release: query release
        :param str q_page: query page
        :param str q_illustration: query illustration
        :param bool with_hits: return snippets with hits
        :param str order_by: order results by, a comma separated list of fields
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_documents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_documents_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_documents_with_http_info(self, **kwargs):  # noqa: E501
        """searches documents  # noqa: E501

        By passing in the appropriate options, you can search for available documents in the system   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_documents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str es_ids: filter by editions series, a comma separated list of edition series IDs
        :param str e_ids: filter by editions, a comma separated list of edition IDs
        :param str author_ids: filter by authors, a comma separated list of author IDs
        :param str doc_ids: filter by documents, a comma separated list of document IDs
        :param str gen_ids: filter by semantic genre, a comma separated list of genre IDs
        :param date pd_from: filter by pub_date, lower bound
        :param date pd_to: filter by pub_date, upper bound
        :param date ld_from: filter by load_date, lower bound
        :param date ld_to: filter by load_date, upper bound
        :param int _from: offset from the beginning of document set
        :param int size: number of documents to return
        :param int doc_type_mask: filter by document type
        :param int morph: use russian morphology
        :param str q_body: query body
        :param str q_title: query title
        :param str q_author: query author
        :param str q_release: query release
        :param str q_page: query page
        :param str q_illustration: query illustration
        :param bool with_hits: return snippets with hits
        :param str order_by: order results by, a comma separated list of fields
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['es_ids', 'e_ids', 'author_ids', 'doc_ids', 'gen_ids', 'pd_from', 'pd_to', 'ld_from', 'ld_to', '_from', 'size', 'doc_type_mask', 'morph', 'q_body', 'q_title', 'q_author', 'q_release', 'q_page', 'q_illustration', 'with_hits', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_documents" % key
                )
            params[key] = val
        del params['kwargs']

        if '_from' in params and params['_from'] > 3000:  # noqa: E501
            raise ValueError("Invalid value for parameter `_from` when calling `search_documents`, must be a value less than or equal to `3000`")  # noqa: E501
        if '_from' in params and params['_from'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `_from` when calling `search_documents`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'size' in params and params['size'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `size` when calling `search_documents`, must be a value less than or equal to `50`")  # noqa: E501
        if 'size' in params and params['size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `size` when calling `search_documents`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'es_ids' in params:
            query_params.append(('es_ids', params['es_ids']))  # noqa: E501
        if 'e_ids' in params:
            query_params.append(('e_ids', params['e_ids']))  # noqa: E501
        if 'author_ids' in params:
            query_params.append(('author_ids', params['author_ids']))  # noqa: E501
        if 'doc_ids' in params:
            query_params.append(('doc_ids', params['doc_ids']))  # noqa: E501
        if 'gen_ids' in params:
            query_params.append(('gen_ids', params['gen_ids']))  # noqa: E501
        if 'pd_from' in params:
            query_params.append(('pd_from', params['pd_from']))  # noqa: E501
        if 'pd_to' in params:
            query_params.append(('pd_to', params['pd_to']))  # noqa: E501
        if 'ld_from' in params:
            query_params.append(('ld_from', params['ld_from']))  # noqa: E501
        if 'ld_to' in params:
            query_params.append(('ld_to', params['ld_to']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'doc_type_mask' in params:
            query_params.append(('doc_type_mask', params['doc_type_mask']))  # noqa: E501
        if 'morph' in params:
            query_params.append(('morph', params['morph']))  # noqa: E501
        if 'q_body' in params:
            query_params.append(('q_body', params['q_body']))  # noqa: E501
        if 'q_title' in params:
            query_params.append(('q_title', params['q_title']))  # noqa: E501
        if 'q_author' in params:
            query_params.append(('q_author', params['q_author']))  # noqa: E501
        if 'q_release' in params:
            query_params.append(('q_release', params['q_release']))  # noqa: E501
        if 'q_page' in params:
            query_params.append(('q_page', params['q_page']))  # noqa: E501
        if 'q_illustration' in params:
            query_params.append(('q_illustration', params['q_illustration']))  # noqa: E501
        if 'with_hits' in params:
            query_params.append(('with_hits', params['with_hits']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

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
            '/doc/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
