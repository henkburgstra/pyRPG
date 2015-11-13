

import pygame
import pytmx
import pyscroll
import pyscroll.data


class Map(object):
    def __init__(self, map_path, layer, window_width, window_height):

        tmx_data = pytmx.load_pygame(map_path)

        self.width = int(tmx_data.width * tmx_data.tilewidth)
        self.height = int(tmx_data.height * tmx_data.tileheight)

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


class Grid(pygame.sprite.Sprite):
    def __init__(self, map_width, map_height, tile_size, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((map_width, map_height))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        for i in range(0, map_width, tile_size):
            pygame.draw.line(self.image, (100, 100, 100), (0, i), (map_width, i))
        for i in range(0, map_height, tile_size):
            pygame.draw.line(self.image, (100, 100, 100), (i, 0), (i, map_height))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        self.show = False


class Info(pygame.sprite.Sprite):
    def __init__(self, obj, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((obj.width, obj.height))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, obj.width, obj.height), 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = obj.topleft
