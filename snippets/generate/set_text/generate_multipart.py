import os

from aspose_barcode_cloud import (
    ApiClient,
    Code128Params,
    Code128EncodeMode,
    EncodeBarcodeType,
    EncodeDataType,
    Configuration,
)
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
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "Code128.png"))

    api_client = ApiClient(configuration=make_configuration())
    generate_api = GenerateApi(api_client=api_client)

    response = generate_api.generate_multipart(
        EncodeBarcodeType.CODE128,
        "4173706F73652E426172436F64652E436C6F7564",
        data_type=EncodeDataType.HEXBYTES,
        code128_params=Code128Params(code128_encode_mode=Code128EncodeMode.AUTO),
    )

    with open(file_name, "wb") as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
