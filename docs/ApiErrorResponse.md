# ApiErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_response_version** | **str** | The version of the error handler. | [optional] 
**status_code** | **int** | The HttpStatusCode of the error. | [optional] 
**error_message** | **str** | The message provided by the error handler. | [optional] 
**error_details** | **str** | The details of the error. | [optional] 
**request_id** | **str** | The Id of the request that triggered the error. If contacting API Support, please include the RequestId. | [optional] 
**validation_errors** | [**list[ApiValidationError]**](ApiValidationError.md) | The list of validation errors (if applicable). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


