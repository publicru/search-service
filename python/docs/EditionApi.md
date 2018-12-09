# swagger_client.EditionApi

All URIs are relative to *https://virtserver.swaggerhub.com/sergeytsivin/search-service/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_edition_search_post**](EditionApi.md#api_v2_edition_search_post) | **POST** /api/v2/edition/search | searches editions


# **api_v2_edition_search_post**
> InlineResponse2001 api_v2_edition_search_post(q=q, with_prev_name=with_prev_name, q_geo=q_geo, morph=morph, first_letter=first_letter, theme_ids=theme_ids, publisher_id=publisher_id, type_id=type_id, periodicity_id=periodicity_id, areal_id=areal_id, format_id=format_id, circulation_gte=circulation_gte, circulation_lte=circulation_lte)

searches editions

By passing in the appropriate parameters, you can search for available editions in the system 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EditionApi()
q = 'q_example' # str | search for q in name, alias or url (optional)
with_prev_name = false # bool | when true, search in previous edition name as well (optional) (default to false)
q_geo = 'q_geo_example' # str | search by geo name (optional)
morph = false # bool | when true, apply morphology to search terms (optional) (default to false)
first_letter = 'first_letter_example' # str | filter by first letter of name (optional)
theme_ids = 'theme_ids_example' # str | filter by edition themes, a comma separated list of integers (optional)
publisher_id = 56 # int | filter by publisher_id (optional)
type_id = 56 # int | filter by type_id (optional)
periodicity_id = 56 # int | filter by periodicity_id (optional)
areal_id = 56 # int | filter by areal_id (optional)
format_id = 56 # int | filter by areal_id (optional)
circulation_gte = 56 # int | filter by edition circulation is greater than or equal to (optional)
circulation_lte = 56 # int | filter by edition circulation is less than or equal to (optional)

try:
    # searches editions
    api_response = api_instance.api_v2_edition_search_post(q=q, with_prev_name=with_prev_name, q_geo=q_geo, morph=morph, first_letter=first_letter, theme_ids=theme_ids, publisher_id=publisher_id, type_id=type_id, periodicity_id=periodicity_id, areal_id=areal_id, format_id=format_id, circulation_gte=circulation_gte, circulation_lte=circulation_lte)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditionApi->api_v2_edition_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| search for q in name, alias or url | [optional] 
 **with_prev_name** | **bool**| when true, search in previous edition name as well | [optional] [default to false]
 **q_geo** | **str**| search by geo name | [optional] 
 **morph** | **bool**| when true, apply morphology to search terms | [optional] [default to false]
 **first_letter** | **str**| filter by first letter of name | [optional] 
 **theme_ids** | **str**| filter by edition themes, a comma separated list of integers | [optional] 
 **publisher_id** | **int**| filter by publisher_id | [optional] 
 **type_id** | **int**| filter by type_id | [optional] 
 **periodicity_id** | **int**| filter by periodicity_id | [optional] 
 **areal_id** | **int**| filter by areal_id | [optional] 
 **format_id** | **int**| filter by areal_id | [optional] 
 **circulation_gte** | **int**| filter by edition circulation is greater than or equal to | [optional] 
 **circulation_lte** | **int**| filter by edition circulation is less than or equal to | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

