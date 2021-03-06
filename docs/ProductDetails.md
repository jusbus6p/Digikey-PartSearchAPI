# ProductDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_pricing** | [**list[PriceBreak]**](PriceBreak.md) | Your pricing for the account with which you authenticated. Also dependent on locale information. | [optional] 
**obsolete** | **bool** | Indicates whether this Part is obsolete. | [optional] 
**media_links** | [**list[MediaLinks]**](MediaLinks.md) | Collection of MediaLinks objects. These can contain links to datasheets, photos or manuals. | [optional] 
**standard_package** | **int** | The number of products in the manufacturer&#39;s standard package. | [optional] 
**limited_taxonomy** | [**LimitedTaxonomy**](LimitedTaxonomy.md) |  | [optional] 
**kits** | [**list[AssociatedProduct]**](AssociatedProduct.md) | Kits that this product is contained in. | [optional] 
**kit_contents** | [**list[KitPart]**](KitPart.md) | Products contained within this product. Only applicable if this product is a kit. | [optional] 
**mating_products** | [**list[AssociatedProduct]**](AssociatedProduct.md) | An association of same manufacturer products that mate with each other. | [optional] 
**search_locale_used** | [**IsoSearchLocale**](IsoSearchLocale.md) |  | [optional] 
**associated_products** | [**list[AssociatedProduct]**](AssociatedProduct.md) | Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ. | [optional] 
**for_use_with_products** | [**list[AssociatedProduct]**](AssociatedProduct.md) | Products that are directly correlated to complete the intended function of the product. These products may be  either same manufacturer or differ. | [optional] 
**rohs_subs** | [**list[AssociatedProduct]**](AssociatedProduct.md) | Rohs substitutions  Note: This is now only available in a details call from partsearch. | [optional] 
**suggested_subs** | [**list[AssociatedProduct]**](AssociatedProduct.md) | Suggested substitutions for when the product is obsolete.  Note: Only available in details calls | [optional] 
**additional_value_fee** | **float** | Any additional value fee. Most commonly the Digi-Reel fee. May be used for programmable parts as well. | [optional] 
**reach_effective_date** | **str** | REACH effective date is string in format \&quot;MMM-yyyy\&quot; or blank \&quot;\&quot;.  REACH is a regulation of the European Union. See documentation from the European Chemicals Agency. | [optional] 
**shipping_info** | **str** | Filled with shipping information, restrictions, or empty  REACH is a regulation of the European Union. See documentation from the European Chemicals Agency. | [optional] 
**standard_pricing** | [**list[PriceBreak]**](PriceBreak.md) | Standard pricing for the validated locale. | [optional] 
**ro_hs_status** | **str** | RoHS status. Can be: RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, ROHS3 Compliant. | [optional] 
**lead_status** | **str** | Lead status. Can be: Lead Free, Contains lead, Lead Free By Exemption, Not Applicable, Vendor undefined, unknown,  or Request Inventory Verification. | [optional] 
**parameters** | [**list[PidVid]**](PidVid.md) | Parameters for the part. Can be used for filtering keyword searches. | [optional] 
**product_url** | **str** | Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values. | [optional] 
**primary_datasheet** | **str** | The URL to the product&#39;s datasheet. | [optional] 
**primary_photo** | **str** | The URL to the product&#39;s image. | [optional] 
**primary_video** | **str** | The URL to the product&#39;s video. | [optional] 
**series** | [**PidVid**](PidVid.md) |  | [optional] 
**manufacturer_lead_weeks** | **str** | The number of weeks expected to receive stock from manufacturer. | [optional] 
**manufacturer_page_url** | **str** | The URL to Digi-Key&#39;s page on the manufacturer. | [optional] 
**product_status** | **str** | Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key, Last Time Buy, Not For New  Designs, Preliminary. For obsolete parts the part will become a non-stocking item when stock is depleted; minimums  will apply. Order the quantity available or the quantity available plus a multiple of the minimum order quantity. | [optional] 
**date_last_buy_chance** | **datetime** | Last date that the product will be available for purchase. Date is in ISO 8601. | [optional] 
**alternate_packaging** | [**list[BasicProduct]**](BasicProduct.md) | Other packaging types available for this product. | [optional] 
**detailed_description** | **str** | Extended catalog description of the product. | [optional] 
**reach_status** | **str** | REACH is a regulation of the European Union. See documentation from the European Chemicals Agency. | [optional] 
**export_control_class_number** | **str** | Export control class number. See documentation from the U.S. Department of Commerce. | [optional] 
**htsus_code** | **str** | Harmonized Tariff Schedule of the United States. See documentation from the U.S. International Trade Commission. | [optional] 
**tariff_description** | **str** | Description of the tariff status. Only applies if purchasing in USD and shipping to the US. Valid options are No  Tariff and Tariff Applied. | [optional] 
**moisture_sensitivity_level** | **str** | Code for Moisture Sensitivity Level of the product | [optional] 
**family** | [**PidVid**](PidVid.md) |  | [optional] 
**category** | [**PidVid**](PidVid.md) |  | [optional] 
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


