# aspose_barcode_cloud.RecognizeApi

All URIs are relative to *https://api.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**recognize**](RecognizeApi.md#recognize) | **GET** /barcode/recognize | Recognize a barcode from a file on an Internet server using a GET request with a query string parameter. For recognizing files from your hard drive, use &#x60;recognize-body&#x60; or &#x60;recognize-multipart&#x60; endpoints instead.
[**recognize_base64**](RecognizeApi.md#recognize_base64) | **POST** /barcode/recognize-body | Recognize a barcode from a file in the request body using a POST request with JSON or XML body parameters.
[**recognize_multipart**](RecognizeApi.md#recognize_multipart) | **POST** /barcode/recognize-multipart | Recognize a barcode from a file in the request body using a POST request with multipart form parameters.


# **recognize**
> BarcodeResponseList recognize(barcode_type, file_url, recognition_mode=recognition_mode, recognition_image_kind=recognition_image_kind)

Recognize a barcode from a file on an Internet server using a GET request with a query string parameter. For recognizing files from your hard drive, use `recognize-body` or `recognize-multipart` endpoints instead.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.DecodeBarcodeType() # DecodeBarcodeType | Type of barcode to recognize.
file_url = 'file_url_example' # str | URL to the barcode image.
recognition_mode = aspose_barcode_cloud.RecognitionMode() # RecognitionMode | Recognition mode. (optional)
recognition_image_kind = aspose_barcode_cloud.RecognitionImageKind() # RecognitionImageKind | Image kind for recognition. (optional)

try:
    # Recognize a barcode from a file on an Internet server using a GET request with a query string parameter. For recognizing files from your hard drive, use `recognize-body` or `recognize-multipart` endpoints instead.
    api_response = api_instance.recognize(barcode_type, file_url, recognition_mode=recognition_mode, recognition_image_kind=recognition_image_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**DecodeBarcodeType**](.md)| Type of barcode to recognize. | 
 **file_url** | **str**| URL to the barcode image. | 
 **recognition_mode** | [**RecognitionMode**](.md)| Recognition mode. | [optional] 
 **recognition_image_kind** | [**RecognitionImageKind**](.md)| Image kind for recognition. | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_base64**
> BarcodeResponseList recognize_base64(recognize_base64_request)

Recognize a barcode from a file in the request body using a POST request with JSON or XML body parameters.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi(aspose_barcode_cloud.ApiClient(configuration))
recognize_base64_request = aspose_barcode_cloud.RecognizeBase64Request() # RecognizeBase64Request | Barcode recognition request.

try:
    # Recognize a barcode from a file in the request body using a POST request with JSON or XML body parameters.
    api_response = api_instance.recognize_base64(recognize_base64_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_base64: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **recognize_base64_request** | [**RecognizeBase64Request**](RecognizeBase64Request.md)| Barcode recognition request. | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recognize_multipart**
> BarcodeResponseList recognize_multipart(barcode_type, file, recognition_mode=recognition_mode, recognition_image_kind=recognition_image_kind)

Recognize a barcode from a file in the request body using a POST request with multipart form parameters.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.RecognizeApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.DecodeBarcodeType() # DecodeBarcodeType | 
file = None # bytearray | Barcode image file.
recognition_mode = aspose_barcode_cloud.RecognitionMode() # RecognitionMode |  (optional)
recognition_image_kind = aspose_barcode_cloud.RecognitionImageKind() # RecognitionImageKind |  (optional)

try:
    # Recognize a barcode from a file in the request body using a POST request with multipart form parameters.
    api_response = api_instance.recognize_multipart(barcode_type, file, recognition_mode=recognition_mode, recognition_image_kind=recognition_image_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**DecodeBarcodeType**](DecodeBarcodeType.md)|  | 
 **file** | **bytearray**| Barcode image file. | 
 **recognition_mode** | [**RecognitionMode**](RecognitionMode.md)|  | [optional] 
 **recognition_image_kind** | [**RecognitionImageKind**](RecognitionImageKind.md)|  | [optional] 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

