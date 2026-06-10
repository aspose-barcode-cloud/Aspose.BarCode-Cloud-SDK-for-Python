# BarcodeImageParams

Optional barcode image parameters.

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**image_format** | [**BarcodeImageFormat**](BarcodeImageFormat.md) |  | [optional] 
**text_location** | [**CodeLocation**](CodeLocation.md) |  | [optional] 
**foreground_color** | **str** | Specify the display color for bars and content. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: Black. | [optional] [default to 'Black']
**background_color** | **str** | Background color of the barcode image. Value: Color name from https://reference.aspose.com/drawing/net/system.drawing/color/ or ARGB value starting with #. For example: AliceBlue or #FF000000. Default value: White. | [optional] [default to 'White']
**units** | [**GraphicsUnit**](GraphicsUnit.md) |  | [optional] 
**resolution** | **float** | Resolution of the barcode image. One value for both dimensions. Default value: 96 dpi. Decimal separator is a dot. | [optional] 
**image_height** | **float** | Height of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
**image_width** | **float** | Width of the barcode image in the specified units. Default units: pixels. Decimal separator is a dot. | [optional] 
**rotation_angle** | **int** | Barcode image rotation angle, measured in degrees. For example, RotationAngle &#x3D; 0 or RotationAngle &#x3D; 360 means no rotation. If RotationAngle is not equal to 90, 180, 270, or 0, it may increase the difficulty for the scanner to read the image. Default value: 0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
