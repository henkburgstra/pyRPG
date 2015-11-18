
import pygame

MOVESPEED1 = 1
MOVESPEED2 = 2
MOVESPEED3 = 4
MOVESPEED4 = 8

# todo, magic numbers opruimen
# todo, vervang direction met enum states?
# todo, handle movement uit deze class
# todo, zie demo van pyscroll betreffende movement ed



# Hero extends the pygame.sprite.Sprite class
class Hero(pygame.sprite.Sprite):
    # In the main program, we will pass a spritesheet and x-y values to the constructor
    def __init__(self, position, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        self._west_states = {0:  (32, 32, 32, 32), 1: (0, 32, 32, 32), 2: (32, 32, 32, 32), 3: (64, 32, 32, 32)}
        self._east_states = {0:  (32, 64, 32, 32), 1: (0, 64, 32, 32), 2: (32, 64, 32, 32), 3: (64, 64, 32, 32)}
        self._north_states = {0: (32, 96, 32, 32), 1: (0, 96, 32, 32), 2: (32, 96, 32, 32), 3: (64, 96, 32, 32)}
        self._south_states = {0: (32,  0, 32, 32), 1: (0,  0, 32, 32), 2: (32,  0, 32, 32), 3: (64,  0, 32, 32)}

        # Assign the spritesheet to self._full_sprite
        self._full_sprite = pygame.image.load(spritesheet)
        # 'Clip' the sheet so that only one frame is displayed (the first frame of _south_states)
        self._full_sprite.set_clip(pygame.Rect(self._north_states[0]))

        # Create a rect to animate around the screen
        self.image = self._full_sprite.subsurface(self._full_sprite.get_clip())
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Assign the position parameter value to the topleft x-y values of the rect
        self.rect.topleft = position

        self._fallback_pos = None
        self._direction = 'north'
        self._step_count = 0
        self._step_animation = 0
        self._step_delay = 0

        self._press_up = 0
        self._press_down = 0
        self._press_left = 0
        self._press_right = 0

        self._movespeed = MOVESPEED2

    def set_speed(self, keys):

        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
            self._movespeed = MOVESPEED4
        elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self._movespeed = MOVESPEED3
        elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            self._movespeed = MOVESPEED1
        elif not keys[pygame.K_LSHIFT] and not keys[pygame.K_RSHIFT] and \
                not keys[pygame.K_LCTRL] and not keys[pygame.K_RCTRL]:
            self._movespeed = MOVESPEED2

    def set_fallback(self):
        self._fallback_pos = self.rect.topleft

    def fallback(self):
        self.rect.topleft = self._fallback_pos

    def handle_movement(self, keys):

        if keys[pygame.K_UP]:
            self._press_up += 1
        else:
            self._press_up = 0
        if keys[pygame.K_DOWN]:
            self._press_down += 1
        else:
            self._press_down = 0
        if keys[pygame.K_LEFT]:
            self._press_left += 1
        else:
            self._press_left = 0
        if keys[pygame.K_RIGHT]:
            self._press_right += 1
        else:
            self._press_right = 0

        # Als hij nog geen stappen heeft gezet en hij kijkt naar een andere kant dan je drukt, stel een delay in.
        if self._step_count == 0:
            if (keys[pygame.K_UP] and self._direction != 'north') or \
               (keys[pygame.K_DOWN] and self._direction != 'south') or \
               (keys[pygame.K_LEFT] and self._direction != 'west') or \
               (keys[pygame.K_RIGHT] and self._direction != 'east'):
                    self._step_delay = 7

        # Als je meerdere knoppen indrukt, ga dan naar de richting van de laatst ingedrukte knop.
        if self._press_up > 0 and ((self._press_up <= self._press_down and self._press_down > 0) or
                                   (self._press_up <= self._press_left and self._press_left > 0) or
                                   (self._press_up <= self._press_right and self._press_right > 0)):
            self._direction = 'north'
        elif self._press_down > 0 and ((self._press_down <= self._press_up and self._press_up > 0) or
                                       (self._press_down <= self._press_left and self._press_left > 0) or
                                       (self._press_down <= self._press_right and self._press_right > 0)):
            self._direction = 'south'
        elif self._press_left > 0 and ((self._press_left <= self._press_up and self._press_up > 0) or
                                       (self._press_left <= self._press_down and self._press_down > 0) or
                                       (self._press_left <= self._press_right and self._press_right > 0)):
            self._direction = 'west'
        elif self._press_right > 0 and ((self._press_right <= self._press_up and self._press_up > 0) or
                                        (self._press_right <= self._press_down and self._press_down > 0) or
                                        (self._press_right <= self._press_left and self._press_left > 0)):
            self._direction = 'east'
        # Of ga in de richting van de enige knop die je indrukt.
        elif self._press_up > 0:
            self._direction = 'north'
        elif self._press_down > 0:
            self._direction = 'south'
        elif self._press_left > 0:
            self._direction = 'west'
        elif self._press_right > 0:
            self._direction = 'east'

        # Als je helemaal geen knoppen indrukt, ga dan in de stilstand pose.
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and \
           not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self._update(False)

        # Als je een knop indrukt, en er is geen delay, beweeg dan in die richting.
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or \
           keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if self._step_delay > 0:
                self._step_delay -= 1
            else:
                self._update(True)

    def _update(self, moving):
        if moving:
            if self._direction == 'west':
                self._clip(self._west_states)
                self.rect.x -= self._movespeed
            if self._direction == 'east':
                self._clip(self._east_states)
                self.rect.x += self._movespeed
            if self._direction == 'north':
                self._clip(self._north_states)
                self.rect.y -= self._movespeed
            if self._direction == 'south':
                self._clip(self._south_states)
                self.rect.y += self._movespeed

        if not moving:
            if self._direction == 'west':
                self._clip(self._west_states[0])
            if self._direction == 'east':
                self._clip(self._east_states[0])
            if self._direction == 'north':
                self._clip(self._north_states[0])
            if self._direction == 'south':
                self._clip(self._south_states[0])

        # Update the image for each pass
        self.image = self._full_sprite.subsurface(self._full_sprite.get_clip())

    def _clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self._full_sprite.set_clip(pygame.Rect(self._get_frame(clipped_rect)))
        else:
            self._step_count = 0
            self._step_animation = 0
            self._step_delay = 0
            self._full_sprite.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def _get_frame(self, frame_set):
        self._step_count += 1
        if self._step_count % (24 / self._movespeed) == 1:  # 24 is deelbaar door alle movespeeds
            self._step_animation += 1
            if self._step_animation > 3:
                self._step_animation = 0
        return frame_set[self._step_animation]

    def align_to_grid(self, tile_size):
        self.rect.topleft = (round(self.rect.x / tile_size) * tile_size, round(self.rect.y / tile_size) * tile_size)

    def move_back(self):
        if self._direction == 'west':
            self.rect.x += 1
        if self._direction == 'east':
            self.rect.x -= 1
        if self._direction == 'north':
            self.rect.y += 1
        if self._direction == 'south':
            self.rect.y -= 1

    def move_side(self, obj):
        if self._direction in ('west', 'east'):
            if abs(self.rect.top - obj.bottom) < self.rect.h / 2:  # < 16
                self.rect.y += self._movespeed
            if abs(self.rect.bottom - obj.top) < self.rect.h / 2:
                self.rect.y -= self._movespeed
        if self._direction in ('north', 'south'):
            if abs(self.rect.left - obj.right) < self.rect.w / 2:
                self.rect.x += self._movespeed
            if abs(self.rect.right - obj.left) < self.rect.w / 2:
                self.rect.x -= self._movespeed
