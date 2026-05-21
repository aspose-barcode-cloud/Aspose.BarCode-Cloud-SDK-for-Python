# Aspose.BarCode Cloud SDK for Python

[![License](https://img.shields.io/github/license/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python)](LICENSE)
[![Python package](https://github.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/aspose-barcode-cloud/Aspose.BarCode-Cloud-SDK-for-Python/actions/workflows/python-package.yml)
[![PyPI](https://img.shields.io/pypi/v/aspose-barcode-cloud)](https://pypi.org/project/aspose-barcode-cloud/)

- API version: 4.0
- Package version: 26.5.0

## SDK and API Version Compatibility:

- SDK Version 25.1 and Later: Starting from SDK version 25.1, all subsequent versions are compatible with API Version v4.0.
- SDK Version 24.12 and Earlier: These versions are compatible with API Version v3.0.

## Demo applications

[Scan QR](https://products.aspose.app/barcode/scanqr) | [Generate Barcode](https://products.aspose.app/barcode/generate) | [Recognize Barcode](https://products.aspose.app/barcode/recognize)
:---: | :---: | :---:
[![ScanQR](https://products.aspose.app/barcode/scanqr/img/aspose_scanqr-app-48.png)](https://products.aspose.app/barcode/scanqr) | [![Generate](https://products.aspose.app/barcode/generate/img/aspose_generate-app-48.png)](https://products.aspose.app/barcode/generate) | [![Recognize](https://products.aspose.app/barcode/recognize/img/aspose_recognize-app-48.png)](https://products.aspose.app/barcode/recognize)
[**Generate Wi-Fi QR**](https://products.aspose.app/barcode/wifi-qr) | [**Embed Barcode**](https://products.aspose.app/barcode/embed) | [**Scan Barcode**](https://products.aspose.app/barcode/scan)
[![Wi-FiQR](https://products.aspose.app/barcode/embed/img/aspose_wifi-qr-app-48.png)](https://products.aspose.app/barcode/wifi-qr) | [![Embed](https://products.aspose.app/barcode/embed/img/aspose_embed-app-48.png)](https://products.aspose.app/barcode/embed) | [![Scan](https://products.aspose.app/barcode/embed/img/aspose_scan-app-48.png)](https://products.aspose.app/barcode/scan)

[Aspose.BarCode for Cloud](https://products.aspose.cloud/barcode/) is a REST API for Linear, 2D and postal barcode generation and recognition in the cloud. API recognizes and generates barcode images in a variety of formats. Barcode REST API allows to specify barcode image attributes like image width, height, border style and output image format in order to customize the generation process. Developers can also specify the barcode type and text attributes such as text location and font styles in order to suit the application requirements.

This repository contains Aspose.BarCode Cloud SDK for Python source code. This SDK allows you to work with Aspose.BarCode for Cloud REST APIs in your Python 3 applications quickly and easily.

Supported Python versions:

- Python 3.9+

To use these SDKs, you will need Client Id and Client Secret which can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/applications) (free registration in Aspose Cloud is required for this).

## How to use the SDK

The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [from PyPi](https://pypi.org/project/aspose-barcode-cloud/) (recommended).

## AI Agent Skills

This repository includes an AI-agent skill in [`skills/generate-and-scan-barcode-python/SKILL.md`](skills/generate-and-scan-barcode-python/SKILL.md). Point your coding agent to it when working with this SDK so it follows the repo workflow and SDK-specific API patterns.

## Prerequisites

To use Aspose.BarCode Cloud SDK for Python you need to register an account with [Aspose Cloud](https://www.aspose.cloud) and lookup/create Client Secret and Client Id at [Cloud Dashboard](https://dashboard.aspose.cloud/applications). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/).

## Installation

### Install aspose-barcode-cloud via pip

From the command line:

```sh
pip install aspose-barcode-cloud
```

Then import the package:

```python
import aspose_barcode_cloud
```

## Sample usage

The examples below show how you can generate and recognize Code128 barcode and save it into local file using aspose-barcode-cloud:

```python
import os
from pprint import pprint

from aspose_barcode_cloud import (
    GenerateApi,
    RecognizeApi,
    ApiClient,
    Configuration,
    EncodeBarcodeType,
    CodeLocation,
    DecodeBarcodeType,
)

config = Configuration(
    client_id="Client Id from https://dashboard.aspose.cloud/applications",
    client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
    access_token=os.environ.get("TEST_CONFIGURATION_ACCESS_TOKEN"),  # Only for testing in CI, remove this line
)

# Generate barcode
generateApi = GenerateApi(ApiClient(config))
response = generateApi.generate(EncodeBarcodeType.QR, "Example", text_location=CodeLocation.NONE)
with open("example.png", "wb") as f:
    f.write(response.data)
print("Barcode saved to file 'example.png'")

# Recognize barcode
recognizeApi = RecognizeApi(ApiClient(config))
response = recognizeApi.recognize_multipart(DecodeBarcodeType.QR, open("example.png", "rb"))
pprint(response)

```

## Requirements

- urllib3 >= 1.21.1, <2.0

## Licensing

All Aspose.BarCode for Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

## Resources

- [**Website**](https://www.aspose.cloud)
- [**Product Home**](https://products.aspose.cloud/barcode/)
- [**Documentation**](https://docs.aspose.cloud/barcode/)
- [**Free Support Forum**](https://forum.aspose.cloud/c/barcode)
- [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
- [**Blog**](https://blog.aspose.cloud/categories/aspose.barcode-cloud-product-family/)

## Documentation for API Endpoints

All URIs are relative to *<https://api.aspose.cloud/v4.0>*

Class | Method | HTTP request | Description
----- | ------ | ------------ | -----------
*GenerateApi* | [**generate**](docs/GenerateApi.md#generate) | **GET** /barcode/generate/{barcodeType} | Generate barcode using GET request with parameters in route and query string.
*GenerateApi* | [**generate_body**](docs/GenerateApi.md#generate_body) | **POST** /barcode/generate-body | Generate barcode using POST request with parameters in body in json or xml format.
*GenerateApi* | [**generate_multipart**](docs/GenerateApi.md#generate_multipart) | **POST** /barcode/generate-multipart | Generate barcode using POST request with parameters in multipart form.
*RecognizeApi* | [**recognize**](docs/RecognizeApi.md#recognize) | **GET** /barcode/recognize | Recognize barcode from file on server in the Internet using GET requests with parameter in query string. For recognizing files from your hard drive use &#x60;recognize-body&#x60; or &#x60;recognize-multipart&#x60; endpoints instead.
*RecognizeApi* | [**recognize_base64**](docs/RecognizeApi.md#recognize_base64) | **POST** /barcode/recognize-body | Recognize barcode from file in request body using POST requests with parameters in body in json or xml format.
*RecognizeApi* | [**recognize_multipart**](docs/RecognizeApi.md#recognize_multipart) | **POST** /barcode/recognize-multipart | Recognize barcode from file in request body using POST requests with parameters in multipart form.
*ScanApi* | [**scan**](docs/ScanApi.md#scan) | **GET** /barcode/scan | Scan barcode from file on server in the Internet using GET requests with parameter in query string. For scaning files from your hard drive use &#x60;scan-body&#x60; or &#x60;scan-multipart&#x60; endpoints instead.
*ScanApi* | [**scan_base64**](docs/ScanApi.md#scan_base64) | **POST** /barcode/scan-body | Scan barcode from file in request body using POST requests with parameter in body in json or xml format.
*ScanApi* | [**scan_multipart**](docs/ScanApi.md#scan_multipart) | **POST** /barcode/scan-multipart | Scan barcode from file in request body using POST requests with parameter in multipart form.

## Documentation For Models

- [ApiError](docs/ApiError.md)
- [ApiErrorResponse](docs/ApiErrorResponse.md)
- [BarcodeImageFormat](docs/BarcodeImageFormat.md)
- [BarcodeImageParams](docs/BarcodeImageParams.md)
- [BarcodeResponse](docs/BarcodeResponse.md)
- [BarcodeResponseList](docs/BarcodeResponseList.md)
- [CodeLocation](docs/CodeLocation.md)
- [DecodeBarcodeType](docs/DecodeBarcodeType.md)
- [EncodeBarcodeType](docs/EncodeBarcodeType.md)
- [EncodeData](docs/EncodeData.md)
- [EncodeDataType](docs/EncodeDataType.md)
- [GenerateParams](docs/GenerateParams.md)
- [GraphicsUnit](docs/GraphicsUnit.md)
- [RecognitionImageKind](docs/RecognitionImageKind.md)
- [RecognitionMode](docs/RecognitionMode.md)
- [RecognizeBase64Request](docs/RecognizeBase64Request.md)
- [RegionPoint](docs/RegionPoint.md)
- [ScanBase64Request](docs/ScanBase64Request.md)
