import os
import unittest
import uuid
import base64

from aspose_barcode_cloud import (
    ApiClient,
    DecodeBarcodeType,
    RecognitionImageKind,
    RecognitionMode,
    RecognizeBase64Request,
    BarcodeResponse,
    BarcodeResponseList,
)
from aspose_barcode_cloud.api.recognize_api import RecognizeApi
from .load_configuration import TEST_CONFIGURATION


class TestRecognizeApi(unittest.TestCase):
    """RecognizeApi unit tests"""

    @classmethod
    def setUpClass(cls):
        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png")
        )

        cls.api_client = ApiClient(configuration=TEST_CONFIGURATION)

        # noinspection PyUnresolvedReferences
        cls.api = RecognizeApi(api_client=cls.api_client)
        cls.temp_folder_path = "BarcodeTests/%s" % uuid.uuid4()
        cls.test_put_barcode_generate_filename = "test_put_barcode_generate_file.png"

    def test_barcode_recognize_get(self):
        """Test case for recognize

        Recognize barcode from an url.
        """

        response = self.api.recognize(
            DecodeBarcodeType.QR,
            "https://raw.githubusercontent.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/main/testdata/qr_and_code128.png",
            RecognitionMode.FAST,
            RecognitionImageKind.CLEARIMAGE,
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.QR, barcode.type)
        self.assertEqual("QR text", barcode.barcode_value)

    def test_barcode_recognize_body_post(self):
        """Test case for recognize_base64

        Recognize barcode from an request body.
        Request body should contain string data encoded with base64.
        """
        with open(self.test_filename, "rb") as f:
            image_bytes = f.read()

        f.close()
        encoded_string = base64.b64encode(image_bytes).decode()
        response = self.api.recognize_base64(
            RecognizeBase64Request(
                barcode_types=[DecodeBarcodeType.PDF417],
                file_base64=encoded_string,
            )
        )

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual("Pdf417", barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)
        self.assertGreater(barcode.region[0].x, 0)
        self.assertGreater(barcode.region[0].y, 0)

    def test_barcode_recognize_multipart_post(self):
        """Test case for recognize_multipart

        Recognition of a barcode from file on server with parameters in body.
        """
        with open(self.test_filename, "rb") as f:
            response = self.api.recognize_multipart(DecodeBarcodeType.PDF417, f)

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual("Pdf417", barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)
