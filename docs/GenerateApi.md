# aspose_barcode_cloud.GenerateApi

All URIs are relative to *https://api.aspose.cloud/v4.0*

Method | HTTP request | Description
------ | ------------ | -----------
[**generate**](GenerateApi.md#generate) | **GET** /barcode/generate/{barcodeType} | Generate a barcode using a GET request with parameters in the route and query string.
[**generate_body**](GenerateApi.md#generate_body) | **POST** /barcode/generate-body | Generate a barcode using a POST request with parameters in the request body in JSON or XML format.
[**generate_multipart**](GenerateApi.md#generate_multipart) | **POST** /barcode/generate-multipart | Generate a barcode using a POST request with parameters in a multipart form.


# **generate**
> bytearray generate(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, qr_encode_mode=qr_encode_mode, qr_error_level=qr_error_level, qr_version=qr_version, qr_eci_encoding=qr_eci_encoding, qr_aspect_ratio=qr_aspect_ratio, micro_qr_version=micro_qr_version, rect_micro_qr_version=rect_micro_qr_version, code128_encode_mode=code128_encode_mode, pdf417_encode_mode=pdf417_encode_mode, pdf417_error_level=pdf417_error_level, pdf417_truncate=pdf417_truncate, pdf417_columns=pdf417_columns, pdf417_rows=pdf417_rows, pdf417_aspect_ratio=pdf417_aspect_ratio, pdf417_eci_encoding=pdf417_eci_encoding, pdf417_is_reader_initialization=pdf417_is_reader_initialization, pdf417_macro_characters=pdf417_macro_characters, pdf417_is_linked=pdf417_is_linked, pdf417_is_code128_emulation=pdf417_is_code128_emulation)

Generate a barcode using a GET request with parameters in the route and query string.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | Type of barcode to generate.
data = 'data_example' # str | String that represents the data to encode.
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType | Type of data to encode. Default value: StringData. (optional)
image_format = aspose_barcode_cloud.BarcodeImageFormat() # BarcodeImageFormat | Barcode output image format. Default value: png. (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation | Specify the displayed text location. Set to CodeLocation.None to hide CodeText. Default value depends on BarcodeType: CodeLocation.Below for 1D barcodes and CodeLocation.None for 2D barcodes. (optional)
foreground_color = 'Black' # str | Specify the display color for bars and content. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: Black. (optional) (default to 'Black')
background_color = 'White' # str | Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: White. (optional) (default to 'White')
units = aspose_barcode_cloud.GraphicsUnit() # GraphicsUnit | Common units for all measurements. Default units: pixels. (optional)
resolution = 3.4 # float | Resolution of the barcode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is a dot. (optional)
image_height = 3.4 # float | Height of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. (optional)
image_width = 3.4 # float | Width of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. (optional)
rotation_angle = 56 # int | Barcode image rotation angle, measured in degrees. For example, RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle is not equal to 90, 180, 270, or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)
qr_encode_mode = aspose_barcode_cloud.QREncodeMode() # QREncodeMode | QR barcode encode mode. (optional)
qr_error_level = aspose_barcode_cloud.QRErrorLevel() # QRErrorLevel | QR barcode error correction level. (optional)
qr_version = aspose_barcode_cloud.QRVersion() # QRVersion | QR barcode version. Automatically selects the smallest version that fits the data. (optional)
qr_eci_encoding = aspose_barcode_cloud.ECIEncodings() # ECIEncodings | ECI encoding for QR barcode data. (optional)
qr_aspect_ratio = 3.4 # float | QR barcode aspect ratio. Values: 0 to 1. (optional)
micro_qr_version = aspose_barcode_cloud.MicroQRVersion() # MicroQRVersion | MicroQR barcode version. Used when BarcodeType is MicroQR. (optional)
rect_micro_qr_version = aspose_barcode_cloud.RectMicroQRVersion() # RectMicroQRVersion | RectMicroQR barcode version. Used when BarcodeType is RectMicroQR. (optional)
code128_encode_mode = aspose_barcode_cloud.Code128EncodeMode() # Code128EncodeMode | Code128 barcode encode mode. Controls which Code 128 subset (A, B, C, or mix) is used. (optional)
pdf417_encode_mode = aspose_barcode_cloud.Pdf417EncodeMode() # Pdf417EncodeMode | PDF417 barcode encode mode. (optional)
pdf417_error_level = aspose_barcode_cloud.Pdf417ErrorLevel() # Pdf417ErrorLevel | PDF417 barcode error correction level. (optional)
pdf417_truncate = True # bool | Whether to use truncated PDF417 format (removes right-side stop pattern). (optional)
pdf417_columns = 56 # int | Number of columns in the PDF417 barcode. Values between 1 and 30. 0 for auto. (optional)
pdf417_rows = 56 # int | Number of rows in the PDF417 barcode. Values between 3 and 90. 0 for automatic. (optional)
pdf417_aspect_ratio = 3.4 # float | PDF417 barcode aspect ratio (height/width of the barcode module). Values are defined by the standard: 2 to 5 for MicroPdf417; 3 to 5 for Pdf417 and MacroPdf417. (optional)
pdf417_eci_encoding = aspose_barcode_cloud.ECIEncodings() # ECIEncodings | ECI encoding for PDF417 barcode data. (optional)
pdf417_is_reader_initialization = True # bool | Whether the barcode is used for reader initialization (programming). (optional)
pdf417_macro_characters = aspose_barcode_cloud.MacroCharacter() # MacroCharacter | Macro character to prepend (structured append). (optional)
pdf417_is_linked = True # bool | Whether to use linked mode (for MicroPdf417). (optional)
pdf417_is_code128_emulation = True # bool | Whether to use Code128 emulation for MicroPdf417. (optional)

try:
    # Generate a barcode using a GET request with parameters in the route and query string.
    api_response = api_instance.generate(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, qr_encode_mode=qr_encode_mode, qr_error_level=qr_error_level, qr_version=qr_version, qr_eci_encoding=qr_eci_encoding, qr_aspect_ratio=qr_aspect_ratio, micro_qr_version=micro_qr_version, rect_micro_qr_version=rect_micro_qr_version, code128_encode_mode=code128_encode_mode, pdf417_encode_mode=pdf417_encode_mode, pdf417_error_level=pdf417_error_level, pdf417_truncate=pdf417_truncate, pdf417_columns=pdf417_columns, pdf417_rows=pdf417_rows, pdf417_aspect_ratio=pdf417_aspect_ratio, pdf417_eci_encoding=pdf417_eci_encoding, pdf417_is_reader_initialization=pdf417_is_reader_initialization, pdf417_macro_characters=pdf417_macro_characters, pdf417_is_linked=pdf417_is_linked, pdf417_is_code128_emulation=pdf417_is_code128_emulation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](.md)| Type of barcode to generate. | 
 **data** | **str**| String that represents the data to encode. | 
 **data_type** | [**EncodeDataType**](.md)| Type of data to encode. Default value: StringData. | [optional] 
 **image_format** | [**BarcodeImageFormat**](.md)| Barcode output image format. Default value: png. | [optional] 
 **text_location** | [**CodeLocation**](.md)| Specify the displayed text location. Set to CodeLocation.None to hide CodeText. Default value depends on BarcodeType: CodeLocation.Below for 1D barcodes and CodeLocation.None for 2D barcodes. | [optional] 
 **foreground_color** | **str**| Specify the display color for bars and content. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: Black. | [optional] [default to &#39;Black&#39;]
 **background_color** | **str**| Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: White. | [optional] [default to &#39;White&#39;]
 **units** | [**GraphicsUnit**](.md)| Common units for all measurements. Default units: pixels. | [optional] 
 **resolution** | **float**| Resolution of the barcode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is a dot. | [optional] 
 **image_height** | **float**| Height of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
 **image_width** | **float**| Width of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
 **rotation_angle** | **int**| Barcode image rotation angle, measured in degrees. For example, RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle is not equal to 90, 180, 270, or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 
 **qr_encode_mode** | [**QREncodeMode**](.md)| QR barcode encode mode. | [optional] 
 **qr_error_level** | [**QRErrorLevel**](.md)| QR barcode error correction level. | [optional] 
 **qr_version** | [**QRVersion**](.md)| QR barcode version. Automatically selects the smallest version that fits the data. | [optional] 
 **qr_eci_encoding** | [**ECIEncodings**](.md)| ECI encoding for QR barcode data. | [optional] 
 **qr_aspect_ratio** | **float**| QR barcode aspect ratio. Values: 0 to 1. | [optional] 
 **micro_qr_version** | [**MicroQRVersion**](.md)| MicroQR barcode version. Used when BarcodeType is MicroQR. | [optional] 
 **rect_micro_qr_version** | [**RectMicroQRVersion**](.md)| RectMicroQR barcode version. Used when BarcodeType is RectMicroQR. | [optional] 
 **code128_encode_mode** | [**Code128EncodeMode**](.md)| Code128 barcode encode mode. Controls which Code 128 subset (A, B, C, or mix) is used. | [optional] 
 **pdf417_encode_mode** | [**Pdf417EncodeMode**](.md)| PDF417 barcode encode mode. | [optional] 
 **pdf417_error_level** | [**Pdf417ErrorLevel**](.md)| PDF417 barcode error correction level. | [optional] 
 **pdf417_truncate** | **bool**| Whether to use truncated PDF417 format (removes right-side stop pattern). | [optional] 
 **pdf417_columns** | **int**| Number of columns in the PDF417 barcode. Values between 1 and 30. 0 for auto. | [optional] 
 **pdf417_rows** | **int**| Number of rows in the PDF417 barcode. Values between 3 and 90. 0 for automatic. | [optional] 
 **pdf417_aspect_ratio** | **float**| PDF417 barcode aspect ratio (height/width of the barcode module). Values are defined by the standard: 2 to 5 for MicroPdf417; 3 to 5 for Pdf417 and MacroPdf417. | [optional] 
 **pdf417_eci_encoding** | [**ECIEncodings**](.md)| ECI encoding for PDF417 barcode data. | [optional] 
 **pdf417_is_reader_initialization** | **bool**| Whether the barcode is used for reader initialization (programming). | [optional] 
 **pdf417_macro_characters** | [**MacroCharacter**](.md)| Macro character to prepend (structured append). | [optional] 
 **pdf417_is_linked** | **bool**| Whether to use linked mode (for MicroPdf417). | [optional] 
 **pdf417_is_code128_emulation** | **bool**| Whether to use Code128 emulation for MicroPdf417. | [optional] 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_body**
> bytearray generate_body(generate_params)

Generate a barcode using a POST request with parameters in the request body in JSON or XML format.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
generate_params = aspose_barcode_cloud.GenerateParams() # GenerateParams | Generation parameters.

try:
    # Generate a barcode using a POST request with parameters in the request body in JSON or XML format.
    api_response = api_instance.generate_body(generate_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate_body: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **generate_params** | [**GenerateParams**](GenerateParams.md)| Generation parameters. | 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_multipart**
> bytearray generate_multipart(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, qr_encode_mode=qr_encode_mode, qr_error_level=qr_error_level, qr_version=qr_version, qr_eci_encoding=qr_eci_encoding, qr_aspect_ratio=qr_aspect_ratio, micro_qr_version=micro_qr_version, rect_micro_qr_version=rect_micro_qr_version, code128_encode_mode=code128_encode_mode, pdf417_encode_mode=pdf417_encode_mode, pdf417_error_level=pdf417_error_level, pdf417_truncate=pdf417_truncate, pdf417_columns=pdf417_columns, pdf417_rows=pdf417_rows, pdf417_aspect_ratio=pdf417_aspect_ratio, pdf417_eci_encoding=pdf417_eci_encoding, pdf417_is_reader_initialization=pdf417_is_reader_initialization, pdf417_macro_characters=pdf417_macro_characters, pdf417_is_linked=pdf417_is_linked, pdf417_is_code128_emulation=pdf417_is_code128_emulation)

Generate a barcode using a POST request with parameters in a multipart form.

### Example
```python
import time
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = aspose_barcode_cloud.Configuration(access_token="YOUR_ACCESS_TOKEN")

# create an instance of the API class
api_instance = aspose_barcode_cloud.GenerateApi(aspose_barcode_cloud.ApiClient(configuration))
barcode_type = aspose_barcode_cloud.EncodeBarcodeType() # EncodeBarcodeType | 
data = 'data_example' # str | String that represents the data to encode.
data_type = aspose_barcode_cloud.EncodeDataType() # EncodeDataType |  (optional)
image_format = aspose_barcode_cloud.BarcodeImageFormat() # BarcodeImageFormat |  (optional)
text_location = aspose_barcode_cloud.CodeLocation() # CodeLocation |  (optional)
foreground_color = 'Black' # str | Specify the display color for bars and content. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: Black. (optional) (default to 'Black')
background_color = 'White' # str | Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: White. (optional) (default to 'White')
units = aspose_barcode_cloud.GraphicsUnit() # GraphicsUnit |  (optional)
resolution = 3.4 # float | Resolution of the barcode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is a dot. (optional)
image_height = 3.4 # float | Height of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. (optional)
image_width = 3.4 # float | Width of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. (optional)
rotation_angle = 56 # int | Barcode image rotation angle, measured in degrees. For example, RotationAngle = 0 or RotationAngle = 360 means no rotation. If RotationAngle is not equal to 90, 180, 270, or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. (optional)
qr_encode_mode = aspose_barcode_cloud.QREncodeMode() # QREncodeMode |  (optional)
qr_error_level = aspose_barcode_cloud.QRErrorLevel() # QRErrorLevel |  (optional)
qr_version = aspose_barcode_cloud.QRVersion() # QRVersion |  (optional)
qr_eci_encoding = aspose_barcode_cloud.ECIEncodings() # ECIEncodings |  (optional)
qr_aspect_ratio = 3.4 # float | QR barcode aspect ratio. Values: 0 to 1. (optional)
micro_qr_version = aspose_barcode_cloud.MicroQRVersion() # MicroQRVersion |  (optional)
rect_micro_qr_version = aspose_barcode_cloud.RectMicroQRVersion() # RectMicroQRVersion |  (optional)
code128_encode_mode = aspose_barcode_cloud.Code128EncodeMode() # Code128EncodeMode |  (optional)
pdf417_encode_mode = aspose_barcode_cloud.Pdf417EncodeMode() # Pdf417EncodeMode |  (optional)
pdf417_error_level = aspose_barcode_cloud.Pdf417ErrorLevel() # Pdf417ErrorLevel |  (optional)
pdf417_truncate = True # bool | Whether to use truncated PDF417 format (removes right-side stop pattern). (optional)
pdf417_columns = 56 # int | Number of columns in the PDF417 barcode. Values between 1 and 30. 0 for auto. (optional)
pdf417_rows = 56 # int | Number of rows in the PDF417 barcode. Values between 3 and 90. 0 for automatic. (optional)
pdf417_aspect_ratio = 3.4 # float | PDF417 barcode aspect ratio (height/width of the barcode module). Values are defined by the standard: 2 to 5 for MicroPdf417; 3 to 5 for Pdf417 and MacroPdf417. (optional)
pdf417_eci_encoding = aspose_barcode_cloud.ECIEncodings() # ECIEncodings |  (optional)
pdf417_is_reader_initialization = True # bool | Whether the barcode is used for reader initialization (programming). (optional)
pdf417_macro_characters = aspose_barcode_cloud.MacroCharacter() # MacroCharacter |  (optional)
pdf417_is_linked = True # bool | Whether to use linked mode (for MicroPdf417). (optional)
pdf417_is_code128_emulation = True # bool | Whether to use Code128 emulation for MicroPdf417. (optional)

try:
    # Generate a barcode using a POST request with parameters in a multipart form.
    api_response = api_instance.generate_multipart(barcode_type, data, data_type=data_type, image_format=image_format, text_location=text_location, foreground_color=foreground_color, background_color=background_color, units=units, resolution=resolution, image_height=image_height, image_width=image_width, rotation_angle=rotation_angle, qr_encode_mode=qr_encode_mode, qr_error_level=qr_error_level, qr_version=qr_version, qr_eci_encoding=qr_eci_encoding, qr_aspect_ratio=qr_aspect_ratio, micro_qr_version=micro_qr_version, rect_micro_qr_version=rect_micro_qr_version, code128_encode_mode=code128_encode_mode, pdf417_encode_mode=pdf417_encode_mode, pdf417_error_level=pdf417_error_level, pdf417_truncate=pdf417_truncate, pdf417_columns=pdf417_columns, pdf417_rows=pdf417_rows, pdf417_aspect_ratio=pdf417_aspect_ratio, pdf417_eci_encoding=pdf417_eci_encoding, pdf417_is_reader_initialization=pdf417_is_reader_initialization, pdf417_macro_characters=pdf417_macro_characters, pdf417_is_linked=pdf417_is_linked, pdf417_is_code128_emulation=pdf417_is_code128_emulation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerateApi->generate_multipart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
---- | ---- | ------------ | -----
 **barcode_type** | [**EncodeBarcodeType**](EncodeBarcodeType.md)|  | 
 **data** | **str**| String that represents the data to encode. | 
 **data_type** | [**EncodeDataType**](EncodeDataType.md)|  | [optional] 
 **image_format** | [**BarcodeImageFormat**](BarcodeImageFormat.md)|  | [optional] 
 **text_location** | [**CodeLocation**](CodeLocation.md)|  | [optional] 
 **foreground_color** | **str**| Specify the display color for bars and content. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: Black. | [optional] [default to &#39;Black&#39;]
 **background_color** | **str**| Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: White. | [optional] [default to &#39;White&#39;]
 **units** | [**GraphicsUnit**](GraphicsUnit.md)|  | [optional] 
 **resolution** | **float**| Resolution of the barcode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is a dot. | [optional] 
 **image_height** | **float**| Height of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
 **image_width** | **float**| Width of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
 **rotation_angle** | **int**| Barcode image rotation angle, measured in degrees. For example, RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle is not equal to 90, 180, 270, or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 
 **qr_encode_mode** | [**QREncodeMode**](QREncodeMode.md)|  | [optional] 
 **qr_error_level** | [**QRErrorLevel**](QRErrorLevel.md)|  | [optional] 
 **qr_version** | [**QRVersion**](QRVersion.md)|  | [optional] 
 **qr_eci_encoding** | [**ECIEncodings**](ECIEncodings.md)|  | [optional] 
 **qr_aspect_ratio** | **float**| QR barcode aspect ratio. Values: 0 to 1. | [optional] 
 **micro_qr_version** | [**MicroQRVersion**](MicroQRVersion.md)|  | [optional] 
 **rect_micro_qr_version** | [**RectMicroQRVersion**](RectMicroQRVersion.md)|  | [optional] 
 **code128_encode_mode** | [**Code128EncodeMode**](Code128EncodeMode.md)|  | [optional] 
 **pdf417_encode_mode** | [**Pdf417EncodeMode**](Pdf417EncodeMode.md)|  | [optional] 
 **pdf417_error_level** | [**Pdf417ErrorLevel**](Pdf417ErrorLevel.md)|  | [optional] 
 **pdf417_truncate** | **bool**| Whether to use truncated PDF417 format (removes right-side stop pattern). | [optional] 
 **pdf417_columns** | **int**| Number of columns in the PDF417 barcode. Values between 1 and 30. 0 for auto. | [optional] 
 **pdf417_rows** | **int**| Number of rows in the PDF417 barcode. Values between 3 and 90. 0 for automatic. | [optional] 
 **pdf417_aspect_ratio** | **float**| PDF417 barcode aspect ratio (height/width of the barcode module). Values are defined by the standard: 2 to 5 for MicroPdf417; 3 to 5 for Pdf417 and MacroPdf417. | [optional] 
 **pdf417_eci_encoding** | [**ECIEncodings**](ECIEncodings.md)|  | [optional] 
 **pdf417_is_reader_initialization** | **bool**| Whether the barcode is used for reader initialization (programming). | [optional] 
 **pdf417_macro_characters** | [**MacroCharacter**](MacroCharacter.md)|  | [optional] 
 **pdf417_is_linked** | **bool**| Whether to use linked mode (for MicroPdf417). | [optional] 
 **pdf417_is_code128_emulation** | **bool**| Whether to use Code128 emulation for MicroPdf417. | [optional] 

### Return type

**bytearray**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/png, image/bmp, image/gif, image/jpeg, image/svg+xml, image/tiff, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

