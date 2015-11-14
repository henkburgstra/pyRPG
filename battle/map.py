

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

        self.grid = Grid(self.width, self.height, TILESIZE, GRIDLAYER)
        self.infob = False  # info boolean
        self.infol = []     # info list

    @staticmethod
    def add_object(obj, object_type):
        object_type.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    @staticmethod
    def del_object(obj, object_type):
        object_type.remove(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def show_grid(self):
        if self.grid.show:
            self.grid.show = False
            self.group.remove(self.grid)
        else:
            self.grid.show = True
            self.group.add(self.grid)

    def show_info(self, status):
        if status == 1:     # active, with key press
            if self.infob:
                self.infob = False
                self.group.remove(self.infol)
                self.infol = []
            else:
                self.infob = True
                self.fill_info_list()
                self.group.add(self.infol)
        if status == 0:     # passive, already on
            if self.infob:
                self.group.remove(self.infol)
                self.infol = []
                self.fill_info_list()
                self.group.add(self.infol)

    def fill_info_list(self):
        for obj in self.start_pos:
            self.infol.append(Info(obj, 'start', GRIDLAYER))
        for obj in self.heroes:
            self.infol.append(Info(obj, 'hero', GRIDLAYER))
        for obj in self.trees:
            self.infol.append(Info(obj, 'tree', GRIDLAYER))
