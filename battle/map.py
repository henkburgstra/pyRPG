

import pygame
import pytmx
import pyscroll
import pyscroll.data

from battle.drawings import MoveRange
from battle.drawings import Grid
from battle.drawings import Info

MOVERANGELAYER = 1
GRIDLAYER = 5
MOVERANGESIZE = 400
TILESIZE = 32


class Map(object):
    def __init__(self, map_path, layer, window_width, window_height):

        tmx_data = pytmx.load_pygame(map_path)

        self._width = int(tmx_data.width * tmx_data.tilewidth)
        self._height = int(tmx_data.height * tmx_data.tileheight)

        self.start_pos = []
        self.trees = []
        self.heroes = []
        self.obstacles = []
        for obj in tmx_data.objects:
            self.add_object(obj, self.trees)
            self.add_object(obj, self.obstacles)

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)

        self._moverange = MoveRange(MOVERANGESIZE, MOVERANGELAYER)
        self.group.add(self._moverange)

        self._grid = Grid(self._width, self._height, TILESIZE, GRIDLAYER)
        self._infob = False  # info boolean
        self._infol = []     # info list

    @staticmethod
    def add_object(obj, object_type):
        object_type.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    @staticmethod
    def del_object(obj, object_type):
        object_type.remove(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def show_moverange(self, position):
        self._moverange.update(position)

    def show_grid(self):
        if self._grid.show:
            self._grid.show = False
            self.group.remove(self._grid)
        else:
            self._grid.show = True
            self.group.add(self._grid)

    def show_info(self, status):
        if status == 1:     # active, with key press
            if self._infob:
                self._infob = False
                self.group.remove(self._infol)
                self._infol = []
            else:
                self._infob = True
                self._fill_info_list()
                self.group.add(self._infol)
        if status == 0:     # passive, already on
            if self._infob:
                self.group.remove(self._infol)
                self._infol = []
                self._fill_info_list()
                self.group.add(self._infol)

    def _fill_info_list(self):
        for obj in self.start_pos:
            self._infol.append(Info(obj, 'start', GRIDLAYER))
        for obj in self.heroes:
            self._infol.append(Info(obj, 'hero', GRIDLAYER))
        for obj in self.trees:
            self._infol.append(Info(obj, 'tree', GRIDLAYER))
