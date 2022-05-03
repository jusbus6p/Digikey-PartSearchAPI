# digikey.PartSearchApi

All URIs are relative to *https://api.digikey.com/Search/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyword_search**](PartSearchApi.md#keyword_search) | **POST** /Products/Keyword | KeywordSearch can search for any product in the Digi-Key catalog.

# **keyword_search**
> KeywordSearchResponse keyword_search(authorization, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)

KeywordSearch can search for any product in the Digi-Key catalog.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_search_request** | [**KeywordSearchRequest**](KeywordSearchRequest.md)|  | [optional] 

### Return type

[**KeywordSearchResponse**](KeywordSearchResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
