
import pygame


MOVESPEED1 = 1
MOVESPEED2 = 2
MOVESPEED3 = 4
MOVESPEED4 = 8


# Hero extends the pygame.sprite.Sprite class
class Hero(pygame.sprite.Sprite):
    # In the main program, we will pass a spritesheet and x-y values to the constructor
    def __init__(self, position, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        self.west_states = {0:  (32, 32, 32, 32), 1: (0, 32, 32, 32), 2: (32, 32, 32, 32), 3: (64, 32, 32, 32)}
        self.east_states = {0:  (32, 64, 32, 32), 1: (0, 64, 32, 32), 2: (32, 64, 32, 32), 3: (64, 64, 32, 32)}
        self.north_states = {0: (32, 96, 32, 32), 1: (0, 96, 32, 32), 2: (32, 96, 32, 32), 3: (64, 96, 32, 32)}
        self.south_states = {0: (32,  0, 32, 32), 1: (0,  0, 32, 32), 2: (32,  0, 32, 32), 3: (64,  0, 32, 32)}

        # Assign the spritesheet to self.full_sprite
        self.full_sprite = pygame.image.load(spritesheet)
        # 'Clip' the sheet so that only one frame is displayed (the first frame of south_states)
        self.full_sprite.set_clip(pygame.Rect(self.north_states[0]))

        # Create a rect to animate around the screen
        self.image = self.full_sprite.subsurface(self.full_sprite.get_clip())
        self.rect = self.image.get_rect()

        # Assign the position parameter value to the topleft x-y values of the rect
        self.rect.topleft = position

        self.direction = 'north'
        self.step_count = 0
        self.step_animation = 0
        self.step_delay = 0

        self.press_up = 0
        self.press_down = 0
        self.press_left = 0
        self.press_right = 0

        self.movespeed = MOVESPEED2

    def set_speed(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
            self.movespeed = MOVESPEED4
        elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.movespeed = MOVESPEED3
        elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            self.movespeed = MOVESPEED1
        elif not keys[pygame.K_LSHIFT] and not keys[pygame.K_RSHIFT] and \
                not keys[pygame.K_LCTRL] and not keys[pygame.K_RCTRL]:
            self.movespeed = MOVESPEED2

    def handle_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.press_up += 1
        else:
            self.press_up = 0
        if keys[pygame.K_DOWN]:
            self.press_down += 1
        else:
            self.press_down = 0
        if keys[pygame.K_LEFT]:
            self.press_left += 1
        else:
            self.press_left = 0
        if keys[pygame.K_RIGHT]:
            self.press_right += 1
        else:
            self.press_right = 0

        # Als hij nog geen stappen heeft gezet en hij kijkt naar een andere kant dan je drukt, stel een delay in.
        if self.step_count == 0:
            if (keys[pygame.K_UP] and self.direction != 'north') or \
               (keys[pygame.K_DOWN] and self.direction != 'south') or \
               (keys[pygame.K_LEFT] and self.direction != 'west') or \
               (keys[pygame.K_RIGHT] and self.direction != 'east'):
                    self.step_delay = 7

        # Als je meerdere knoppen indrukt, ga dan naar de richting van de laatst ingedrukte knop.
        if self.press_up > 0 and ((self.press_up <= self.press_down and self.press_down > 0) or
                                  (self.press_up <= self.press_left and self.press_left > 0) or
                                  (self.press_up <= self.press_right and self.press_right > 0)):
            self.direction = 'north'
        elif self.press_down > 0 and ((self.press_down <= self.press_up and self.press_up > 0) or
                                      (self.press_down <= self.press_left and self.press_left > 0) or
                                      (self.press_down <= self.press_right and self.press_right > 0)):
            self.direction = 'south'
        elif self.press_left > 0 and ((self.press_left <= self.press_up and self.press_up > 0) or
                                      (self.press_left <= self.press_down and self.press_down > 0) or
                                      (self.press_left <= self.press_right and self.press_right > 0)):
            self.direction = 'west'
        elif self.press_right > 0 and ((self.press_right <= self.press_up and self.press_up > 0) or
                                       (self.press_right <= self.press_down and self.press_down > 0) or
                                       (self.press_right <= self.press_left and self.press_left > 0)):
            self.direction = 'east'
        # Of ga in de richting van de enige knop die je indrukt.
        elif self.press_up > 0:
            self.direction = 'north'
        elif self.press_down > 0:
            self.direction = 'south'
        elif self.press_left > 0:
            self.direction = 'west'
        elif self.press_right > 0:
            self.direction = 'east'

        # Als je helemaal geen knoppen indrukt, ga dan in de stilstand pose.
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and \
           not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.update(False)

        # Als je een knop indrukt, en er is geen delay, beweeg dan in die richting.
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or \
           keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if self.step_delay > 0:
                self.step_delay -= 1
            else:
                self.update(True)

    def update(self, moving):
        if moving:
            if self.direction == 'west':
                self.clip(self.west_states)
                self.rect.x -= self.movespeed
            if self.direction == 'east':
                self.clip(self.east_states)
                self.rect.x += self.movespeed
            if self.direction == 'north':
                self.clip(self.north_states)
                self.rect.y -= self.movespeed
            if self.direction == 'south':
                self.clip(self.south_states)
                self.rect.y += self.movespeed

        if not moving:
            if self.direction == 'west':
                self.clip(self.west_states[0])
            if self.direction == 'east':
                self.clip(self.east_states[0])
            if self.direction == 'north':
                self.clip(self.north_states[0])
            if self.direction == 'south':
                self.clip(self.south_states[0])

        # Update the image for each pass
        self.image = self.full_sprite.subsurface(self.full_sprite.get_clip())

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.full_sprite.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.step_count = 0
            self.step_animation = 0
            self.step_delay = 0
            self.full_sprite.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def get_frame(self, frame_set):
        self.step_count += 1
        if self.step_count % (24 / self.movespeed) == 1:
            self.step_animation += 1
            if self.step_animation > 3:
                self.step_animation = 0
        return frame_set[self.step_animation]

    def move_back(self):
        if self.direction == 'west':
            self.rect.x += 1
        if self.direction == 'east':
            self.rect.x -= 1
        if self.direction == 'north':
            self.rect.y += 1
        if self.direction == 'south':
            self.rect.y -= 1
