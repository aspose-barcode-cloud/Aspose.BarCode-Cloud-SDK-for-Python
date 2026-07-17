from aspose_barcode_cloud import ApiClient, Configuration, RecognizeApi, DecodeBarcodeType
import os


def main():
    access_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if access_token:
        config = Configuration(access_token=access_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    recognize_api = RecognizeApi(ApiClient(config))

    # Call the API to recognize the barcode
    result = recognize_api.recognize(
        barcode_type=DecodeBarcodeType.QR,
        file_url="https://raw.githubusercontent.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/main/testdata/qr_and_code128.png",
    )

    # Output the result
    if result.barcodes:
        print(f"File recognized, result: '{result.barcodes[0].barcode_value}'")
    else:
        print("No barcodes were recognized.")


if __name__ == "__main__":
    main()
