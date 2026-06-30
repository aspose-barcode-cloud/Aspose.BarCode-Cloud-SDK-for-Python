import os
from aspose_barcode_cloud import (
    ApiClient,
    GenerateApi,
    EncodeBarcodeType,
    BarcodeImageFormat,
    BarcodeImageParams,
    Configuration,
)


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
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "Code39.png"))

    api_client = ApiClient(configuration=make_configuration())
    generate_api = GenerateApi(api_client=api_client)

    response = generate_api.generate_multipart(
        barcode_type=EncodeBarcodeType.CODE39,
        data="Aspose",
        barcode_image_params=BarcodeImageParams(
            foreground_color="Green",
            background_color="Yellow",
            image_format=BarcodeImageFormat.GIF,
        ),
    )

    with open(file_name, "wb") as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
