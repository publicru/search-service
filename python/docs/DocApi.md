# swagger_client.DocApi

All URIs are relative to *https://virtserver.swaggerhub.com/sergeytsivin/search-service/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_doc_doc_id_get**](DocApi.md#api_v2_doc_doc_id_get) | **GET** /api/v2/doc/{docId} | returns a document
[**search_documents**](DocApi.md#search_documents) | **POST** /api/v2/doc/search | searches documents


# **api_v2_doc_doc_id_get**
> Doc api_v2_doc_doc_id_get(doc_id, q_body=q_body)

returns a document

Returns document specified by docId, optionally with highlighted hits 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocApi()
doc_id = 789 # int | ID of document to return
q_body = 'q_body_example' # str | If specified, it will be used for highlighting hits in the body. If missing, no highlighting will be done. (optional)

try:
    # returns a document
    api_response = api_instance.api_v2_doc_doc_id_get(doc_id, q_body=q_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->api_v2_doc_doc_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **int**| ID of document to return | 
 **q_body** | **str**| If specified, it will be used for highlighting hits in the body. If missing, no highlighting will be done. | [optional] 

### Return type

[**Doc**](Doc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_documents**
> InlineResponse200 search_documents(es_ids=es_ids, author_ids=author_ids, doc_ids=doc_ids, gen_ids=gen_ids, pd_from=pd_from, pd_to=pd_to, ld_from=ld_from, ld_to=ld_to, _from=_from, size=size, doc_type_mask=doc_type_mask, morph=morph, q_body=q_body, q_title=q_title, q_author=q_author, q_release=q_release, q_page=q_page, q_illustration=q_illustration, with_hits=with_hits, order_by=order_by)

searches documents

By passing in the appropriate options, you can search for available documents in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocApi()
es_ids = 'es_ids_example' # str | filter by editions, a comma separated list of edition IDs (optional)
author_ids = 'author_ids_example' # str | filter by authors, a comma separated list of author IDs (optional)
doc_ids = 'doc_ids_example' # str | filter by documents, a comma separated list of document IDs (optional)
gen_ids = 'gen_ids_example' # str | filter by semantic genre, a comma separated list of genre IDs (optional)
pd_from = '2013-10-20' # date | filter by pub_date, lower bound (optional)
pd_to = '2013-10-20' # date | filter by pub_date, upper bound (optional)
ld_from = '2013-10-20' # date | filter by load_date, lower bound (optional)
ld_to = '2013-10-20' # date | filter by load_date, upper bound (optional)
_from = 0 # int | offset from the beginning of document set (optional) (default to 0)
size = 50 # int | number of documents to return (optional) (default to 50)
doc_type_mask = 1 # int | filter by document type (optional) (default to 1)
morph = 1 # int | use russian morphology (optional) (default to 1)
q_body = 'q_body_example' # str | query body (optional)
q_title = 'q_title_example' # str | query title (optional)
q_author = 'q_author_example' # str | query author (optional)
q_release = 'q_release_example' # str | query release (optional)
q_page = 'q_page_example' # str | query page (optional)
q_illustration = 'q_illustration_example' # str | query illustration (optional)
with_hits = true # bool | return snippets with hits (optional) (default to true)
order_by = 'order_by_example' # str | order results by, a comma separated list of fields (optional)

try:
    # searches documents
    api_response = api_instance.search_documents(es_ids=es_ids, author_ids=author_ids, doc_ids=doc_ids, gen_ids=gen_ids, pd_from=pd_from, pd_to=pd_to, ld_from=ld_from, ld_to=ld_to, _from=_from, size=size, doc_type_mask=doc_type_mask, morph=morph, q_body=q_body, q_title=q_title, q_author=q_author, q_release=q_release, q_page=q_page, q_illustration=q_illustration, with_hits=with_hits, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->search_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **es_ids** | **str**| filter by editions, a comma separated list of edition IDs | [optional] 
 **author_ids** | **str**| filter by authors, a comma separated list of author IDs | [optional] 
 **doc_ids** | **str**| filter by documents, a comma separated list of document IDs | [optional] 
 **gen_ids** | **str**| filter by semantic genre, a comma separated list of genre IDs | [optional] 
 **pd_from** | **date**| filter by pub_date, lower bound | [optional] 
 **pd_to** | **date**| filter by pub_date, upper bound | [optional] 
 **ld_from** | **date**| filter by load_date, lower bound | [optional] 
 **ld_to** | **date**| filter by load_date, upper bound | [optional] 
 **_from** | **int**| offset from the beginning of document set | [optional] [default to 0]
 **size** | **int**| number of documents to return | [optional] [default to 50]
 **doc_type_mask** | **int**| filter by document type | [optional] [default to 1]
 **morph** | **int**| use russian morphology | [optional] [default to 1]
 **q_body** | **str**| query body | [optional] 
 **q_title** | **str**| query title | [optional] 
 **q_author** | **str**| query author | [optional] 
 **q_release** | **str**| query release | [optional] 
 **q_page** | **str**| query page | [optional] 
 **q_illustration** | **str**| query illustration | [optional] 
 **with_hits** | **bool**| return snippets with hits | [optional] [default to true]
 **order_by** | **str**| order results by, a comma separated list of fields | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

