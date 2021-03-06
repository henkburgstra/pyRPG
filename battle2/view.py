

import os

import pygame

from battle2.model import Direction
from battle2.model import State
import battle2.eventmanager as evm

SCREENWIDTH = 1600
SCREENHEIGHT = 800  # 1600, 800  # 1920, 1080
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWPOS = 100, 100

TILESIZE = 32
PLAYERLAYER = 2
GRIDLAYER = 4

FPS = 60

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
GREEN = pygame.Color("green")
GRAY = pygame.Color("gray38")
DARKGRAY = pygame.Color("gray12")
BLUE = pygame.Color("blue")
PURPLE = pygame.Color("purple")


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
        if isinstance(event, evm.InitializeEvent):
            self._initialize()

        elif isinstance(event, evm.DrawMapEvent):
            self._draw_map()

        elif isinstance(event, evm.QuitEvent):
            self.isinitialized = False
            pygame.quit()

        elif isinstance(event, evm.CharUpdateEvent):

            self.current_player.rect.topleft = self.model.current_character.new_position
            self.detect_collision()
            self.current_player.updatespeed = self.model.current_character.movespeed
            self.current_player.update(event)

        elif isinstance(event, evm.InputEvent):
            if event.key == pygame.K_c:
                self.model.current_character.align_to_grid()
                # voeg de rect van de huidige speler toe aan de lists en verwijder de rect van start_pos
                self.model.map.add_rect_to_list(self.current_player.rect, self.model.map.heroes)
                self.model.map.add_rect_to_list(self.current_player.rect, self.model.map.obstacles)
                self.model.map.start_pos = None

                self.model.current_character = self.model.characters[1]
                self.current_player = self.players[1]

                # de rect van de player die aan de beurt is weer verwijderen en ken de start_pos toe
                self.model.map.del_rect_from_list(self.current_player.rect, self.model.map.heroes)
                self.model.map.del_rect_from_list(self.current_player.rect, self.model.map.obstacles)
                self.model.map.start_pos = self.current_player.rect.copy()

                # voeg de info sprites toe aan de mapview vanuit de mapdata
                self.map1.info.append(InfoSprite(self.model.map.start_pos, 'start', GRIDLAYER))
                for rect in self.model.map.trees:
                    self.map1.info.append(InfoSprite(pygame.Rect(rect), 'tree', GRIDLAYER))
                for rect in self.model.map.waters:
                    self.map1.info.append(InfoSprite(pygame.Rect(rect), 'water', GRIDLAYER))
                for rect in self.model.map.heroes:
                    self.map1.info.append(InfoSprite(pygame.Rect(rect), 'hero', GRIDLAYER))

                # voeg de obstacle waarden toe aan de mapview vanuit de mapdata
                for rect in self.model.map.obstacles:
                    self.map1.obstacles.append(pygame.Rect(rect))
                for rect in self.model.map.low_obst:
                    self.map1.low_obst.append(pygame.Rect(rect))


            if event.key == pygame.K_F10:
                self.map1.grid.show ^= True
            if event.key == pygame.K_F11:
                self.info ^= True
            if event.key == pygame.K_F12:
                self.debug ^= True          # simple boolean swith

        elif isinstance(event, evm.TickEvent):
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

        self.players = []
        for character in self.model.characters:
            self.players.append(CharSprite(character.bmp))
        self.current_player = None

        self.info = False
        self.debug = False
        self.isinitialized = True

    def _draw_map(self):
        import pyscroll
        map_layer = pyscroll.BufferedRenderer(self.model.map.map_data, (WINDOWWIDTH, WINDOWHEIGHT), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=PLAYERLAYER)

        # zet alle players sprites op de juiste posities
        for count, player in enumerate(self.players):
            player.rect.topleft = self.model.characters[count].new_position

        self.current_player = self.players[0]

        self.group.add(self.players)

        # voeg de posities van alles heroes aan de mapdata toe en ook als obstacle
        for char in self.model.characters:
            rect = pygame.Rect(char.new_position[0], char.new_position[1], char.width, char.height)
            self.model.map.add_rect_to_list(rect, self.model.map.heroes)
            self.model.map.add_rect_to_list(rect, self.model.map.obstacles)

        # de rect van de player die aan de beurt is weer verwijderen en ken de start_pos toe
        self.model.map.del_rect_from_list(self.current_player.rect, self.model.map.heroes)
        self.model.map.del_rect_from_list(self.current_player.rect, self.model.map.obstacles)
        self.model.map.start_pos = self.current_player.rect.copy()

        # creeer een mapview
        self.map1 = MapView(self.model.map.width, self.model.map.height)

        # maak van het current hokje een hero-info sprite
        self.map1.current = InfoSprite(self.current_player.rect, 'hero', GRIDLAYER)

        # voeg de info sprites toe aan de mapview vanuit de mapdata
        self.map1.info.append(InfoSprite(self.model.map.start_pos, 'start', GRIDLAYER))
        for rect in self.model.map.trees:
            self.map1.info.append(InfoSprite(pygame.Rect(rect), 'tree', GRIDLAYER))
        for rect in self.model.map.waters:
            self.map1.info.append(InfoSprite(pygame.Rect(rect), 'water', GRIDLAYER))
        for rect in self.model.map.heroes:
            self.map1.info.append(InfoSprite(pygame.Rect(rect), 'hero', GRIDLAYER))

        # voeg de obstacle waarden toe aan de mapview vanuit de mapdata
        for rect in self.model.map.obstacles:
            self.map1.obstacles.append(pygame.Rect(rect))
        for rect in self.model.map.low_obst:
            self.map1.low_obst.append(pygame.Rect(rect))

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
        self.draw_grid()
        self.draw_info()
        self.show_window()
        self.show_debug()
        self.show_buttons()
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def draw_grid(self):
        if self.map1.grid.show:
            self.group.add(self.map1.grid)
        else:
            self.group.remove(self.map1.grid)

    def draw_info(self):
        if self.info:
            self.map1.current.rect.topleft = self.model.current_character.new_position
            self.group.add(self.map1.current)
            self.group.add(self.map1.info)
        else:
            self.group.remove(self.map1.current)
            self.group.remove(self.map1.info)

    def show_window(self):
        self.group.center(self.current_player.rect.center)
        self.group.draw(self.window)
        self.screen.blit(self.window, WINDOWPOS)

    def show_debug(self):
        if self.debug:
            text = ("FPS:            {}".format(int(self.clock.get_fps())),
                    "step_north:     {}".format(self.model.current_character.step_north),
                    "step_south:     {}".format(self.model.current_character.step_south),
                    "step_west:      {}".format(self.model.current_character.step_west),
                    "step_east:      {}".format(self.model.current_character.step_east),
                    "step_delay:     {}".format(self.model.current_character.step_delay),
                    "last_direction: {}".format(self.model.current_character.last_direction),
                    "move_direction: {}".format(self.model.current_character.move_direction),
                    "movespeed:      {}".format(self.model.current_character.movespeed),
                    "start_pos.x:    {}".format(self.model.map.start_pos[0]
                                                if self.model.map.start_pos is not None else "None"),
                    "old_position.x: {}".format(self.model.current_character.old_position[0]),
                    "new_position.x: {}".format(self.model.current_character.new_position[0]),
                    "start_pos.y     {}".format(self.model.map.start_pos[1]
                                                if self.model.map.start_pos is not None else "None"),
                    "old_position.y  {}".format(self.model.current_character.old_position[1]),
                    "new_position.y  {}".format(self.model.current_character.new_position[1]),
                    "step_count:     {}".format(self.current_player.step_count),
                    "step_animation: {}".format(self.current_player.step_animation),
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
        self.button_view = ButtonSprite((SCREENWIDTH-200,   SCREENHEIGHT-300), "V")
        self.button_up = ButtonSprite((SCREENWIDTH-150,     SCREENHEIGHT-300), "Up")
        self.button_down = ButtonSprite((SCREENWIDTH-150,   SCREENHEIGHT-250), "Down")
        self.button_left = ButtonSprite((SCREENWIDTH-200,   SCREENHEIGHT-250), "Left")
        self.button_right = ButtonSprite((SCREENWIDTH-100,  SCREENHEIGHT-250), "Right")
        self.button_cancel = ButtonSprite((SCREENWIDTH-100, SCREENHEIGHT-200), "C")

        self.buttons = [self.button_view, self.button_up, self.button_down, self.button_left, self.button_right,
                        self.button_cancel]

    def detect_collision(self):
        # loop tegen de rand van een obstacle aan
        # er mag maar 1 obstacle in deze lijst zijn
        if len(self.current_player.rect.collidelistall(self.map1.obstacles)) == 1:
            # obj_nr is het nummer van de betreffende obstacle
            obj_nr = self.current_player.rect.collidelist(self.map1.obstacles)
            self.model.current_character.move_side(self.map1.obstacles[obj_nr])
            self.current_player.rect.topleft = self.model.current_character.new_position

        # loop tegen de rand van een low obstacle aan, bijv water
        if len(self.current_player.rect.collidelistall(self.map1.low_obst)) == 1:
            obj_nr = self.current_player.rect.collidelist(self.map1.low_obst)
            self.model.current_character.move_side(self.map1.low_obst[obj_nr])
            self.current_player.rect.topleft = self.model.current_character.new_position

        # loop tegen een obstacle of low_obst aan
        while self.current_player.rect.collidelist(self.map1.obstacles) > -1 or \
                self.current_player.rect.collidelist(self.map1.low_obst) > -1:
            self.model.current_character.move_back()
            self.current_player.rect.topleft = self.model.current_character.new_position


class MapView(object):
    def __init__(self, map_width, map_height):
        self.grid = Grid(map_width, map_height, TILESIZE, GRIDLAYER)
        self.info = []
        self.current = None
        self.obstacles = []
        self.low_obst = []


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
            if event.last_dir == Direction.North:
                self._clip(self.north_states[0])
            if event.last_dir == Direction.South:
                self._clip(self.south_states[0])
            if event.last_dir == Direction.West:
                self._clip(self.west_states[0])
            if event.last_dir == Direction.East:
                self._clip(self.east_states[0])
        else:
            if event.move_dir == Direction.North:
                self._clip(self.north_states)
            if event.move_dir == Direction.South:
                self._clip(self.south_states)
            if event.move_dir == Direction.West:
                self._clip(self.west_states)
            if event.move_dir == Direction.East:
                self._clip(self.east_states)

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


class ButtonSprite(pygame.sprite.Sprite):
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


class InfoSprite(pygame.sprite.Sprite):
    def __init__(self, rect, rect_type, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect_type = rect_type
        pygame.draw.rect(self.image, self._color, (0, 0, rect.width, rect.height), 1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = rect.topleft

    @property
    def _color(self):
        if self.rect_type == 'start':
            return GREEN
        if self.rect_type == 'hero':
            return BLUE
        if self.rect_type == 'tree':
            return PURPLE
        if self.rect_type == 'water':
            return BLUE


class Grid(pygame.sprite.Sprite):
    def __init__(self, map_width, map_height, tile_size, layer):
        pygame.sprite.Sprite.__init__(self)

        self._layer = layer
        self.image = pygame.Surface((map_width, map_height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        for i in range(0, map_width, tile_size):
            pygame.draw.line(self.image, GRAY, (0, i), (map_width, i))
        for i in range(0, map_height, tile_size):
            pygame.draw.line(self.image, GRAY, (i, 0), (i, map_height))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

        self.show = False
