import os
from pprint import pprint

from aspose_barcode_cloud import (
    GenerateApi,
    RecognizeApi,
    ApiClient,
    Configuration,
    EncodeBarcodeType,
    CodeLocation,
    DecodeBarcodeType,
    BarcodeImageParams,
    QrParams,
    QREncodeMode,
    QRErrorLevel,
    QRVersion,
)

config = Configuration(
    client_id="Client Id from https://dashboard.aspose.cloud/applications",
    client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
    access_token=os.environ.get("TEST_CONFIGURATION_ACCESS_TOKEN"),  # Only for testing in CI, remove this line
)

# Generate barcode
generateApi = GenerateApi(ApiClient(config))
response = generateApi.generate(
    EncodeBarcodeType.QR,
    "Example",
    barcode_image_params=BarcodeImageParams(text_location=CodeLocation.NONE),
    qr_params=QrParams(
        qr_encode_mode=QREncodeMode.AUTO,
        qr_error_level=QRErrorLevel.LEVELM,
        qr_version=QRVersion.AUTO,
        qr_aspect_ratio=0.75,
    ),
)
with open("example.png", "wb") as f:
    f.write(response.data)
print("Barcode saved to file 'example.png'")

# Recognize barcode
recognizeApi = RecognizeApi(ApiClient(config))
response = recognizeApi.recognize_multipart(DecodeBarcodeType.QR, open("example.png", "rb"))
pprint(response)
