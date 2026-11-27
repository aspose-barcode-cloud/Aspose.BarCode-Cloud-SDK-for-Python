# coding: utf-8

"""Offline coverage for the generated models and enums.

Exercises model value-object methods and enum wire-format compatibility without
touching the network, so the generated SDK stays above the 80% line-coverage gate
regardless of which live API calls run.
"""

import json
from types import SimpleNamespace

import pytest

from .model_factories import ENUM_TYPES, MODEL_TYPES, _make_model


@pytest.mark.parametrize("enum_type", ENUM_TYPES)
def test_enum_constants_round_trip(enum_type: type, api_client) -> None:
    constants = [value for name, value in vars(enum_type).items() if name.isupper()]
    assert constants
    assert enum_type.swagger_types == {}

    for value in constants:
        assert isinstance(value, str)
        assert api_client.sanitize_for_serialization(value) == value
        response = SimpleNamespace(data=json.dumps(value).encode("utf-8"))
        assert api_client.deserialize(response, enum_type) == value
        assert api_client.deserialize(response, enum_type.__name__) == value


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
