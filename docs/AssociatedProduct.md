# AssociatedProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_url** | **str** | Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values. | [optional] 
**manufacturer_part_number** | **str** | The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts. | [optional] 
**minimum_order_quantity** | **int** | The minimum quantity to order from Digi-Key. | [optional] 
**non_stock** | **bool** | Indicates this product is a non stock product. | [optional] 
**packaging** | [**PidVid**](PidVid.md) |  | [optional] 
**quantity_available** | **int** | Quantity of the product available for immediate sale. | [optional] 
**digi_key_part_number** | **str** | The Digi-Key part number. | [optional] 
**product_description** | **str** | Catalog description of the product. | [optional] 
**unit_price** | **float** | The price for a single unit of this product. | [optional] 
**manufacturer** | [**PidVid**](PidVid.md) |  | [optional] 
**manufacturer_public_quantity** | **int** | Quantity of this product available to order from manufacturer. | [optional] 
**quantity_on_order** | **int** | Quantity of this product ordered but not immediately available. | [optional] 
**max_quantity_for_distribution** | **int** | Maximum order quantity for Distribution | [optional] 
**back_order_not_allowed** | **bool** | True if back order is not allowed for this product | [optional] 
**dk_plus_restriction** | **bool** | If true- this product is not available for purchase through the Ordering API - it must be purchased through the  Digi-Key web site | [optional] 
**marketplace** | **bool** | Product is a Marketplace product that ships direct from the supplier.  A separate shipping fee may apply | [optional] 
**supplier_direct_ship** | **bool** | If true- this product is shipped directly from the Supplier | [optional] 
**pim_product_name** | **str** | Pim name for the product | [optional] 
**supplier** | **str** | The Supplier is the provider of the products to Digi-Key and some cases the customer directly. | [optional] 
**supplier_id** | **int** | Id for Supplier | [optional] 
**is_ncnr** | **bool** | Is product non-cancellable and non-returnable | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


