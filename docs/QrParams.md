# QrParams

Optional QR barcode generation parameters. Applies to QR, GS1QR, MicroQR, and RectMicroQR barcode types.

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**qr_encode_mode** | [**QREncodeMode**](QREncodeMode.md) | QR barcode encode mode. | [optional] 
**qr_error_level** | [**QRErrorLevel**](QRErrorLevel.md) | QR barcode error correction level. | [optional] 
**qr_version** | [**QRVersion**](QRVersion.md) | QR barcode version. Automatically selects the smallest version that fits the data. | [optional] 
**qr_eci_encoding** | [**ECIEncodings**](ECIEncodings.md) | ECI encoding for QR barcode data. | [optional] 
**qr_aspect_ratio** | **float** | QR barcode aspect ratio. Values: 0 to 1. | [optional] 
**micro_qr_version** | [**MicroQRVersion**](MicroQRVersion.md) | MicroQR barcode version. Used when BarcodeType is MicroQR. | [optional] 
**rect_micro_qr_version** | [**RectMicroQRVersion**](RectMicroQRVersion.md) | RectMicroQR barcode version. Used when BarcodeType is RectMicroQR. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
