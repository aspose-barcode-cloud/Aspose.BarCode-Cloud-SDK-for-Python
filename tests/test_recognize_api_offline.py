# coding: utf-8

"""Offline request-building coverage for ``RecognizeApi``.

Complements ``test_models_coverage.py`` / ``test_api_client_offline.py``: drives every generated
``RecognizeApi`` method through ``ApiClient`` against a mocked ``RESTClientObject`` (fixtures
in ``conftest.py``, the same pattern as ``test_headers.py``), so the request-building code in
``aspose_barcode_cloud/api/recognize_api.py`` stays covered without a single live API call.
"""

import pytest

from aspose_barcode_cloud.api.recognize_api import RecognizeApi
from aspose_barcode_cloud.models import (
    BarcodeResponseList,
    DecodeBarcodeType,
    RecognitionImageKind,
    RecognitionMode,
    RecognizeBase64Request,
)

from .conftest import FILE_URL


def test_recognize_offline_builds_get_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = RecognizeApi(api_client)

    result = api.recognize(
        DecodeBarcodeType.QR,
        FILE_URL,
        recognition_mode=RecognitionMode.NORMAL,
        recognition_image_kind=RecognitionImageKind.PHOTO,
    )

    assert isinstance(result, BarcodeResponseList)
    assert result.barcodes[0].barcode_value == "Test"
    assert rest_client.GET.call_count == 1
    query = dict(rest_client.GET.call_args[1]["query_params"])
    assert query["barcodeType"] == DecodeBarcodeType.QR
    assert query["fileUrl"] == FILE_URL
    assert query["recognitionMode"] == RecognitionMode.NORMAL
    assert query["recognitionImageKind"] == RecognitionImageKind.PHOTO

    with pytest.raises(ValueError, match="barcode_type"):
        api.recognize(None, FILE_URL)
    with pytest.raises(ValueError, match="file_url"):
        api.recognize(DecodeBarcodeType.QR, None)
    with pytest.raises(TypeError, match="bogus"):
        api.recognize(DecodeBarcodeType.QR, FILE_URL, bogus="value")


def test_recognize_offline_with_http_info_returns_status_and_headers(api_client):
    # type: (ApiClient) -> None
    api = RecognizeApi(api_client)

    result, status, headers = api.recognize_with_http_info(DecodeBarcodeType.QR, FILE_URL, _return_http_data_only=False)

    assert isinstance(result, BarcodeResponseList)
    assert status == 200
    assert headers["Content-Type"] == "application/json"


def test_recognize_base64_offline_builds_post_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = RecognizeApi(api_client)
    request = RecognizeBase64Request(
        barcode_types=[DecodeBarcodeType.QR],
        file_base64="QVFJRA==",
        recognition_mode=RecognitionMode.FAST,
        recognition_image_kind=RecognitionImageKind.CLEARIMAGE,
    )

    result = api.recognize_base64(request)

    assert isinstance(result, BarcodeResponseList)
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/recognize-body")
    body = rest_client.POST.call_args[1]["body"]
    assert body["fileBase64"] == "QVFJRA=="

    with pytest.raises(ValueError, match="recognize_base64_request"):
        api.recognize_base64(None)


def test_recognize_multipart_offline_builds_form_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = RecognizeApi(api_client)

    result = api.recognize_multipart(
        DecodeBarcodeType.QR,
        b"fake-image-bytes",
        recognition_mode=RecognitionMode.EXCELLENT,
        recognition_image_kind=RecognitionImageKind.SCANNEDDOCUMENT,
    )

    assert isinstance(result, BarcodeResponseList)
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/recognize-multipart")
    form = dict(rest_client.POST.call_args[1]["post_params"])
    assert form["barcodeType"] == DecodeBarcodeType.QR
    # sanitize_for_serialization turns the FileFieldData namedtuple into a plain tuple
    file_name, file_bytes, mime_type = form["file"]
    assert file_bytes == b"fake-image-bytes"
    assert mime_type == "application/octet-stream"

    with pytest.raises(ValueError, match="barcode_type"):
        api.recognize_multipart(None, b"fake-image-bytes")
    with pytest.raises(ValueError, match="'file'"):
        api.recognize_multipart(DecodeBarcodeType.QR, None)
