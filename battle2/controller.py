

import pygame
from .eventmanager import *


class HumanInput(object):
    """
    Handles keyboard and mouse input.
    """
    def __init__(self, ev_manager, model):
        """
        ev_manager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
        """
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ev_manager.post(QuitEvent())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ev_manager.post(InputEvent(None, pygame.mouse.get_pos()))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ev_manager.post(QuitEvent())
                    else:
                        self.ev_manager.post(InputEvent(event.unicode, None))
