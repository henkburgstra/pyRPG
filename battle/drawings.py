
import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0
DARKGRAY = 96, 96, 96
GREEN = 32, 128, 32
BLUE = 0, 0, 255
PURPLE = 255, 0, 255


class Pointer(pygame.sprite.Sprite):
    def __init__(self, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((65, 65))   # 64 bij 64 + 1, anders niet helemaal gecentreerd
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, WHITE, (32, 32), 32, 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect.center = position


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
        pygame.draw.rect(self.image, self._color, (0, 0, obj.width, obj.height), 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = obj.topleft

    @property
    def _color(self):
        if self.object_type == 'start':
            return GREEN
        if self.object_type == 'hero':
            return BLUE
        if self.object_type == 'tree':
            return PURPLE
