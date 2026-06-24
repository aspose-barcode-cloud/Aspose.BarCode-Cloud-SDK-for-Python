# Pdf417Params

Optional PDF417 barcode generation parameters. Applies to Pdf417, MacroPdf417, MicroPdf417, and GS1MicroPdf417 barcode types.

## Properties

Name | Type | Description | Notes
---- | ---- | ----------- | -----
**pdf417_encode_mode** | [**Pdf417EncodeMode**](Pdf417EncodeMode.md) | PDF417 barcode encode mode. | [optional] 
**pdf417_error_level** | [**Pdf417ErrorLevel**](Pdf417ErrorLevel.md) | PDF417 barcode error correction level. | [optional] 
**pdf417_truncate** | **bool** | Whether to use truncated PDF417 format (removes right-side stop pattern). | [optional] 
**pdf417_columns** | **int** | Number of columns in the PDF417 barcode. Values between 1 and 30. 0 for auto. | [optional] 
**pdf417_rows** | **int** | Number of rows in the PDF417 barcode. Values between 3 and 90. 0 for automatic. | [optional] 
**pdf417_aspect_ratio** | **float** | PDF417 barcode aspect ratio (height/width of the barcode module). Values are defined by the standard: 2 to 5 for MicroPdf417; 3 to 5 for Pdf417 and MacroPdf417. | [optional] 
**pdf417_eci_encoding** | [**ECIEncodings**](ECIEncodings.md) | ECI encoding for PDF417 barcode data. | [optional] 
**pdf417_is_reader_initialization** | **bool** | Whether the barcode is used for reader initialization (programming). | [optional] 
**pdf417_macro_characters** | [**MacroCharacter**](MacroCharacter.md) | Macro character to prepend (structured append). | [optional] 
**pdf417_is_linked** | **bool** | Whether to use linked mode (for MicroPdf417). | [optional] 
**pdf417_is_code128_emulation** | **bool** | Whether to use Code128 emulation for MicroPdf417. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
