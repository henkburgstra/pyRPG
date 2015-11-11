

import pygame
import pytmx
import pyscroll
import pyscroll.data


class Map(object):
    def __init__(self, map_path, window_width, window_height, layer):

        tmx_data = pytmx.load_pygame(map_path)

        self.obstacles = []
        for obj in tmx_data.objects:
            self.add_obstacle(obj)

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)

    def add_obstacle(self, obj):
        self.obstacles.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def del_obstacle(self, obj):
        self.obstacles.remove(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
