# coding: utf-8

"""Offline coverage for the ``Configuration`` accessors.

Split out of the former ``test_core_coverage.py`` (mirrors the Java SDK's
``SdkCoreCoverageTest``): exercises the network-free ``Configuration`` accessors — auth
settings, API-key prefixing, debug toggling and the file logger — so the generated SDK
stays above the 80% line-coverage gate regardless of which live API calls run.
"""

import pathlib

from aspose_barcode_cloud.configuration import Configuration


def test_configuration_offline_accessors(tmp_path: pathlib.Path) -> None:
    config = Configuration(access_token="fake-token", client_id="client-id", client_secret="client-secret")

    assert config.access_token == "fake-token"
    assert config.token_url
    assert "Bearer fake-token" in config.auth_settings()["JWT"]["value"]
    assert config.get_basic_auth_token()
    assert "Python SDK Debug Report" in config.to_debug_report()

    config.api_key["JWT"] = "secret-key"
    config.api_key_prefix["JWT"] = "Bearer"
    assert config.get_api_key_with_prefix("JWT") == "Bearer secret-key"
    config.api_key_prefix["JWT"] = None
    assert config.get_api_key_with_prefix("JWT") == "secret-key"

    config.debug = True
    assert config.debug is True
    config.debug = False
    assert config.debug is False

    assert config.logger_format
    config.logger_file = str(tmp_path / "sdk.log")
    assert config.logger_file.endswith("sdk.log")
    file_handler = config.logger_file_handler
    config.logger_file = None
    assert config.logger_file is None
    # The generated setter never closes the replaced FileHandler; close it here
    # so the test does not leak a ResourceWarning under -Werror (make cover).
    file_handler.close()
