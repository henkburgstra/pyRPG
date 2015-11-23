

import os

import pygame
import pytmx
import pyscroll
import pyscroll.data

from battle2.model import State
from battle2.eventmanager import *

SCREENWIDTH = 1600
SCREENHEIGHT = 800  # 1600, 800  # 1920, 1080
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWPOS = 100, 100

PLAYERLAYER = 2

FPS = 60

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
GREEN = pygame.Color("green")
DARKGRAY = pygame.Color("gray12")


class GraphicalView(object):
    """
    Draws the model state onto the screen.
    """
    def __init__(self, ev_manager, model):
        """
        ev_manager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.

        Attributes:
        isinitialized (bool): pygame is ready to draw.
        screen (pygame.Surface): the screen surface.
        clock (pygame.time.Clock): keeps the fps constant.
        fonts (pygame.Font): a small font.
        """
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model
        self.isinitialized = False

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, InitializeEvent):
            self._initialize()

        elif isinstance(event, QuitEvent):
            self.isinitialized = False
            pygame.quit()

        elif isinstance(event, CharUpdateEvent):

            self.player1.rect.topleft = self.model.char.new_position
            self.player1.updatespeed = self.model.char.movespeed
            self.player1.update(event)

        elif isinstance(event, InputEvent):
            if event.key == pygame.K_F12:
                self.debug ^= True          # simple boolean swith

        elif isinstance(event, TickEvent):
            if not self.isinitialized:
                return
            currentstate = self.model.state.peek()
            if currentstate == State.Intro:
                self.render_intro()
            if currentstate == State.Menu:
                self.render_menu()
            if currentstate == State.Play:
                self.render_play()
            if currentstate == State.Help:
                self.render_help()
            self.clock.tick(FPS)            # limit the redraw speed to 60 frames per second

    def _initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.DOUBLEBUF)  # | pygame.FULLSCREEN)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(BLACK)
        self.background = self.background.convert()
        self.window = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.window.fill(DARKGRAY)
        self.window = self.window.convert()

        self.clock = pygame.time.Clock()
        self.debugfont = pygame.font.SysFont('courier', 11)
        self.titlefont = pygame.font.SysFont('sans', 25, True)
        self._init_buttons()

        self.map = MapView(self.model, PLAYERLAYER, WINDOWWIDTH, WINDOWHEIGHT)

        import data
        self.player1 = CharSprite(data.heroes.alagos.BMP)
        self.map.group.add(self.player1)

        self.debug = False                  # todo, moet de debug niet in de model?
        self.isinitialized = True

    def render_intro(self):
        """
        Render the game intro.
        """
        bg_rect = self.background.get_rect()

        somewords = self.titlefont.render('Battle...!', True, GREEN)
        text_rect = somewords.get_rect()
        text_rect.center = bg_rect.width/2, bg_rect.height/2

        self.screen.blit(somewords, text_rect.topleft)
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def render_play(self):
        """
        Render the game play.
        """
        self.show_window()
        self.show_debug()
        self.show_buttons()
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def show_window(self):
        self.map.group.center(self.player1.rect.center)
        self.map.group.draw(self.window)
        self.screen.blit(self.window, WINDOWPOS)

    def show_debug(self):
        if self.debug:
            text = ("FPS:            {}".format(int(self.clock.get_fps())),
                    "step_north:     {}".format(self.model.char.step_north),
                    "step_south:     {}".format(self.model.char.step_south),
                    "step_west:      {}".format(self.model.char.step_west),
                    "step_east:      {}".format(self.model.char.step_east),
                    "step_delay:     {}".format(self.model.char.step_delay),
                    "last_direction: {}".format(self.model.char.last_direction),
                    "move_direction: {}".format(self.model.char.move_direction),
                    "movespeed:      {}".format(self.model.char.movespeed),
                    "old_position.x: {}".format(self.model.char.old_position[0]),
                    "old_position.y  {}".format(self.model.char.old_position[1]),
                    "new_position.x: {}".format(self.model.char.new_position[0]),
                    "new_position.y  {}".format(self.model.char.new_position[1]),
                    "step_count:     {}".format(self.player1.step_count),
                    "step_animation: {}".format(self.player1.step_animation),
                    )
            for count, line in enumerate(text):
                self.screen.blit(self.debugfont.render(line, True, WHITE), (0, count * 10))

    def show_buttons(self):
        for button in self.buttons:
            button.draw(self.screen)

    def render_menu(self):
        """
        Render the game menu.
        """
        somewords = self.titlefont.render('You are in the Menu. Space to play. Esc exits.', True, GREEN)
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def render_help(self):
        """
        Render the help screen.
        """
        somewords = self.titlefont.render('Help is here. space, escape or return.', True, GREEN)
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def _init_buttons(self):
        self.button_view = Button((SCREENWIDTH-200,   SCREENHEIGHT-300), "V")
        self.button_up = Button((SCREENWIDTH-150,     SCREENHEIGHT-300), "Up")
        self.button_down = Button((SCREENWIDTH-150,   SCREENHEIGHT-250), "Down")
        self.button_left = Button((SCREENWIDTH-200,   SCREENHEIGHT-250), "Left")
        self.button_right = Button((SCREENWIDTH-100,  SCREENHEIGHT-250), "Right")
        self.button_cancel = Button((SCREENWIDTH-100, SCREENHEIGHT-200), "C")

        self.buttons = [self.button_view, self.button_up, self.button_down, self.button_left, self.button_right,
                        self.button_cancel]


