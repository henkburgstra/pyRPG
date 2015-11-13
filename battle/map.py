

import pygame
import pytmx
import pyscroll
import pyscroll.data

WHITE = 255, 255, 255
BLACK = 0, 0, 0
DARKGRAY = 96, 96, 96
GREEN = 32, 128, 32
BLUE = 0, 0, 255
PURPLE = 255, 0, 255


class Map(object):
    def __init__(self, map_path, layer, window_width, window_height):

        tmx_data = pytmx.load_pygame(map_path)

        self.width = int(tmx_data.width * tmx_data.tilewidth)
        self.height = int(tmx_data.height * tmx_data.tileheight)

        self.start_pos = None
        self.trees = []
        self.heroes = []
        self.obstacles = []
        for obj in tmx_data.objects:
            self.add_object(obj, self.trees)
            self.add_object(obj, self.obstacles)

        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)

    @staticmethod
    def add_object(obj, object_type):
        object_type.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    @staticmethod
    def del_object(obj, object_type):
        object_type.remove(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


class Grid(pygame.sprite.Sprite):
    def __init__(self, map_width, map_height, tile_size, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((map_width, map_height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        for i in range(0, map_width, tile_size):
            pygame.draw.line(self.image, DARKGRAY, (0, i), (map_width, i))
        for i in range(0, map_height, tile_size):
            pygame.draw.line(self.image, DARKGRAY, (i, 0), (i, map_height))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        self.show = False


class Info(pygame.sprite.Sprite):
    def __init__(self, obj, object_type, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((obj.width, obj.height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.object_type = object_type
        pygame.draw.rect(self.image, self.color, (0, 0, obj.width, obj.height), 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = obj.topleft

    @property
    def color(self):
        if self.object_type == 'start':
            return GREEN
        if self.object_type == 'hero':
            return BLUE
        if self.object_type == 'tree':
            return PURPLE
