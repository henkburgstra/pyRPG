
import pygame

WHITE = 255, 255, 255
BLACK = 0, 0, 0
DARKGRAY = 96, 96, 96
GREEN = 32, 128, 32
BLUE = 0, 0, 255
PURPLE = 255, 0, 255

# todo, magic numbers opruimen
# todo, transparant moverange weer aanzetten wanneer mogelijk


class Button(pygame.sprite.Sprite):
    def __init__(self, position, caption):
        pygame.sprite.Sprite.__init__(self)

        self._width = 40
        self._height = 40
        self._position = position
        self._bgcolor = BLACK
        self._visible = True

        self.image = pygame.Surface((self._width, self._height))
        self.rect = self.image.get_rect()

        self._font = pygame.font.SysFont('sans', 14)
        self._caption = self._font.render(caption, True, WHITE)
        self._caprect = self._caption.get_rect()
        self._caprect.center = self.rect.width / 2, self.rect.height / 2

        self._update()

    def handle_event(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                pipo = list(pygame.key.get_pressed())
                pipo[pygame.K_UP] = pygame.K_UP
                return pipo

    def draw(self, surface):
        if self._visible:
            surface.blit(self.image, self._position)

    def _update(self):
        self.image.fill(self.bgcolor)
        pygame.draw.rect(self.image, WHITE, (0, 0, self._width, self._height), 1)
        self.image.blit(self._caption, self._caprect)
        self.image = self.image.convert()

    @property
    def bgcolor(self):
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value):
        self._bgcolor = value
        self._update()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
        self._update()


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
        pygame.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2, 4)
        self.image.set_alpha(64)
        self.image = self.image.convert()
        # self.circle1 = self.circle1.convert()
        # self.circle2 = self.circle2.convert()
        # self.image.blit(self.circle1, (0, 0))
        # self.image.blit(self.circle2, (0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

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
        if self.rect_type == 'water':
            return BLUE
