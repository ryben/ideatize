import json
from collections import namedtuple
from types import SimpleNamespace


def from_json(json_str, to_class):
    json_data = json.loads(json_str)

    def _dict_to_dataclass(cls, data):
        if isinstance(data, dict):
            field_types = {f.name: f.type for f in cls.__dataclass_fields__.values()}
            return cls(**{k: _dict_to_dataclass(field_types[k], v) for k, v in data.items()})
        elif isinstance(data, list):
            return [_dict_to_dataclass(cls.__args__[0], item) for item in data]
        else:
            return data

    return _dict_to_dataclass(to_class, json_data)


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
