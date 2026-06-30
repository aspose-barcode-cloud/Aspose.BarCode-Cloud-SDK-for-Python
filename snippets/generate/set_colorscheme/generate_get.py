import os
from aspose_barcode_cloud import ApiClient, EncodeBarcodeType, BarcodeImageFormat, BarcodeImageParams, Configuration
from aspose_barcode_cloud.api.generate_api import GenerateApi


def make_configuration():
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
    """Main function to generate QR code barcode."""
    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    response = generate_api.generate(
        EncodeBarcodeType.QR,
        "https://products.aspose.cloud/barcode/family/",
        barcode_image_params=BarcodeImageParams(
            foreground_color="DarkBlue",
            background_color="LightGray",
            image_format=BarcodeImageFormat.PNG,
        ),
    )

    # Write the response to a file
    with open(file_name, "wb") as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
