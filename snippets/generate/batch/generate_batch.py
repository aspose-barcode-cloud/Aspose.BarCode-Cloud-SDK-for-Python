import os

from aspose_barcode_cloud import (
    ApiClient,
    Configuration,
    GenerateApi,
    BatchGenerateRequest,
    BatchGenerateItem,
    GenerateParams,
    EncodeData,
)


def main():
    configuration = Configuration(access_token=os.environ["TEST_CONFIGURATION_ACCESS_TOKEN"])
    request = BatchGenerateRequest(
        archive_format="Zip",
        items=[
            BatchGenerateItem(
                file_name="qr.png",
                generation=GenerateParams(barcode_type="QR", encode_data=EncodeData(data="Batch example")),
            )
        ],
    )
    response = GenerateApi(ApiClient(configuration)).generate_batch(request)
    try:
        with open("barcodes.zip", "wb") as archive:
            archive.write(response.data)
    finally:
        response.close()
        response.release_conn()


if __name__ == "__main__":
    main()
