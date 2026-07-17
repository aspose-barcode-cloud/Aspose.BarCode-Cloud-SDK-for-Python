import os
import unittest
import base64

from aspose_barcode_cloud import ApiClient, ScanApi, DecodeBarcodeType, ScanBase64Request
from .load_configuration import TEST_CONFIGURATION


class TestScanBarcode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ScanApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "qr_and_code128.png")
        )

    def test_barcode_scan_get(self):
        """Test case for scan

        Scan barcode from url.
        """

        response = self.api.scan(
            "https://raw.githubusercontent.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/main/testdata/qr_and_code128.png"
        )

        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)
        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)

    def test_barcode_scan_body_post(self):
        """Test case for scan_base64
        Scan barcode from an request body.
        Request body should contain data encoded with base64.
        """
        with open(self.test_filename, "rb") as f:
            image_bytes = f.read()
            f.close()

        encoded_string = base64.b64encode(image_bytes).decode()

        response = self.api.scan_base64(ScanBase64Request(file_base64=encoded_string))

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)

    def test_barcode_scan_multipart_post(self):
        """Test case for scan_multipart

        Recognition of a barcode from file with parameters in form.
        """
        with open(self.test_filename, "rb") as f:
            response = self.api.scan_multipart(f)

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)
