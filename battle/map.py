

import pygame
import pytmx
import pyscroll
import pyscroll.data


class Map(object):
    def __init__(self, map_path, window_width, window_height, layer):

        tmx_data = pytmx.load_pygame(map_path)

        self.walls = []
        for obj in tmx_data.objects:
            self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)
