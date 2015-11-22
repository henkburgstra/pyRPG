

import pygame

from battle2.model import State
from battle2.eventmanager import *


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

            key_input = pygame.key.get_pressed()
            if 1 in key_input:
                currentstate = self.model.state.peek()
                if currentstate == State.Play:
                    if key_input[pygame.K_UP]:
                        self.ev_manager.post(CharMoveEvent("North"))
                    if key_input[pygame.K_DOWN]:
                        self.ev_manager.post(CharMoveEvent("South"))

            for event in pygame.event.get():                    # Called for each game tick. We check our input here.

                if event.type == pygame.QUIT:                   # handle window manager closing our window
                    self.ev_manager.post(QuitEvent())

                if event.type == pygame.MOUSEBUTTONDOWN:        # handle mouse down events
                    if event.button:
                        self.ev_manager.post(InputEvent(clickpos=event.pos, button=event.button))

                if event.type == pygame.KEYDOWN:                # handle key down events
                    if event.key == pygame.K_ESCAPE:
                        self.ev_manager.post(ChangeStateEvent(None, self.model.state.peek()))
                    # else:
                    #     currentstate = self.model.state.peek()
                    #     if currentstate == State.Menu:
                    #         self.keydown_menu(event, currentstate)
                    #     if currentstate == State.Play:
                    #         self.keydown_play(event, currentstate)
                    #     if currentstate == State.Help:
                    #         self.keydown_help(event, currentstate)

    def keydown_menu(self, event, currentstate):
        """
        Handles menu key events.
        """
        if event.key == pygame.K_ESCAPE:                                            # escape pops the menu
            self.ev_manager.post(ChangeStateEvent(None, currentstate))
        if event.key == pygame.K_SPACE:                                             # space plays the game
            self.ev_manager.post(ChangeStateEvent(State.Play))

    def keydown_help(self, event, currentstate):
        """
        Handles help key events.
        """
        if event.key in [pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN]:         # space, enter or escape pops help
            self.ev_manager.post(ChangeStateEvent(None, currentstate))

    def keydown_play(self, event, currentstate):
        """
        Handles play key events.
        """
        if event.key == pygame.K_ESCAPE:
            self.ev_manager.post(ChangeStateEvent(None, currentstate))
        if event.key == pygame.K_F1:                                                # F1 shows the help
            self.ev_manager.post(ChangeStateEvent(State.Help))
        elif event.key == pygame.K_F12:
            self.ev_manager.post(InputEvent(event.key))
        else:
            self.ev_manager.post(InputEvent(event.unicode))
