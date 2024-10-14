import json
import pickle
from typing import Any

import pytest


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
