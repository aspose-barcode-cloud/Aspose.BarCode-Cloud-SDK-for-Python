import os
from aspose_barcode_cloud import ApiClient, BarcodeImageParams, EncodeBarcodeType, Configuration, GraphicsUnit
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
    config = make_configuration()
    api_client = ApiClient(configuration=config)
    api = GenerateApi(api_client=api_client)

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "aztec.png"))

    response = api.generate_multipart(
        barcode_type=EncodeBarcodeType.AZTEC,
        data="Aspose.BarCode.Cloud",
        barcode_image_params=BarcodeImageParams(
            image_height=200,
            image_width=200,
            resolution=150,
            units=GraphicsUnit.POINT,
        ),
    )
    with open(file_name, "wb") as file_stream:
        file_stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
