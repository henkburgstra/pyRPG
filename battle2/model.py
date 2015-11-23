

import enum
import time

from battle2.eventmanager import *


class GameEngine(object):
    """
    Tracks the game state.
    """

    INTRO_WAIT_TIME = 2
    MAP_PATH = 'resources/maps/area01/new.tmx'          # todo, dit moet uiteraard nog op een andere dynamische plek

    def __init__(self, ev_manager):
        """
        ev_manager (EventManager): Allows posting messages to the event queue.

        Attributes:
        running (bool): True while the engine is online. Changed via QuitEvent().
        """
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.running = False
        self.state = StateMachine()
        self.map = MapData(self.MAP_PATH)
        self.char = CharData(ev_manager)
        self.wait_timer = None                          # todo, is dit wel de juiste plek voor een timer?

    def notify(self, event):
        """
        Called by an event in the message queue.
        """
        if isinstance(event, QuitEvent):
            self.running = False

        if isinstance(event, ChangeStateEvent):
            if not event.new_state:                     # pop request
                if not self.state.pop():                # false if no more states are left
                    self.ev_manager.post(QuitEvent())
            else:
                self.state.push(event.new_state)        # push a new state on the stack

        if isinstance(event, TickEvent):
            currentstate = self.state.peek()
            if currentstate == State.Intro:
                new_time = time.time()
                if new_time - self.wait_timer > self.INTRO_WAIT_TIME:
                    self.wait_timer = None
                    self.ev_manager.post(ChangeStateEvent(None, currentstate))

    def run(self):
        """
        Starts the game engine loop.

        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify().
        """
        self.running = True
        self.ev_manager.post(InitializeEvent())
        self.ev_manager.post(ChangeStateEvent(State.Play))
        self.ev_manager.post(ChangeStateEvent(State.Intro))
        self.wait_timer = time.time()
        while self.running:
            new_tick = TickEvent()
            self.ev_manager.post(new_tick)


class State(enum.Enum):
    # State machine constants for the StateMachine class below
    Intro = 1
    Menu = 2
    Help = 3
    About = 4
    Play = 5
    Dialogue = 6
    Settings = 7


class StateMachine(object):
    """
    Manages a stack based state machine.
    peek(), pop() and push() perform as traditionally expected.
    peeking and popping an empty stack returns None.
    """
    def __init__(self):
        self.statestack = []

    def peek(self):
        """
        Returns the current state without altering the stack.
        Returns None if the stack is empty.
        """
        try:
            return self.statestack[-1]      # [-1] is om de laatste in een list te krijgen
        except IndexError:
            return None     # empty stack

    def pop(self):
        """
        Returns the current state and remove it from the stack.
        Returns None if the stack is empty.
        """
        try:
            self.statestack.pop()
            return len(self.statestack) > 0
        except IndexError:
            return None     # empty stack

    def push(self, state):
        """
        Push a new state onto the stack.
        Returns the pushed value.
        """
        self.statestack.append(state)
        return state


class CharData(object):
    def __init__(self, ev_manager):
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)

        self.old_position = [0, 0]
        self.new_position = [0, 0]
        self.last_direction = 'north'
        self.move_direction = None
        self.movespeed = 0

        self.step_north = 0
        self.step_south = 0
        self.step_west = 0
        self.step_east = 0
        self.step_delay = 0

    def notify(self, event):
        pass

    def stand(self):
        self.move_direction = None
        self.step_north = 0
        self.step_south = 0
        self.step_west = 0
        self.step_east = 0
        self.step_delay = 0
        self.ev_manager.post(CharUpdateEvent(last_dir=self.last_direction))

    def move(self):

        # Als hij nog geen stappen heeft gezet en hij kijkt naar een andere kant dan je drukt, stel een delay in.
        if self.move_direction is None and ((self.step_north == 0 and self.last_direction == 'north') or
                                            (self.step_south == 0 and self.last_direction == 'south') or
                                            (self.step_west == 0 and self.last_direction == 'west') or
                                            (self.step_east == 0 and self.last_direction == 'east')):
            self.step_delay = 7

        # Als je meerdere knoppen indrukt, ga dan naar de richting van de laatst ingedrukte knop.
        if self.step_north > 0 and ((self.step_north <= self.step_south and self.step_south > 0) or
                                    (self.step_north <= self.step_west and self.step_west > 0) or
                                    (self.step_north <= self.step_east and self.step_east > 0)):
            self.move_direction = 'north'
        elif self.step_south > 0 and ((self.step_south <= self.step_north and self.step_north > 0) or
                                      (self.step_south <= self.step_west and self.step_west > 0) or
                                      (self.step_south <= self.step_east and self.step_east > 0)):
            self.move_direction = 'south'
        elif self.step_west > 0 and ((self.step_west <= self.step_north and self.step_north > 0) or
                                     (self.step_west <= self.step_south and self.step_south > 0) or
                                     (self.step_west <= self.step_east and self.step_east > 0)):
            self.move_direction = 'west'
        elif self.step_east > 0 and ((self.step_east <= self.step_north and self.step_north > 0) or
                                     (self.step_east <= self.step_south and self.step_south > 0) or
                                     (self.step_east <= self.step_west and self.step_west > 0)):
            self.move_direction = 'east'
        # Of ga in de richting van de enige knop die je indrukt.
        elif self.step_north > 0:
            self.move_direction = 'north'
        elif self.step_south > 0:
            self.move_direction = 'south'
        elif self.step_west > 0:
            self.move_direction = 'west'
        elif self.step_east > 0:
            self.move_direction = 'east'

        self.last_direction = self.move_direction

        # Als je een knop indrukt, en er is geen delay, beweeg dan in die richting.
        if self.step_delay > 0:
            self.step_delay -= 1
        else:
            if self.move_direction == "north":
                self.new_position[1] -= self.movespeed
            elif self.move_direction == "south":
                self.new_position[1] += self.movespeed
            elif self.move_direction == "west":
                self.new_position[0] -= self.movespeed
            elif self.move_direction == "east":
                self.new_position[0] += self.movespeed

            self.ev_manager.post(CharUpdateEvent(move_dir=self.move_direction, movespeed=self.movespeed))


class MapData(object):
    def __init__(self, map_path):

        self.map_path = map_path

        self.tmx_data = None
        self.map_data = None

        self.width = None
        self.height = None

        self.start_pos = []     # start pos is maar één rect, maar moet in een list staan ivm updaten
        self.trees = []         # een lijst van rects van alle bomen
        self.waters = []
        self.heroes = []
        self.villains = []
        self.obstacles = []
        self.low_obst = []

    #     for rect in tmx_data.get_layer_by_name("trees"):
    #         self.add_rect_to_list(rect, self.trees)   # vul die lijst van rects van alle bomen
    #         self.add_rect_to_list(rect, self.obstacles)
    #
    #     for rect in tmx_data.get_layer_by_name("water"):
    #         self.add_rect_to_list(rect, self.waters)
    #         self.add_rect_to_list(rect, self.low_obst)
    #
    # @staticmethod
    # def add_rect_to_list(rect, alist):
    #     alist.append(pygame.Rect(rect.x, rect.y, rect.width, rect.height))
    #
    # @staticmethod
    # def del_rect_from_list(rect, alist):
    #     alist.remove(pygame.Rect(rect.x, rect.y, rect.width, rect.height))
