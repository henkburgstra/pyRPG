
class DotDict(dict):
    """dot.notation access to dictionary attributes"""
    def __getattr__(self, item):
        return self[item]
