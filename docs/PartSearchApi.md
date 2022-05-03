# digikey.PartSearchApi

All URIs are relative to *https://api.digikey.com/Search/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyword_search**](PartSearchApi.md#keyword_search) | **POST** /Products/Keyword | KeywordSearch can search for any product in the Digi-Key catalog.

# **keyword_search**
> KeywordSearchResponse keyword_search(authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)

KeywordSearch can search for any product in the Digi-Key catalog.

### Example
```python
from __future__ import print_function
import time
import digikey
from digikey.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = digikey.Configuration()
configuration.api_key['X-DIGIKEY-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
configuration = digikey.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = digikey.PartSearchApi(digikey.ApiClient(configuration))
authorization = 'authorization_example' # str | OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str |  (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)
body = digikey.KeywordSearchRequest() # KeywordSearchRequest |  (optional)

try:
    # KeywordSearch can search for any product in the Digi-Key catalog.
    api_response = api_instance.keyword_search(authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->keyword_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**|  | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 
 **body** | [**KeywordSearchRequest**](KeywordSearchRequest.md)|  | [optional] 

### Return type

[**KeywordSearchResponse**](KeywordSearchResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
