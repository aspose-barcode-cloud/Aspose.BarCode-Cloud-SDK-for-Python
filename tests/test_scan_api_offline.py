# coding: utf-8

"""Offline request-building coverage for ``ScanApi``.

Complements ``test_models_coverage.py`` / ``test_api_client_offline.py``: drives every generated
``ScanApi`` method through ``ApiClient`` against a mocked ``RESTClientObject`` (fixtures in
``conftest.py``, the same pattern as ``test_headers.py``), so the request-building code in
``aspose_barcode_cloud/api/scan_api.py`` stays covered without a single live API call.
"""

import pytest

from aspose_barcode_cloud.api.scan_api import ScanApi
from aspose_barcode_cloud.models import BarcodeResponseList, ScanBase64Request

from .conftest import FILE_URL


def test_scan_offline_builds_get_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = ScanApi(api_client)

    result = api.scan(FILE_URL)

    assert isinstance(result, BarcodeResponseList)
    assert rest_client.GET.call_count == 1
    query = dict(rest_client.GET.call_args[1]["query_params"])
    assert query["fileUrl"] == FILE_URL

    with pytest.raises(ValueError, match="file_url"):
        api.scan(None)
    with pytest.raises(TypeError, match="bogus"):
        api.scan(FILE_URL, bogus="value")


def test_scan_base64_offline_builds_post_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = ScanApi(api_client)

    result = api.scan_base64(ScanBase64Request(file_base64="QVFJRA=="))

    assert isinstance(result, BarcodeResponseList)
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/scan-body")
    body = rest_client.POST.call_args[1]["body"]
    assert body["fileBase64"] == "QVFJRA=="

    with pytest.raises(ValueError, match="scan_base64_request"):
        api.scan_base64(None)


def test_scan_multipart_offline_builds_form_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = ScanApi(api_client)

    result = api.scan_multipart(b"fake-image-bytes")

    assert isinstance(result, BarcodeResponseList)
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/scan-multipart")
    form = dict(rest_client.POST.call_args[1]["post_params"])
    file_name, file_bytes, mime_type = form["file"]
    assert file_bytes == b"fake-image-bytes"

    with pytest.raises(ValueError, match="'file'"):
        api.scan_multipart(None)
