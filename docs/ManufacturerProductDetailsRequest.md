# ManufacturerProductDetailsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer_product** | **str** | Manufacturer product name to search on. | 
**record_count** | **int** | Number of products to return between 1 and 50. | [optional] 
**record_start_position** | **int** | The starting index of the records returned. This is used to paginate beyond 50 results. | [optional] 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**sort** | [**SortParameters**](SortParameters.md) |  | [optional] 
**requested_quantity** | **int** | The quantity of the product you are looking to purchase. This is used with the SortByUnitPrice SortOption as price varies at differing quantities. | [optional] 
**search_options** | [**list[SearchOption]**](SearchOption.md) | Filters the search results by the included SearchOption. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


