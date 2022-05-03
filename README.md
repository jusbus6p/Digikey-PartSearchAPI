# digikey
Search for products and retrieve details and pricing.

This Python package is semi-automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: Ps2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developer.digikey.com/support](https://developer.digikey.com/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/jusbus6p/Digikey-PartSearchAPI.git`)

Then import the package:
```python
import digikey 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import digikey
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following or your own code:

```python
from __future__ import print_function
import time
from digikey.api.part_search_api import PartSearchAPI
from digikey.api_exception import ApiException
from digikey.models.keyword_search_request import KeywordSearchRequest
from digikey.models.filters import Filters
from digikey.models.parametric_filter import ParametricFilter
from digikey.api_client import ApiClient
from digikey.configuration import Configuration
from pprint import pprint

config = Configuration()

config.client_id = "Your Client ID"
config.client_secret = "Your Client Secret"
config.client_callback_url = "Your Client Callback URL"

# Resource folder will be used to store and retrieve your access and refresh tokens.
config.resource_folder_path = "Directory to use for resource"

config.get_tokens_from_file()

client = ApiClient(config)

api = PartSearchAPI(client)

try:
    pfilters = ParametricFilter(-5, start)
    filteroption = Filters(parametric_filters=pfilters)

    kwsr = KeywordSearchRequest(keywords="-", record_count=50, record_start_position=start, filters=filteroption)
    
    data = api.keyword_search(kwsr)
    if data is not None:
        pprint(api_response)
except ApiException as e:
    print("Exception when calling PartSearchApi->keyword_search: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.digikey.com/Search/v3*

*NOTE:*
keyword_search is the only API that is currently implemented.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PartSearchApi* | [**categories**](docs/PartSearchApi.md#categories) | **GET** /Categories | Returns all Product Categories. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
*PartSearchApi* | [**categories_by_id**](docs/PartSearchApi.md#categories_by_id) | **GET** /Categories/{categoryId} | Returns Category for given Id. Category Id can be used in KeywordSearchRequest.Filters.TaxonomyIds to restrict a keyword search to a given category
*PartSearchApi* | [**digi_reel_pricing**](docs/PartSearchApi.md#digi_reel_pricing) | **GET** /Products/{digiKeyPartNumber}/DigiReelPricing | Calculate the DigiReel pricing for the given DigiKeyPartNumber and RequestedQuantity
*PartSearchApi* | [**keyword_search**](docs/PartSearchApi.md#keyword_search) | **POST** /Products/Keyword | KeywordSearch can search for any product in the Digi-Key catalog.
*PartSearchApi* | [**manufacturer_product_details**](docs/PartSearchApi.md#manufacturer_product_details) | **POST** /Products/ManufacturerProductDetails | Create list of ProductDetails from the matches of the requested manufacturer product name.
*PartSearchApi* | [**manufacturers**](docs/PartSearchApi.md#manufacturers) | **GET** /Manufacturers | Returns all Product Manufacturers. ManufacturersId can be used in KeywordSearchRequest.Filters.ManufacturerIds to restrict a keyword search to a given Manufacturer
*PartSearchApi* | [**product_details**](docs/PartSearchApi.md#product_details) | **GET** /Products/{digiKeyPartNumber} | Retrieve detailed product information including real time pricing and availability.
*PartSearchApi* | [**suggested_parts**](docs/PartSearchApi.md#suggested_parts) | **GET** /Products/{partNumber}/WithSuggestedProducts | Retrieve detailed product information and two suggested products


## Documentation For Models

 - [ApiErrorResponse](docs/ApiErrorResponse.md)
 - [ApiValidationError](docs/ApiValidationError.md)
 - [AssociatedProduct](docs/AssociatedProduct.md)
 - [BasicProduct](docs/BasicProduct.md)
 - [CategoriesResponse](docs/CategoriesResponse.md)
 - [Category](docs/Category.md)
 - [DigiReelPricingDto](docs/DigiReelPricingDto.md)
 - [Filters](docs/Filters.md)
 - [IsoSearchLocale](docs/IsoSearchLocale.md)
 - [KeywordSearchRequest](docs/KeywordSearchRequest.md)
 - [KeywordSearchResponse](docs/KeywordSearchResponse.md)
 - [KitPart](docs/KitPart.md)
 - [LimitedParameter](docs/LimitedParameter.md)
 - [LimitedTaxonomy](docs/LimitedTaxonomy.md)
 - [ManufacturerInfo](docs/ManufacturerInfo.md)
 - [ManufacturerProductDetailsRequest](docs/ManufacturerProductDetailsRequest.md)
 - [ManufacturersResponse](docs/ManufacturersResponse.md)
 - [MediaLinks](docs/MediaLinks.md)
 - [ParametricFilter](docs/ParametricFilter.md)
 - [PidVid](docs/PidVid.md)
 - [PriceBreak](docs/PriceBreak.md)
 - [Product](docs/Product.md)
 - [ProductDetails](docs/ProductDetails.md)
 - [ProductDetailsResponse](docs/ProductDetailsResponse.md)
 - [ProductWithSuggestions](docs/ProductWithSuggestions.md)
 - [SearchOption](docs/SearchOption.md)
 - [SortDirection](docs/SortDirection.md)
 - [SortOption](docs/SortOption.md)
 - [SortParameters](docs/SortParameters.md)
 - [ValuePair](docs/ValuePair.md)


## Documentation For Authorization


## apiKeySecurity

- **Type**: API key
- **API key parameter name**: X-DIGIKEY-Client-Id
- **Location**: HTTP header

## oauth2AccessCodeSecurity

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api.digikey.com/v1/oauth2/authorize
- **Scopes**: N/A


## Author
Justin Bushue

