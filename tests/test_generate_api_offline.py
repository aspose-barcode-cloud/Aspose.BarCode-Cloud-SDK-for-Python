# coding: utf-8

"""Offline request-building coverage for ``GenerateApi``.

Complements ``test_models_coverage.py`` / ``test_api_client_offline.py``: drives every generated
``GenerateApi`` method through ``ApiClient`` against a mocked ``RESTClientObject`` (fixtures
in ``conftest.py``, the same pattern as ``test_headers.py``), so the request-building code in
``aspose_barcode_cloud/api/generate_api.py`` stays covered without a single live API call.
"""

import pytest

from aspose_barcode_cloud.api.generate_api import GenerateApi
from aspose_barcode_cloud.models import (
    BarcodeImageParams,
    EncodeBarcodeType,
    EncodeDataType,
    GenerateParams,
    Pdf417Params,
    QrParams,
)

from .model_factories import (
    _barcode_image_params,
    _code128_params,
    _make_model,
    _pdf417_params,
    _qr_params,
)


def test_generate_offline_builds_get_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = GenerateApi(api_client)

    response = api.generate(
        EncodeBarcodeType.QR,
        "Sample",
        data_type=EncodeDataType.STRINGDATA,
        barcode_image_params=_barcode_image_params(1),
        qr_params=_qr_params(1),
        code128_params=_code128_params(1),
        pdf417_params=_pdf417_params(1),
    )

    assert response is rest_client.GET.return_value
    assert rest_client.GET.call_count == 1
    url = rest_client.GET.call_args[0][0]
    assert url.endswith("/barcode/generate/QR")

    query = dict(rest_client.GET.call_args[1]["query_params"])
    assert query["data"] == "Sample"
    assert query["dataType"] == EncodeDataType.STRINGDATA
    for flattened_param in (
        "imageFormat",
        "textLocation",
        "foregroundColor",
        "backgroundColor",
        "units",
        "resolution",
        "imageHeight",
        "imageWidth",
        "rotationAngle",
        "qrEncodeMode",
        "qrErrorLevel",
        "qrVersion",
        "qrECIEncoding",
        "qrAspectRatio",
        "microQRVersion",
        "rectMicroQrVersion",
        "code128EncodeMode",
        "pdf417EncodeMode",
        "pdf417ErrorLevel",
        "pdf417Truncate",
        "pdf417Columns",
        "pdf417Rows",
        "pdf417AspectRatio",
        "pdf417ECIEncoding",
        "pdf417IsReaderInitialization",
        "pdf417MacroCharacters",
        "pdf417IsLinked",
        "pdf417IsCode128Emulation",
    ):
        assert flattened_param in query, flattened_param

    headers = rest_client.GET.call_args[1]["headers"]
    assert headers["Authorization"] == "Bearer fake-token"
    assert headers["Cookie"] == "session=fake-cookie"


def test_generate_offline_async_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = GenerateApi(api_client)

    thread = api.generate_with_http_info(EncodeBarcodeType.CODE128, "Sample", async_req=True)
    result, status, headers = thread.get()

    assert result is rest_client.GET.return_value
    assert status == 200
    assert headers["Content-Type"] == "application/json"
    assert rest_client.GET.call_count == 1


def test_generate_offline_rejects_missing_and_unknown_params(api_client):
    # type: (ApiClient) -> None
    api = GenerateApi(api_client)

    with pytest.raises(ValueError, match="barcode_type"):
        api.generate(None, "Sample")
    with pytest.raises(ValueError, match="'data'"):
        api.generate(EncodeBarcodeType.QR, None)
    with pytest.raises(TypeError, match="bogus"):
        api.generate(EncodeBarcodeType.QR, "Sample", bogus="value")


def _params_with_raw_attribute(model_type, attribute, value):
    # type: (type, str, float) -> object
    """Bypass the model setter validation to exercise the API-side range guards."""
    instance = model_type()
    setattr(instance, "_" + attribute, value)
    return instance


@pytest.mark.parametrize(
    "group, model_type, attribute, value",
    [
        ("barcode_image_params", BarcodeImageParams, "resolution", 100001.0),
        ("barcode_image_params", BarcodeImageParams, "resolution", 0.5),
        ("qr_params", QrParams, "qr_aspect_ratio", 1.5),
        ("qr_params", QrParams, "qr_aspect_ratio", 0.0001),
        ("pdf417_params", Pdf417Params, "pdf417_columns", 31),
        ("pdf417_params", Pdf417Params, "pdf417_columns", -1),
        ("pdf417_params", Pdf417Params, "pdf417_rows", 91),
        ("pdf417_params", Pdf417Params, "pdf417_rows", -1),
        ("pdf417_params", Pdf417Params, "pdf417_aspect_ratio", 10.5),
        ("pdf417_params", Pdf417Params, "pdf417_aspect_ratio", 1.5),
    ],
)
def test_generate_offline_rejects_out_of_range_params(api_client, group, model_type, attribute, value):
    # type: (ApiClient, str, type, str, float) -> None
    api = GenerateApi(api_client)
    grouped_params = {group: _params_with_raw_attribute(model_type, attribute, value)}

    with pytest.raises(ValueError, match=attribute):
        api.generate(EncodeBarcodeType.QR, "Sample", **grouped_params)
    with pytest.raises(ValueError, match=attribute):
        api.generate_multipart(EncodeBarcodeType.QR, "Sample", **grouped_params)


def test_generate_body_offline_builds_post_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = GenerateApi(api_client)

    response = api.generate_body(_make_model(GenerateParams, 1))

    assert response is rest_client.POST.return_value
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/generate-body")
    body = rest_client.POST.call_args[1]["body"]
    assert body["barcodeType"]
    assert "encodeData" in body

    with pytest.raises(ValueError, match="generate_params"):
        api.generate_body(None)


def test_generate_multipart_offline_builds_form_request(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    api = GenerateApi(api_client)

    response = api.generate_multipart(
        EncodeBarcodeType.QR,
        "Sample",
        data_type=EncodeDataType.STRINGDATA,
        barcode_image_params=_barcode_image_params(1),
        qr_params=_qr_params(1),
        code128_params=_code128_params(1),
        pdf417_params=_pdf417_params(1),
    )

    assert response is rest_client.POST.return_value
    assert rest_client.POST.call_count == 1
    url = rest_client.POST.call_args[0][0]
    assert url.endswith("/barcode/generate-multipart")
    form = dict(rest_client.POST.call_args[1]["post_params"])
    assert form["barcodeType"] == EncodeBarcodeType.QR
    assert form["data"] == "Sample"
    assert "qrEncodeMode" in form
    assert "pdf417EncodeMode" in form

    with pytest.raises(ValueError, match="barcode_type"):
        api.generate_multipart(None, "Sample")
    with pytest.raises(ValueError, match="'data'"):
        api.generate_multipart(EncodeBarcodeType.QR, None)
