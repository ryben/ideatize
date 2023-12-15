import json
from types import SimpleNamespace


def from_json(json_str: str, my_class):
    return json.loads(json_str, object_hook=lambda d: my_class(**d))
