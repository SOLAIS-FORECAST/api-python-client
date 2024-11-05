import json
import pickle
from typing import Any

import pytest

from calibsunapi import CalibsunApiClient
from calibsunapi.token import Token


@pytest.fixture
def json_resource():
    def loader(path: str) -> dict:
        with open(path) as f:
            return json.load(f)

    return loader


@pytest.fixture
def pickle_resource():
    def loader(path: str) -> Any:
        with open(path, "rb") as f:
            return pickle.load(f)

    return loader


@pytest.fixture
def plant(json_resource):
    return json_resource("tests/resources/plant.json")


@pytest.fixture
def client():
    return CalibsunApiClient("test_id", "test_secret")


@pytest.fixture
def authentified_client():
    client = CalibsunApiClient("test_id", "test_secret")
    client._token = Token(access_token="test_token", token_type="Bearer", expires_in=3600)
    return client
