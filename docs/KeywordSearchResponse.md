# KeywordSearchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_taxonomy** | [**LimitedTaxonomy**](LimitedTaxonomy.md) |  | [optional] 
**filter_options** | [**list[LimitedParameter]**](LimitedParameter.md) | Available filters for narrowing down results. | [optional] 
**products** | [**list[Product]**](Product.md) | List of products returned by KeywordSearch | [optional] 
**products_count** | **int** | Total number of matching products found. | [optional] 
**exact_manufacturer_products_count** | **int** | Number of exact ManufacturerPartNumber matches. | [optional] 
**exact_manufacturer_products** | [**list[Product]**](Product.md) | List of products that are exact ManufacturerPartNumber matches. | [optional] 
**exact_digi_key_product** | [**Product**](Product.md) |  | [optional] 
**search_locale_used** | [**IsoSearchLocale**](IsoSearchLocale.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


