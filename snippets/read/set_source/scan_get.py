import os
from aspose_barcode_cloud import ScanApi, ApiClient, Configuration


def make_configuration():
    """
    Creates and returns the configuration for the Aspose Barcode API.
    """
    env_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if env_token:
        config = Configuration(access_token=env_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():

    config = make_configuration()
    scan_api = ScanApi(ApiClient(config))

    barcode_image_url = "https://raw.githubusercontent.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/main/testdata/qr_and_code128.png"

    result = scan_api.scan(file_url=barcode_image_url)

    if result.barcodes and len(result.barcodes) > 0:
        print(f"Recognized barcode value: '{result.barcodes[0].barcode_value}'")
    else:
        print("No barcodes recognized.")


if __name__ == "__main__":
    main()
