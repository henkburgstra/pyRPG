
import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0
DARKGRAY = 96, 96, 96
GREEN = 32, 128, 32
BLUE = 0, 0, 255
PURPLE = 255, 0, 255

# todo, magic numbers opruimen


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


class MoveRange(pygame.sprite.Sprite):
    def __init__(self, size, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((size, size))
        # self.circle1 = pygame.Surface((size, size))
        # self.circle2 = pygame.Surface((size, size))
        self.image.fill(BLACK)
        # self.circle1.fill(BLUE)
        # self.circle2.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # self.circle1.set_colorkey(BLUE)
        # self.circle2.set_colorkey(BLACK)
        # pygame.draw.circle(self.circle1, BLACK, (size // 2, size // 2), size // 2, 0)
        pygame.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2, 2)
        # self.circle1.set_alpha(48)
        self.image = self.image.convert()
        # self.circle1 = self.circle1.convert()
        # self.circle2 = self.circle2.convert()
        # self.image.blit(self.circle1, (0, 0))
        # self.image.blit(self.circle2, (0, 0))
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
    def __init__(self, rect, rect_type, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect_type = rect_type
        pygame.draw.rect(self.image, self._color, (0, 0, rect.width, rect.height), 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = rect.topleft

    @property
    def _color(self):
        if self.rect_type == 'start':
            return GREEN
        if self.rect_type == 'hero':
            return BLUE
        if self.rect_type == 'tree':
            return PURPLE
