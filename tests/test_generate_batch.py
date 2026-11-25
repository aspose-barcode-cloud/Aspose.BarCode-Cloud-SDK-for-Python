import io
import tarfile
import zipfile

import pytest

from aspose_barcode_cloud import (
    ApiClient,
    GenerateApi,
    BatchGenerateRequest,
    BatchGenerateItem,
    GenerateParams,
    EncodeData,
)
from .load_configuration import TEST_CONFIGURATION


@pytest.mark.parametrize("archive_format", ["Zip", "Tar", "TarGzip"])
def test_generate_batch_archive(archive_format):
    request = BatchGenerateRequest(
        archive_format=archive_format,
        items=[
            BatchGenerateItem(
                file_name="qr.png",
                generation=GenerateParams(barcode_type="QR", encode_data=EncodeData(data="Batch example")),
            )
        ],
    )
    response = GenerateApi(ApiClient(TEST_CONFIGURATION)).generate_batch(request)
    try:
        data = response.data
    finally:
        response.close()
        response.release_conn()
    if archive_format == "Zip":
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            assert archive.namelist() == ["qr.png"]
            image = archive.read("qr.png")
    else:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as archive:
            assert archive.getnames() == ["qr.png"]
            image = archive.extractfile("qr.png").read()
    assert image.startswith(b"\x89PNG\r\n\x1a\n")