class CharSprite(pygame.sprite.Sprite):
    # CharSprite extends the pygame.sprite.Sprite class
    def __init__(self, spritesheet):
        pygame.sprite.Sprite.__init__(self)

        self.west_states = {0:  (32, 32, 32, 32), 1: (0, 32, 32, 32), 2: (32, 32, 32, 32), 3: (64, 32, 32, 32)}
        self.east_states = {0:  (32, 64, 32, 32), 1: (0, 64, 32, 32), 2: (32, 64, 32, 32), 3: (64, 64, 32, 32)}
        self.north_states = {0: (32, 96, 32, 32), 1: (0, 96, 32, 32), 2: (32, 96, 32, 32), 3: (64, 96, 32, 32)}
        self.south_states = {0: (32,  0, 32, 32), 1: (0,  0, 32, 32), 2: (32,  0, 32, 32), 3: (64,  0, 32, 32)}

        # Assign the spritesheet to self.full_sprite
        self.full_sprite = pygame.image.load(spritesheet)
        # 'Clip' the sheet so that only one frame is displayed (the first frame of _south_states)
        self.full_sprite.set_clip(pygame.Rect(self.north_states[0]))

        # Create a rect to animate around the screen
        self.image = self.full_sprite.subsurface(self.full_sprite.get_clip())
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.updatespeed = 0
        self.step_count = 0
        self.step_animation = 0

    def update(self, event):

        if event.movespeed is None:
            if event.last_dir == 'west':
                self._clip(self.west_states[0])
            if event.last_dir == 'east':
                self._clip(self.east_states[0])
            if event.last_dir == 'north':
                self._clip(self.north_states[0])
            if event.last_dir == 'south':
                self._clip(self.south_states[0])
        else:
            if event.move_dir == 'west':
                self._clip(self.west_states)
            if event.move_dir == 'east':
                self._clip(self.east_states)
            if event.move_dir == 'north':
                self._clip(self.north_states)
            if event.move_dir == 'south':
                self._clip(self.south_states)

        # Update the image for each pass
        self.image = self.full_sprite.subsurface(self.full_sprite.get_clip())

    def _clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.full_sprite.set_clip(pygame.Rect(self._get_frame(clipped_rect)))
        else:
            self.step_count = 0
            self.step_animation = 0
            self.full_sprite.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def _get_frame(self, frame_set):
        self.step_count += 1
        if self.step_count % (24 / self.updatespeed) == 1:  # 24 is deelbaar door alle movespeeds
            self.step_animation += 1
            if self.step_animation > 3:
                self.step_animation = 0
        return frame_set[self.step_animation]


class MapView(object):
    def __init__(self, model, layer, window_width, window_height):

        self.model = model

        # todo, is dit echt de manier om te werken?

        self.model.map.tmx_data = pytmx.load_pygame(self.model.map.map_path)
        self.model.map.map_data = pyscroll.data.TiledMapData(self.model.map.tmx_data)

        self.model.map.width = int(self.model.map.tmx_data.width * self.model.map.tmx_data.tilewidth)
        self.model.map.height = int(self.model.map.tmx_data.height * self.model.map.tmx_data.tileheight)

        map_layer = pyscroll.BufferedRenderer(self.model.map.map_data, (window_width, window_height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=layer)


class Button(pygame.sprite.Sprite):
    def __init__(self, position, caption):
        pygame.sprite.Sprite.__init__(self)

        self.width = 40
        self.height = 40
        self._bgcolor = BLACK
        self._visible = True

        self.image = pygame.Surface((self.width, self.height))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.font = pygame.font.SysFont('sans', 14)
        self.caption = self.font.render(caption, True, WHITE)
        self.caprect = self.caption.get_rect()
        self.caprect.center = self.rect.width / 2, self.rect.height / 2

        self._update()

    def draw(self, surface):
        if self._visible:
            surface.blit(self.image, self.rect.topleft)

    def _update(self):
        self.image.fill(self.bgcolor)
        pygame.draw.rect(self.image, WHITE, (0, 0, self.width, self.height), 1)
        self.image.blit(self.caption, self.caprect)

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
