

import pygame
import pytmx
import pyscroll
import pyscroll.data

from battle.drawings import Grid
from battle.drawings import Info

GRIDLAYER = 4
TILESIZE = 32


class Map(object):
    def __init__(self, map_path, layer, window_width, window_height):

        tmx_data = pytmx.load_pygame(map_path)

        self.width = int(tmx_data.width * tmx_data.tilewidth)
        self.height = int(tmx_data.height * tmx_data.tileheight)

        self.start_pos = []     # start pos is maar één rect, maar moet in een list staan ivm updaten
        self.trees = []         # een lijst van rects van alle bomen
        self.waters = []
        self.heroes = []
        self.obstacles = []
        self.low_obst = []

        for rect in tmx_data.get_layer_by_name("trees"):
            self.add_rect_to_list(rect, self.trees)   # vul die lijst van rects van alle bomen
            self.add_rect_to_list(rect, self.obstacles)

        for rect in tmx_data.get_layer_by_name("water"):
            self.add_rect_to_list(rect, self.waters)
            self.add_rect_to_list(rect, self.low_obst)

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)

        self._grid = Grid(self.width, self.height, TILESIZE, GRIDLAYER)
        self._infol = []     # info list, list van classes zoals grid
        self._infob = False  # info boolean

    @staticmethod
    def add_rect_to_list(rect, alist):
        alist.append(pygame.Rect(rect.x, rect.y, rect.width, rect.height))

    @staticmethod
    def del_rect_from_list(rect, alist):
        alist.remove(pygame.Rect(rect.x, rect.y, rect.width, rect.height))

    def add_sprite_to_map_layer_group(self, sprite):
        self.group.add(sprite)

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
        for rect in self.start_pos:
            self._infol.append(Info(rect, 'start', GRIDLAYER))
        for rect in self.heroes:
            self._infol.append(Info(rect, 'hero', GRIDLAYER))
        for rect in self.trees:
            self._infol.append(Info(rect, 'tree', GRIDLAYER))
        for rect in self.waters:
            self._infol.append(Info(rect, 'water', GRIDLAYER))
