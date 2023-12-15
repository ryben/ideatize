import json
from collections import namedtuple
from types import SimpleNamespace


def from_json(json_str: str, my_class):
    return json.loads(json_str, object_hook=lambda d: my_class(**d))


def json_load(json_str: str):
    return json.loads(json_str)


def to_json(obj):
    return json.dumps(obj, indent=2)
