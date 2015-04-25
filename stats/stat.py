
import output


class Stat(object):
    def __init__(self, name, raw, maximum, upgrade, quantity):
        self.NAME = name
        self.RAW = raw
        self.MAXIMUM = maximum      # maximum mogelijk, bijv 30
        self.UPGRADE = upgrade      # upgrade forumule constante
        self._quantity = quantity   # standaard hoeveelheid op te waarderen stat (tot bijv 30)
        self._extra = 0             # wat geeft gear voor pos/neg extra
        self._total = quantity      # quantity + extra
        self._current = quantity    # gaat af wanneer er bijv schade is (sta, edu, lev)
        self._output = output.Output()

    def show_stat(self):
        """ Deze is voor hero stats"""
        self._output.stat(self.NAME, self._quantity, self._extra)

    def get_extra(self):
        return self._extra

    def set_extra(self, extra):
        self._extra = extra

    extra = property(get_extra, set_extra)

    def get_total(self):
        return self._total

    def set_total(self, total):
        self._total = total

    total = property(get_total, set_total)

    @property
    def quantity(self):
        return self._quantity

    @property
    def current(self):
        return self._current
