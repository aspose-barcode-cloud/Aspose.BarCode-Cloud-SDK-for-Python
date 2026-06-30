import os
import base64
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
    RecognitionMode,
    RecognizeBase64Request,
)


def make_configuration():
    access_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if access_token:
        config = Configuration(access_token=access_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():
    config = make_configuration()
    recognize_api = RecognizeApi(ApiClient(config))

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417.png"))

    with open(file_name, "rb") as file:
        image_bytes = file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    request = RecognizeBase64Request(
        barcode_types=[DecodeBarcodeType.PDF417],
        file_base64=image_base64,
        recognition_mode=RecognitionMode.EXCELLENT,
    )

    result = recognize_api.recognize_base64(request)

    print(f"File '{file_name}' recognized, result: '{result.barcodes[0].barcode_value}'")


if __name__ == "__main__":
    main()
