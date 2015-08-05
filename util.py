
import json


class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)
