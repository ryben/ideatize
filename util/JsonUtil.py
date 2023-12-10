import json
from types import SimpleNamespace


def from_json(json_str: str):
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
