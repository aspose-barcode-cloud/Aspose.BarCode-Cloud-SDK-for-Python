# coding: utf-8

"""Offline coverage for ``ApiClient``.

Exercises the network-free ``ApiClient`` helpers (serialization sanitising, collection
formatting, header selection, file/post-parameter preparation), request dispatch and
response deserialization through the mocked ``RESTClientObject`` fixtures from
``conftest.py``. The network-free half mirrors the Java SDK's ``SdkCoreCoverageTest`` so
the plumbing in ``api_client.py`` stays above the 80% line-coverage gate regardless of
which live API calls run.
"""

import datetime
import io
import typing

import pytest

from aspose_barcode_cloud.api_client import ApiClient
from aspose_barcode_cloud.configuration import Configuration
from aspose_barcode_cloud.models import GenerateParams, RegionPoint
from aspose_barcode_cloud.rest import ApiException

from .conftest import _FakeRestResponse
from .model_factories import _make_model


def test_api_client_offline_helpers() -> None:
    """Exercise the network-free helpers on ``ApiClient`` (mirrors Java ``SdkCoreCoverageTest``)."""
    client = ApiClient(Configuration(access_token="fake-token"))

    client.user_agent = "unit-test"
    assert client.user_agent == "unit-test"
    client.set_default_header("X-Default", "default-value")
    assert client.default_headers["X-Default"] == "default-value"

    assert client.sanitize_for_serialization(None) is None
    assert client.sanitize_for_serialization("text") == "text"
    assert client.sanitize_for_serialization([1, 2]) == [1, 2]
    assert client.sanitize_for_serialization((1, 2)) == (1, 2)
    assert client.sanitize_for_serialization({"k": "v"}) == {"k": "v"}
    assert client.sanitize_for_serialization(datetime.date(2026, 6, 29)) == "2026-06-29"
    assert client.sanitize_for_serialization(datetime.datetime(2026, 6, 29, 1, 2, 3)).startswith("2026-06-29")

    serialized = client.sanitize_for_serialization(_make_model(GenerateParams, 1))
    assert serialized["barcodeType"]
    assert "encodeData" in serialized

    collection_formats = {"m": "multi", "c": "csv", "s": "ssv", "t": "tsv", "p": "pipes"}
    formatted = dict(
        client.parameters_to_tuples(
            {"m": ["a", "b"], "c": ["a", "b"], "s": ["a", "b"], "t": ["a", "b"], "p": ["a", "b"], "plain": "x"},
            collection_formats,
        )
    )
    assert formatted["c"] == "a,b"
    assert formatted["s"] == "a b"
    assert formatted["t"] == "a\tb"
    assert formatted["p"] == "a|b"
    assert formatted["plain"] == "x"

    assert client.select_header_accept([]) is None
    assert client.select_header_accept(["application/json"]) == "application/json"
    assert client.select_header_accept(["text/plain", "image/png"]) == "text/plain, image/png"

    assert client.select_header_content_type([]) == "application/json"
    assert client.select_header_content_type(["*/*"]) == "application/json"
    assert client.select_header_content_type(["text/plain"]) == "text/plain"

    assert client.prepare_one_file(b"raw-bytes") is not None
    assert client.prepare_one_file(io.BytesIO(b"stream-bytes")) is not None
    with pytest.raises(ApiException):
        client.prepare_one_file(12345)

    post_params = client.prepare_post_parameters([("name", "value")], {"upload": b"file-bytes"})
    assert ("name", "value") in post_params
    assert any(field == "upload" for field, _ in post_params)

    headers: typing.Dict[str, str] = {}
    querys: typing.List[typing.Tuple[str, str]] = []
    assert client.update_params_for_auth(headers, querys, None) is None


def test_api_client_request_dispatch_offline(api_client, rest_client):
    # type: (ApiClient, mock.Mock) -> None
    for method in ("GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"):
        response = api_client.request(method, "http://localhost/resource")
        assert response is getattr(rest_client, method).return_value
        assert getattr(rest_client, method).call_count == 1

    with pytest.raises(ValueError, match="http method"):
        api_client.request("TRACE", "http://localhost/resource")


class _FakeDeserializeResponse:
    """Explicit stand-in carrying a raw JSON body for ``ApiClient.deserialize``."""

    def __init__(self, data: bytes) -> None:
        self.data = data


def test_api_client_deserialize_offline() -> None:
    client = ApiClient(Configuration(access_token="fake-token"))

    assert client.deserialize(_FakeDeserializeResponse(b'"hello"'), "str") == "hello"
    assert client.deserialize(_FakeDeserializeResponse(b"123"), "int") == 123
    assert client.deserialize(_FakeDeserializeResponse(b"1.5"), "float") == 1.5
    assert client.deserialize(_FakeDeserializeResponse(b"true"), "bool") is True
    assert client.deserialize(_FakeDeserializeResponse(b'{"a": 1}'), "object") == {"a": 1}
    assert client.deserialize(_FakeDeserializeResponse(b'"2026-06-29"'), "date") == datetime.date(2026, 6, 29)
    assert client.deserialize(_FakeDeserializeResponse(b'"2026-06-29T01:02:03Z"'), "datetime").year == 2026

    region = client.deserialize(_FakeDeserializeResponse(b'{"x": 10, "y": 20}'), "RegionPoint")
    assert isinstance(region, RegionPoint)
    assert region.x == 10
    assert region.y == 20

    assert client.deserialize(_FakeDeserializeResponse(b"[1, 2, 3]"), "list[int]") == [1, 2, 3]
    assert client.deserialize(_FakeDeserializeResponse(b'{"a": 1, "b": 2}'), "dict(str, int)") == {"a": 1, "b": 2}


def test_api_client_deserialize_file_offline(api_client, tmp_path):
    # type: (ApiClient, typing.Any) -> None
    api_client.configuration.temp_folder_path = str(tmp_path)

    named = api_client.deserialize(
        _FakeRestResponse(data=b"binary", headers={"Content-Disposition": 'attachment; filename="result.png"'}),
        "file",
    )
    assert named.endswith("result.png")
    with open(named, "rb") as f:
        assert f.read() == b"binary"

    anonymous = api_client.deserialize(_FakeRestResponse(data=b"binary", headers={}), "file")
    with open(anonymous, "rb") as f:
        assert f.read() == b"binary"
