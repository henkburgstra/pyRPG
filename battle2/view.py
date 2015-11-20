

import os
import pygame
from battle2.model import State
from battle2.eventmanager import *

SCREENWIDTH = 1600
SCREENHEIGHT = 800  # 1600, 800  # 1920, 1080

FPS = 60

BLACK = pygame.Color("black")
GREEN = pygame.Color("green")


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
        self.screen = None
        self.clock = None
        self.debugfont = None
        self.buttonfont = None

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, TimeEvent):
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
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

    def render_intro(self):
        """
        Render the game intro.
        """
        self.screen.fill(BLACK)
        screen_rect = self.screen.get_rect()

        somewords = self.buttonfont.render('Battle...!', True, GREEN)
        text_rect = somewords.get_rect()
        text_rect.center = screen_rect.width/2, screen_rect.height/2

        self.screen.blit(somewords, text_rect)
        pygame.display.flip()

    def render_menu(self):
        """
        Render the game menu.
        """
        self.screen.fill(BLACK)
        somewords = self.buttonfont.render('You are in the Menu. Space to play. Esc exits.', True, GREEN)
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()

    def render_play(self):
        """
        Render the game play.
        """
        self.screen.fill(BLACK)
        somewords = self.buttonfont.render('You are playing the game. F1 for help.', True, GREEN)
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()

    def render_help(self):
        """
        Render the help screen.
        """
        self.screen.fill(BLACK)
        somewords = self.buttonfont.render('Help is here. space, escape or return.', True, GREEN)
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()

    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.DOUBLEBUF)  # | pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.debugfont = pygame.font.SysFont('courier', 11)
        self.buttonfont = pygame.font.SysFont('sans', 14)
        self.isinitialized = True


class CharSprite(pygame.sprite.Sprite):
    pass