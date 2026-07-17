import os
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
    RecognitionImageKind,
    RecognitionMode,
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

    result = recognize_api.recognize(
        barcode_type=DecodeBarcodeType.QR,
        file_url="https://raw.githubusercontent.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/main/testdata/qr_and_code128.png",
        recognition_mode=RecognitionMode.FAST,
        recognition_image_kind=RecognitionImageKind.PHOTO,
    )

    print(f"File recognized, result: '{result.barcodes[0].barcode_value}'")


if __name__ == "__main__":
    main()
