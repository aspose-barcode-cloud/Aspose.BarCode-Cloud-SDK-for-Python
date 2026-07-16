# coding: utf-8

"""Offline coverage for the ``rest.ApiException`` hierarchy.

Split out of the former ``test_core_coverage.py`` (mirrors the Java SDK's
``SdkCoreCoverageTest``): builds ``ApiException`` both directly and from a stand-in HTTP
response without touching the network, so the exception plumbing in ``rest.py`` stays
above the 80% line-coverage gate regardless of which live API calls run.

The live counterpart lives in ``test_exception.py``, which asserts the SDK parses a real
400 error body returned by the API.
"""

from aspose_barcode_cloud.rest import ApiException


class _FakeRestResponse:
    """Explicit stand-in for the urllib3 response ``rest.ApiException`` reads from."""

    def __init__(self) -> None:
        self.status = 500
        self.reason = "Server Error"
        self.data = b'{"error": "boom"}'


def test_rest_api_exception_offline() -> None:
    plain = ApiException(status=404, reason="Not Found")
    assert plain.status == 404
    assert plain.body is None
    assert "404" in str(plain)
    assert "HTTP response body" not in str(plain)

    from_response = ApiException(http_resp=_FakeRestResponse())
    assert from_response.status == 500
    assert from_response.body == b'{"error": "boom"}'
    assert "HTTP response body" in str(from_response)
