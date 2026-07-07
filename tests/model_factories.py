# coding: utf-8

"""Factories building fully populated instances of the generated models and enums.

Shared between the value-object tests in ``test_models_coverage.py`` / ``test_api_client_offline.py``
and the offline request-building tests (mirrors the Java SDK's ``newModel`` helpers).
"""

import datetime
import typing

from aspose_barcode_cloud.models import (
    ApiError,
    ApiErrorResponse,
    BarcodeImageFormat,
    BarcodeImageParams,
    BarcodeResponse,
    BarcodeResponseList,
    Code128EncodeMode,
    Code128Params,
    CodeLocation,
    DecodeBarcodeType,
    ECIEncodings,
    EncodeBarcodeType,
    EncodeData,
    EncodeDataType,
    GenerateParams,
    GraphicsUnit,
    MacroCharacter,
    MicroQRVersion,
    Pdf417EncodeMode,
    Pdf417ErrorLevel,
    Pdf417Params,
    QREncodeMode,
    QRErrorLevel,
    QRVersion,
    QrParams,
    RecognitionImageKind,
    RecognitionMode,
    RecognizeBase64Request,
    RectMicroQRVersion,
    RegionPoint,
    ScanBase64Request,
)

ENUM_TYPES: typing.Final = (
    BarcodeImageFormat,
    Code128EncodeMode,
    CodeLocation,
    DecodeBarcodeType,
    ECIEncodings,
    EncodeBarcodeType,
    EncodeDataType,
    GraphicsUnit,
    MacroCharacter,
    MicroQRVersion,
    Pdf417EncodeMode,
    Pdf417ErrorLevel,
    QREncodeMode,
    QRErrorLevel,
    QRVersion,
    RecognitionImageKind,
    RecognitionMode,
    RectMicroQRVersion,
)

MODEL_TYPES: typing.Final = (
    ApiError,
    ApiErrorResponse,
    BarcodeImageParams,
    BarcodeResponse,
    BarcodeResponseList,
    Code128Params,
    EncodeData,
    GenerateParams,
    Pdf417Params,
    QrParams,
    RecognizeBase64Request,
    RegionPoint,
    ScanBase64Request,
)


def _enum_value(enum_type: type, index: int) -> str:
    """Return one of the wire string constants declared on a generated enum class."""
    constants = [value for name, value in vars(enum_type).items() if name.isupper() and isinstance(value, str)]
    assert constants, "enum {0} declares no string constants".format(enum_type.__name__)
    return constants[index % len(constants)]


def _barcode_image_params(variant: int) -> BarcodeImageParams:
    return BarcodeImageParams(
        image_format=_enum_value(BarcodeImageFormat, variant),
        text_location=_enum_value(CodeLocation, variant),
        foreground_color="Black-{0}".format(variant),
        background_color="White-{0}".format(variant),
        units=_enum_value(GraphicsUnit, variant),
        resolution=100.0 + variant,
        image_height=200.0 + variant,
        image_width=300.0 + variant,
        rotation_angle=90 + variant,
    )


def _qr_params(variant: int) -> QrParams:
    return QrParams(
        qr_encode_mode=_enum_value(QREncodeMode, variant),
        qr_error_level=_enum_value(QRErrorLevel, variant),
        qr_version=_enum_value(QRVersion, variant),
        qr_eci_encoding=_enum_value(ECIEncodings, variant),
        qr_aspect_ratio=0.75,
        micro_qr_version=_enum_value(MicroQRVersion, variant),
        rect_micro_qr_version=_enum_value(RectMicroQRVersion, variant),
    )


def _code128_params(variant: int) -> Code128Params:
    return Code128Params(code128_encode_mode=_enum_value(Code128EncodeMode, variant))


def _pdf417_params(variant: int) -> Pdf417Params:
    return Pdf417Params(
        pdf417_encode_mode=_enum_value(Pdf417EncodeMode, variant),
        pdf417_error_level=_enum_value(Pdf417ErrorLevel, variant),
        pdf417_truncate=variant == 1,
        pdf417_columns=5,
        pdf417_rows=12,
        pdf417_aspect_ratio=3.0,
        pdf417_eci_encoding=_enum_value(ECIEncodings, variant),
        pdf417_is_reader_initialization=False,
        pdf417_macro_characters=_enum_value(MacroCharacter, variant),
        pdf417_is_linked=False,
        pdf417_is_code128_emulation=False,
    )


def _encode_data(variant: int) -> EncodeData:
    return EncodeData(data="data-{0}".format(variant), data_type=_enum_value(EncodeDataType, variant))


def _region_point(variant: int) -> RegionPoint:
    return RegionPoint(x=10 + variant, y=20 + variant)


def _barcode_response(variant: int) -> BarcodeResponse:
    return BarcodeResponse(
        barcode_value="value-{0}".format(variant),
        type="QR",
        region=[_region_point(variant)],
        checksum="checksum-{0}".format(variant),
    )


def _api_error(variant: int, with_inner: bool = True) -> ApiError:
    return ApiError(
        code="code-{0}".format(variant),
        message="message-{0}".format(variant),
        description="description-{0}".format(variant),
        date_time=datetime.datetime(2026, 6, 29, 0, 0, variant),
        inner_error=_api_error(variant, with_inner=False) if with_inner else None,
    )


def _make_model(model_type: type, variant: int):
    """Build a fully populated instance of a generated model (mirrors Java ``newModel``)."""
    if model_type is ApiError:
        return _api_error(variant)
    if model_type is ApiErrorResponse:
        return ApiErrorResponse(request_id="request-{0}".format(variant), error=_api_error(variant))
    if model_type is BarcodeImageParams:
        return _barcode_image_params(variant)
    if model_type is BarcodeResponse:
        return _barcode_response(variant)
    if model_type is BarcodeResponseList:
        return BarcodeResponseList(barcodes=[_barcode_response(variant)])
    if model_type is Code128Params:
        return _code128_params(variant)
    if model_type is EncodeData:
        return _encode_data(variant)
    if model_type is GenerateParams:
        return GenerateParams(
            barcode_type=_enum_value(EncodeBarcodeType, variant),
            encode_data=_encode_data(variant),
            barcode_image_params=_barcode_image_params(variant),
            qr_params=_qr_params(variant),
            code128_params=_code128_params(variant),
            pdf417_params=_pdf417_params(variant),
        )
    if model_type is Pdf417Params:
        return _pdf417_params(variant)
    if model_type is QrParams:
        return _qr_params(variant)
    if model_type is RecognizeBase64Request:
        return RecognizeBase64Request(
            barcode_types=[_enum_value(DecodeBarcodeType, variant)],
            file_base64="file-{0}".format(variant),
            recognition_mode=_enum_value(RecognitionMode, variant),
            recognition_image_kind=_enum_value(RecognitionImageKind, variant),
        )
    if model_type is RegionPoint:
        return _region_point(variant)
    if model_type is ScanBase64Request:
        return ScanBase64Request(file_base64="file-{0}".format(variant))
    raise AssertionError("no fixture for model {0}".format(model_type.__name__))
