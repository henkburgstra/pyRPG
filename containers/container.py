

class Container(object):
    def __init__(self, name):
        self.NAME = name
        self._inside = {}

    def __len__(self):
        return len(self._inside)

    def __iter__(self):
        return iter(self._inside.values())

    def __contains__(self, key):
        return key.RAW in self._inside

    def __getitem__(self, key):
        return self._inside[key]

    def __setitem__(self, key, value):
        self._inside[key.RAW] = value

    def __delitem__(self, key):
        del self._inside[key.RAW]

    # def __getattr__(self, item):
    #     return self[item]