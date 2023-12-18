import json
from collections import namedtuple
from types import SimpleNamespace


def from_json(json_str: str, my_class):
    return json.loads(json_str, object_hook=lambda d: my_class(**d))


def json_load(json_str: str):
    return json.loads(json_str)


def to_json(obj):
    return json.dumps(obj, indent=2)


class JSONObject:
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, dict):
            return JSONObject(value)
        elif isinstance(value, list):
            return [self._wrap(item) for item in value]
        else:
            return value


def json_to_object(json_data):
    return JSONObject(json.loads(json_data))
