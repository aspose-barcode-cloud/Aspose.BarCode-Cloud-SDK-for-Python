import os
import unittest
import uuid

from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    EncodeDataType,
    EncodeData,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
)
from aspose_barcode_cloud.api.generate_api import GenerateApi
from .load_configuration import TEST_CONFIGURATION


class TestGenerateApi(unittest.TestCase):
    """GenerateApi unit tests"""

    @classmethod
    def setUpClass(cls):

        cls.api_client = ApiClient(configuration=TEST_CONFIGURATION)

        # noinspection PyUnresolvedReferences
        cls.api = GenerateApi(api_client=cls.api_client)

    def test_barcode_generate_barcode_type_get(self):
        """Test case for generate

        Generate barcode.
        """
        response = self.api.generate(EncodeBarcodeType.CODE128, "Hello!")

        content_length = int(response.headers["content-length"])
        self.assertGreater(content_length, 0, "content_length=%s" % content_length)
        self.assertEqual("image/png", response.headers["content-type"])

    def test_barcode_generate_body_post(self):
        """Test case for generate_body

        Generate barcode from params in body
        """
        generator_params = GenerateParams(
            EncodeBarcodeType.QR,
            EncodeData(EncodeDataType.BASE64BYTES, "VGVzdA=="),
            BarcodeImageParams(BarcodeImageFormat.JPEG),
        )

        response = self.api.generate_body(generator_params)

        content_length = int(response.headers["content-length"])
        self.assertGreater(content_length, 0, "content_length=%s" % content_length)
        self.assertEqual("image/jpeg", response.headers["content-type"])

    def test_barcode_generate_multipart_post(self):
        """Test case for generate_multipart

        Generate barcode from params in form
        """

        response = self.api.generate_multipart(
            EncodeBarcodeType.QR,
            "54657374",
            EncodeDataType.HEXBYTES,
            barcode_image_params=BarcodeImageParams(background_color="0xffe"),
        )

        content_length = int(response.headers["content-length"])
        self.assertGreater(content_length, 0, "content_length=%s" % content_length)
        self.assertEqual("image/png", response.headers["content-type"])
