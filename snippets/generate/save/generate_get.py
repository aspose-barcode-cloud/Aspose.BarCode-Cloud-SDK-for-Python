import os
from aspose_barcode_cloud import (
    ApiClient,
    GenerateApi,
    BarcodeImageFormat,
    BarcodeImageParams,
    Code128Params,
    Code128EncodeMode,
    EncodeBarcodeType,
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
    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    api = GenerateApi(api_client=api_client)

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "code128.jpeg"))

    response = api.generate(
        EncodeBarcodeType.CODE128,
        "Aspose.BarCode.Cloud",
        barcode_image_params=BarcodeImageParams(image_format=BarcodeImageFormat.PNG),
        code128_params=Code128Params(code128_encode_mode=Code128EncodeMode.AUTO),
    )

    with open(file_name, "wb") as f:
        f.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
