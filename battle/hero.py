
import pygame


# Hero extends the pygame.sprite.Sprite class
class Hero(pygame.sprite.Sprite):
    # In the main program, we will pass a spritesheet and x-y values to the constructor
    def __init__(self, position, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        # Load our pickled frame values and assign them to dicts
        self.west_states = {0:  (32, 32, 32, 32), 1: (0, 32, 32, 32), 2: (32, 32, 32, 32), 3: (64, 32, 32, 32)}
        self.east_states = {0:  (32, 64, 32, 32), 1: (0, 64, 32, 32), 2: (32, 64, 32, 32), 3: (64, 64, 32, 32)}
        self.north_states = {0: (32, 96, 32, 32), 1: (0, 96, 32, 32), 2: (32, 96, 32, 32), 3: (64, 96, 32, 32)}
        self.south_states = {0: (32,  0, 32, 32), 1: (0,  0, 32, 32), 2: (32,  0, 32, 32), 3: (64,  0, 32, 32)}

        # Assign the spritesheet to self.sheet
        self.sheet = pygame.image.load(spritesheet)
        # 'Clip' the sheet so that only one frame is displayed (the first frame of south_states)
        self.sheet.set_clip(pygame.Rect(self.south_states[0]))

        # Create a rect to animate around the screen
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        # Assign the position parameter value to the topleft x-y values of the rect
        self.rect.topleft = position

        # We'll use this later to cycle through frames
        self.direction = 'north'
        self.step_count = 0
        self.step_animation = 0
        self.step_delay = 0

        self.press_up = 0
        self.press_down = 0
        self.press_left = 0
        self.press_right = 0

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
                self.rect.x -= 1
            if self.direction == 'east':
                self.clip(self.east_states)
                self.rect.x += 1
            if self.direction == 'north':
                self.clip(self.north_states)
                self.rect.y -= 1
            if self.direction == 'south':
                self.clip(self.south_states)
                self.rect.y += 1

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
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.step_count = 0
            self.step_animation = 0
            self.step_delay = 0
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def get_frame(self, frame_set):
        self.step_count += 1
        if self.step_count % 10 == 1:
            self.step_animation += 1
            if self.step_animation > 3:
                self.step_animation = 0
        return frame_set[self.step_animation]
