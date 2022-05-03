# digikey.PartSearchApi

All URIs are relative to *https://api.digikey.com/Search/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories**](PartSearchApi.md#categories) | **GET** /Categories | Returns all Product Categories. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
[**categories_by_id**](PartSearchApi.md#categories_by_id) | **GET** /Categories/{categoryId} | Returns Category for given Id. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
[**digi_reel_pricing**](PartSearchApi.md#digi_reel_pricing) | **GET** /Products/{digiKeyPartNumber}/DigiReelPricing | Calculate the DigiReel pricing for the given DigiKeyPartNumber and RequestedQuantity
[**keyword_search**](PartSearchApi.md#keyword_search) | **POST** /Products/Keyword | KeywordSearch can search for any product in the Digi-Key catalog.
[**manufacturer_product_details**](PartSearchApi.md#manufacturer_product_details) | **POST** /Products/ManufacturerProductDetails | Create list of ProductDetails from the matches of the requested manufacturer product name.
[**manufacturers**](PartSearchApi.md#manufacturers) | **GET** /Manufacturers | Returns all Product Manufacturers. ManufacturersId can be used in KeywordSearchRequest.Filters.ManufacturerIds to restrict a keyword search to a given Manufacturer
[**product_details**](PartSearchApi.md#product_details) | **GET** /Products/{digiKeyPartNumber} | Retrieve detailed product information including real time pricing and availability.
[**suggested_parts**](PartSearchApi.md#suggested_parts) | **GET** /Products/{partNumber}/WithSuggestedProducts | Retrieve detailed product information and two suggested products


# **categories**
> CategoriesResponse categories(authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Returns all Product Categories. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category

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
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Returns all Product Categories. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
    api_response = api_instance.categories(authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_by_id**
> Category categories_by_id(category_id, authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Returns Category for given Id. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category

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
category_id = 56 # int | 
authorization = 'authorization_example' # str | OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Returns Category for given Id. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
    api_response = api_instance.categories_by_id(category_id, authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->categories_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **digi_reel_pricing**
> DigiReelPricingDto digi_reel_pricing(digi_key_part_number, requested_quantity, authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Calculate the DigiReel pricing for the given DigiKeyPartNumber and RequestedQuantity

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
digi_key_part_number = 'digi_key_part_number_example' # str | The Digi-Key PartNumber requested for Digi-Reel price calculation. It must be a  Digi-Key part number that is for a Digi-Reel pack type.
requested_quantity = 56 # int | The quantity of the product you are looking to create a Digi-Reel with. Must be greater  than 0.
authorization = 'authorization_example' # str | OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str | Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"ExtendedPrice,ReelingFee\" (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Calculate the DigiReel pricing for the given DigiKeyPartNumber and RequestedQuantity
    api_response = api_instance.digi_reel_pricing(digi_key_part_number, requested_quantity, authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->digi_reel_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digi_key_part_number** | **str**| The Digi-Key PartNumber requested for Digi-Reel price calculation. It must be a  Digi-Key part number that is for a Digi-Reel pack type. | 
 **requested_quantity** | **int**| The quantity of the product you are looking to create a Digi-Reel with. Must be greater  than 0. | 
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**| Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \&quot;ExtendedPrice,ReelingFee\&quot; | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**DigiReelPricingDto**](DigiReelPricingDto.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **manufacturer_product_details**
> ProductDetailsResponse manufacturer_product_details(authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)

Create list of ProductDetails from the matches of the requested manufacturer product name.

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
includes = 'includes_example' # str | Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"Products(DigiKeyPartNumber,QuantityAvailable)\" (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)
body = digikey.ManufacturerProductDetailsRequest() # ManufacturerProductDetailsRequest | ManufacturerProductDetailsRequest (optional)

try:
    # Create list of ProductDetails from the matches of the requested manufacturer product name.
    api_response = api_instance.manufacturer_product_details(authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->manufacturer_product_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**| Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \&quot;Products(DigiKeyPartNumber,QuantityAvailable)\&quot; | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 
 **body** | [**ManufacturerProductDetailsRequest**](ManufacturerProductDetailsRequest.md)| ManufacturerProductDetailsRequest | [optional] 

### Return type

[**ProductDetailsResponse**](ProductDetailsResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturers**
> ManufacturersResponse manufacturers(authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Returns all Product Manufacturers. ManufacturersId can be used in KeywordSearchRequest.Filters.ManufacturerIds to restrict a keyword search to a given Manufacturer

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
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Returns all Product Manufacturers. ManufacturersId can be used in KeywordSearchRequest.Filters.ManufacturerIds to restrict a keyword search to a given Manufacturer
    api_response = api_instance.manufacturers(authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->manufacturers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ManufacturersResponse**](ManufacturersResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_details**
> ProductDetails product_details(digi_key_part_number, authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve detailed product information including real time pricing and availability.

Works best with a Digi-Key part number. Some manufacturer part numbers conflict with unrelated parts and may not  return the correct product.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

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
digi_key_part_number = 'digi_key_part_number_example' # str | The product to retrieve details for.
authorization = 'authorization_example' # str | OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str | Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \"DigiKeyPartNumber,QuantityAvailable,AssociatedProducts[2]\" (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve detailed product information including real time pricing and availability.
    api_response = api_instance.product_details(digi_key_part_number, authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->product_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digi_key_part_number** | **str**| The product to retrieve details for. | 
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**| Comma separated list of fields to return. Used to customize response to reduce bandwidth by  selecting fields that you wish to receive. For example: \&quot;DigiKeyPartNumber,QuantityAvailable,AssociatedProducts[2]\&quot; | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ProductDetails**](ProductDetails.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggested_parts**
> ProductWithSuggestions suggested_parts(part_number, authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve detailed product information and two suggested products

Works best with a Digi-Key part number. Some manufacturer part numbers conflict with unrelated parts and may not  return the correct product.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

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
part_number = 'part_number_example' # str | The product to retrieve details for.
authorization = 'authorization_example' # str | OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve detailed product information and two suggested products
    api_response = api_instance.suggested_parts(part_number, authorization, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->suggested_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_number** | **str**| The product to retrieve details for. | 
 **authorization** | **str**| OAuth Bearer Token. Please see https://developer.digikey.com/documentation/oauth page for more info. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ProductWithSuggestions**](ProductWithSuggestions.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

