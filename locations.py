
class Place(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def connect(self, north=None, south=None, west=None, east=None):
        self.north = north
        if north is not None:
            north.south = self
        self.south = south
        if south:
            south.north = self
        self.west = west
        if west:
            west.east = self
        self.east = east
        if east:
            east.west = self

# field = Place("Grassy Field", "You are in a grassy field.")
# house = Place("House", "You are in a house.")
# field.connect(east=house)
# print(field.east.name)
