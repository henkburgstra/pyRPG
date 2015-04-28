
class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value