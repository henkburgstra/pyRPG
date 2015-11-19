

import pygame
import battle2.model as model
from battle2.eventmanager import *


class HumanInput(object):
    """
    Handles keyboard and mouse input.
    """
    def __init__(self, ev_manager, model1):
        """
        ev_manager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
        """
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model1

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, TickEvent):
            for event in pygame.event.get():                    # Called for each game tick. We check our input here.

                if event.type == pygame.QUIT:                   # handle window manager closing our window
                    self.ev_manager.post(QuitEvent())

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ev_manager.post(InputEvent(None, pygame.mouse.get_pos()))

                if event.type == pygame.KEYDOWN:                # handle key down events
                    if event.key == pygame.K_ESCAPE:
                        self.ev_manager.post(StateChangeEvent(None))
                    else:
                        currentstate = self.model.state.peek()
                        if currentstate == model.State.Menu:
                            self.keydown_menu(event)
                        if currentstate == model.State.Play:
                            self.keydown_play(event)
                        if currentstate == model.State.Help:
                            self.keydown_help(event)

    def keydown_menu(self, event):
        """
        Handles menu key events.
        """
        if event.key == pygame.K_ESCAPE:                        # escape pops the menu
            self.ev_manager.post(StateChangeEvent(None))
        if event.key == pygame.K_SPACE:                         # space plays the game
            self.ev_manager.post(StateChangeEvent(model.State.Play))

    def keydown_help(self, event):
        """
        Handles help key events.
        """
        if event.key in [pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN]:
            self.ev_manager.post(StateChangeEvent(None))        # space, enter or escape pops help

    def keydown_play(self, event):
        """
        Handles play key events.
        """
        if event.key == pygame.K_ESCAPE:
            self.ev_manager.post(StateChangeEvent(None))
        if event.key == pygame.K_F1:                            # F1 shows the help
            self.ev_manager.post(StateChangeEvent(model.State.Help))
        else:
            self.ev_manager.post(InputEvent(event.unicode, None))
