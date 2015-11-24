

import pygame

from battle2.model import State
import battle2.eventmanager as evm

MOVESPEED1 = 1
MOVESPEED2 = 2
MOVESPEED3 = 4
MOVESPEED4 = 8


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
        if isinstance(event, evm.TickEvent):

            currentstate = self.model.state.peek()
            if currentstate == State.Play:
                key_input = pygame.key.get_pressed()

                self.model.char.movespeed = MOVESPEED2
                if (key_input[pygame.K_LSHIFT] or key_input[pygame.K_RSHIFT]) and \
                   (key_input[pygame.K_LCTRL] or key_input[pygame.K_RCTRL]):
                    self.model.char.movespeed = MOVESPEED4
                elif key_input[pygame.K_LSHIFT] or key_input[pygame.K_RSHIFT]:
                    self.model.char.movespeed = MOVESPEED3
                elif key_input[pygame.K_LCTRL] or key_input[pygame.K_RCTRL]:
                    self.model.char.movespeed = MOVESPEED1

                if key_input[pygame.K_UP] or key_input[pygame.K_DOWN] or \
                   key_input[pygame.K_LEFT] or key_input[pygame.K_RIGHT]:
                    if key_input[pygame.K_UP]:
                        self.model.char.step_north += 1
                    else:
                        self.model.char.step_north = 0
                    if key_input[pygame.K_DOWN]:
                        self.model.char.step_south += 1
                    else:
                        self.model.char.step_south = 0
                    if key_input[pygame.K_LEFT]:
                        self.model.char.step_west += 1
                    else:
                        self.model.char.step_west = 0
                    if key_input[pygame.K_RIGHT]:
                        self.model.char.step_east += 1
                    else:
                        self.model.char.step_east = 0
                    self.model.char.move()
                else:
                    self.model.char.stand()

            for event in pygame.event.get():                    # Called for each game tick. We check our input here.

                if event.type == pygame.QUIT:                   # handle window manager closing our window
                    self.ev_manager.post(evm.QuitEvent())

                if event.type == pygame.MOUSEBUTTONDOWN:        # handle mouse down events
                    if event.button:
                        self.ev_manager.post(evm.InputEvent(clickpos=event.pos, button=event.button))

                if event.type == pygame.KEYDOWN:                # handle key down events
                    if event.key == pygame.K_ESCAPE:
                        self.ev_manager.post(evm.ChangeStateEvent(None, self.model.state.peek()))
                    else:
                        currentstate = self.model.state.peek()
                        if currentstate == State.Menu:
                            self.keydown_menu(event, currentstate)
                        if currentstate == State.Play:
                            self.keydown_play(event, currentstate)
                        if currentstate == State.Help:
                            self.keydown_help(event, currentstate)

    def keydown_menu(self, event, currentstate):
        """
        Handles menu key events.
        """
        if event.key == pygame.K_ESCAPE:                                            # escape pops the menu
            self.ev_manager.post(evm.ChangeStateEvent(None, currentstate))
        if event.key == pygame.K_SPACE:                                             # space plays the game
            self.ev_manager.post(evm.ChangeStateEvent(State.Play))

    def keydown_help(self, event, currentstate):
        """
        Handles help key events.
        """
        if event.key in [pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN]:         # space, enter or escape pops help
            self.ev_manager.post(evm.ChangeStateEvent(None, currentstate))

    def keydown_play(self, event, currentstate):
        """
        Handles play key events.
        """
        if event.key == pygame.K_ESCAPE:
            self.ev_manager.post(evm.ChangeStateEvent(None, currentstate))
        if event.key == pygame.K_F1:                                                # F1 shows the help
            self.ev_manager.post(evm.ChangeStateEvent(State.Help))
        elif event.key == pygame.K_F12:
            self.ev_manager.post(evm.InputEvent(event.key))
        elif (event.key == pygame.K_UP or event.key == pygame.K_DOWN or
              event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            self.ev_manager.post(evm.InputEvent(event.key))
        else:
            self.ev_manager.post(evm.InputEvent(event.unicode))
