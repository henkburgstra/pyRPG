

import os

import pygame

from battle2.model import State
from battle2.eventmanager import *

SCREENWIDTH = 1600
SCREENHEIGHT = 800  # 1600, 800  # 1920, 1080
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWPOS = 100, 100

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
        self.debug = False                  # todo, moet de debug niet in de model?
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
        self.screen.blit(self.window, WINDOWPOS)
        self._show_debug()
        self._show_buttons()
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def _show_debug(self):
        if self.debug:
            text = ("FPS:            {}".format(int(self.clock.get_fps())),
                    )
            for count, line in enumerate(text):
                self.screen.blit(self.debugfont.render(line, True, WHITE), (0, count * 10))

    def _show_buttons(self):
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


class MapView(object):
    def __init__(self, layer, window_width, window_height):
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self, position, caption):
        pygame.sprite.Sprite.__init__(self)

        self._width = 40
        self._height = 40
        self._bgcolor = BLACK
        self._visible = True

        self.image = pygame.Surface((self._width, self._height))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self._font = pygame.font.SysFont('sans', 14)
        self._caption = self._font.render(caption, True, WHITE)
        self._caprect = self._caption.get_rect()
        self._caprect.center = self.rect.width / 2, self.rect.height / 2

        self._update()

    def draw(self, surface):
        if self._visible:
            surface.blit(self.image, self.rect.topleft)

    def _update(self):
        self.image.fill(self.bgcolor)
        pygame.draw.rect(self.image, WHITE, (0, 0, self._width, self._height), 1)
        self.image.blit(self._caption, self._caprect)

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
