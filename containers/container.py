

class Container(object):
    def __init__(self, name):
        self.NAME = name
        self.inside = {}

    def __len__(self):
        return len(self.inside)

    def __iter__(self):
        return iter(self.inside.values())

    def __contains__(self, key):
        return key.RAW in self.inside

    def __getitem__(self, key):
        return self.inside[key]

    def __setitem__(self, key, value):
        self.inside[key.RAW] = value

    def __delitem__(self, key):
        del self.inside[key.RAW]

    # def __getattr__(self, item):
    #     return self[item]