# coding: utf-8

"""Shared pytest fixtures for the offline request-building tests.

Provides the mocked ``RESTClientObject`` transport and an ``ApiClient`` wired to it
(the same pattern as ``test_headers.py``), so the ``test_*_offline.py`` files can drive
every generated API method without a single live API call.
"""

import json
import typing
from unittest import mock

import pytest

from aspose_barcode_cloud.api_client import ApiClient
from aspose_barcode_cloud.configuration import Configuration
from aspose_barcode_cloud.rest import RESTClientObject

FILE_URL: typing.Final = "https://barcode.example/image.png"

BARCODES_JSON: typing.Final = json.dumps(
    {"barcodes": [{"barcodeValue": "Test", "type": "QR", "region": [{"x": 1, "y": 2}], "checksum": "123"}]}
).encode("utf-8")


class _FakeRestResponse:
    """Explicit stand-in for ``rest.RESTResponse`` returned by the mocked transport."""

    def __init__(self, data=BARCODES_JSON, headers=None):
        # type: (bytes, typing.Optional[typing.Dict[str, str]]) -> None
        self.status = 200
        self.reason = "OK"
        self.data = data
        self._headers = headers if headers is not None else {"Content-Type": "application/json"}

    def getheaders(self):
        # type: () -> typing.Dict[str, str]
        return self._headers

    def getheader(self, name, default=None):
        # type: (str, typing.Optional[str]) -> typing.Optional[str]
        return self._headers.get(name, default)


@pytest.fixture()
def rest_client():
    # type: () -> mock.Mock
    client = mock.Mock(spec_set=RESTClientObject)
    for method in ("GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"):
        getattr(client, method).return_value = _FakeRestResponse()
    return client


@pytest.fixture()
def api_client(rest_client):
    # type: (mock.Mock) -> ApiClient
    client = ApiClient(
        Configuration(access_token="fake-token", host="http://localhost"),
        cookie="session=fake-cookie",
    )
    client.rest_client = rest_client
    return client
