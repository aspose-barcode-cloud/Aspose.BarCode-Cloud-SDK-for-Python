# aspose_barcode_cloud.ScanApi

All URIs are relative to *https://api.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**scan**](ScanApi.md#scan) | **GET** /barcode/scan | Scan a barcode from a file on an Internet server using a GET request with a query string parameter. For scanning files from your hard drive, use &#x60;scan-body&#x60; or &#x60;scan-multipart&#x60; endpoints instead.
[**scan_base64**](ScanApi.md#scan_base64) | **POST** /barcode/scan-body | Scan a barcode from a file in the request body using a POST request with a JSON or XML body parameter.
[**scan_multipart**](ScanApi.md#scan_multipart) | **POST** /barcode/scan-multipart | Scan a barcode from a file in the request body using a POST request with a multipart form parameter.


# **scan**
> BarcodeResponseList scan(file_url)

Scan a barcode from a file on an Internet server using a GET request with a query string parameter. For scanning files from your hard drive, use `scan-body` or `scan-multipart` endpoints instead.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
file_url = 'file_url_example' # str | URL to the barcode image.

try:
    # Scan a barcode from a file on an Internet server using a GET request with a query string parameter. For scanning files from your hard drive, use `scan-body` or `scan-multipart` endpoints instead.
    api_response = api_instance.scan(file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **file_url** | **str**| URL to the barcode image. | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_base64**
> BarcodeResponseList scan_base64(scan_base64_request)

Scan a barcode from a file in the request body using a POST request with a JSON or XML body parameter.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
scan_base64_request = aspose_barcode_cloud.ScanBase64Request() # ScanBase64Request | Barcode scan request.

try:
    # Scan a barcode from a file in the request body using a POST request with a JSON or XML body parameter.
    api_response = api_instance.scan_base64(scan_base64_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_base64: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **scan_base64_request** | [**ScanBase64Request**](ScanBase64Request.md)| Barcode scan request. | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_multipart**
> BarcodeResponseList scan_multipart(file)

Scan a barcode from a file in the request body using a POST request with a multipart form parameter.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.ScanApi(aspose_barcode_cloud.ApiClient(configuration))
file = None # bytearray | Barcode image file.

try:
    # Scan a barcode from a file in the request body using a POST request with a multipart form parameter.
    api_response = api_instance.scan_multipart(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **file** | **bytearray**| Barcode image file. | 

### Return type

[**BarcodeResponseList**](BarcodeResponseList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

