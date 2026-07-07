# coding: utf-8

"""Offline coverage for the generated models and enums.

Mirrors the Java SDK's ``GeneratedModelCoverageTest``: it exercises the value-object
boilerplate (constructors, property accessors, ``to_dict`` / ``to_str`` / ``__repr__`` /
``__eq__`` / ``__ne__``) without touching the network, so the generated SDK stays above
the 80% line-coverage gate regardless of which live API calls run.
"""

import pytest

from .model_factories import ENUM_TYPES, MODEL_TYPES, _enum_value, _make_model


@pytest.mark.parametrize("enum_type", ENUM_TYPES)
def test_enum_value_objects(enum_type: type) -> None:
    first = enum_type()
    second = enum_type()

    assert first == second
    assert not first != second
    assert first != object()
    assert first.to_dict() == {}
    assert isinstance(first.to_str(), str)
    assert isinstance(repr(first), str)
    assert _enum_value(enum_type, 0)


@pytest.mark.parametrize("model_type", MODEL_TYPES)
def test_model_value_objects(model_type: type) -> None:
    first = _make_model(model_type, 1)
    same = _make_model(model_type, 1)

    assert first == same
    assert not first != same
    assert first != object()
    assert repr(first)

    assert isinstance(first.to_dict(), dict)
    assert isinstance(first.to_str(), str)

    for attribute in model_type.swagger_types:
        assert getattr(first, attribute) is not None
