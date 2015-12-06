

# todo layerprobleem oplossen, wanneer een lagere layer 2 bovenliggende layers overlapt, laat hij informatie weg.
# je kunt dan de lagere layer omhoog halen, maar dat betekent dat er geen (doorzichtige) inhoud in die layer kan zitten
# todo next unit list
# todo frames en borders
# todo moveranges
# todo attack animatie
# todo ugur, mvc, heroes in dict en dynamische posities, niet opslaan in map, maar realtime opslaan in (evt) map

import os
# from random import randint

import pygame
# import pygbutton

from battle.map import Map
from battle.hero import Hero
from battle.drawings import MoveRange
from battle.drawings import Pointer
from battle.drawings import Button

import data
from output import Output

SCREENWIDTH = 1600
SCREENHEIGHT = 800  # 1600, 800  # 1920, 1080
WINDOWSIZE = 800, 600
WINDOWPOS = 100, 100

FPS = 60
SCROLLSPEED = 20        # lager is sneller
VIEWSPEED = 8
PLAYERLAYER = 2
MOVERANGELAYER = 3
POINTERLAYER = 4
GRIDSIZE = 16
MOVERANGESIZE = 400

WHITE = 255, 255, 255
BLACK = 0, 0, 0
DARKGRAY = 32, 32, 32
CLEARPOS = -SCREENWIDTH, -SCREENHEIGHT  # ergens ver weg buiten beeld


class BattleWindow(object):
    def __init__(self):
        global SCREENHEIGHT, SCREENWIDTH
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        info = pygame.display.Info()
        if info.current_h != -1:
            SCREENWIDTH = info.current_w
            SCREENHEIGHT = info.current_h
        self._screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.DOUBLEBUF | pygame.FULLSCREEN)
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(BLACK)
        self._background = self._background.convert()
        self._window = pygame.Surface(WINDOWSIZE)
        self._window = self._window.convert()

        self._clock = pygame.time.Clock()
        self._fps = FPS
        self._debugfont = pygame.font.SysFont('courier', 11)
        self._buttonfont = pygame.font.SysFont('sans', 14)

        self._debug = False

        self._is_viewing = False
        self._view_x, self._view_y = (0, 0)

        self._key_input = None
        self._init_buttons()

        self._map = Map('resources/maps/area01/new.tmx', PLAYERLAYER, *WINDOWSIZE)
        self._player = []       # lijst van hero sprite classes, incl rect voor visuele locatie
        i = 0
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self._player.append(Hero((336 + i * 32, 272 + i * 32), hero.BMP))
                # vul in de map de lijst van rects van alle heroes
                self._map.add_rect_to_list(self._player[i].rect, self._map.heroes)
                self._map.add_rect_to_list(self._player[i].rect, self._map.obstacles)
                i += 1
        self._pointer = Pointer(POINTERLAYER)
        self._moverange = MoveRange(MOVERANGESIZE, MOVERANGELAYER)

        # speler 0 alagos is de eerste cu
        self._cu = 0
        self._start_of_turn()

        self._map.add_sprite_to_map_layer_group(self._moverange)
        # voeg de LIJST van hero sprites toe aan de visuele groep
        self._map.add_sprite_to_map_layer_group(self._player)
        self._map.add_sprite_to_map_layer_group(self._pointer)

    def _init_buttons(self):
        self._button_view = Button((SCREENWIDTH-200,   SCREENHEIGHT-300), "V")
        self._button_up = Button((SCREENWIDTH-150,     SCREENHEIGHT-300), "Up")
        self._button_down = Button((SCREENWIDTH-150,   SCREENHEIGHT-250), "Down")
        self._button_left = Button((SCREENWIDTH-200,   SCREENHEIGHT-250), "Left")
        self._button_right = Button((SCREENWIDTH-100,  SCREENHEIGHT-250), "Right")
        self._button_cancel = Button((SCREENWIDTH-100, SCREENHEIGHT-200), "C")

        self._buttons = [self._button_view, self._button_up, self._button_down, self._button_left, self._button_right,
                         self._button_cancel]
        self._keys = [pygame.K_v, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
                      pygame.K_c]

    def _start_of_turn(self):
        # de rect van de player die aan de beurt is weer verwijderen en ken de start_pos toe
        self._map.del_rect_from_list(self._player[self._cu].rect, self._map.heroes)
        self._map.del_rect_from_list(self._player[self._cu].rect, self._map.obstacles)
        self._map.add_rect_to_list(self._player[self._cu].rect, self._map.start_pos)
        self._moverange.update(self._player[self._cu].rect.center)

    def _end_of_turn(self):
        self._moverange.update(CLEARPOS)
        self._player[self._cu].align_to_grid(GRIDSIZE)
        # voeg de betreffende rect toe aan de lists en verwijder de rect van start_pos
        self._map.add_rect_to_list(self._player[self._cu].rect, self._map.heroes)
        self._map.add_rect_to_list(self._player[self._cu].rect, self._map.obstacles)
        self._map.start_pos = []

        # van waar tot waar moet je scrollen
        start_x, start_y = self._player[self._cu].rect.center
        self._cu += 1
        if self._cu > len(data.party) - 1:
            self._cu = 0
        end_x, end_y = self._player[self._cu].rect.center
        self._scroll_map(start_x, start_y, end_x, end_y)

        self._reset_vars()
        self._start_of_turn()

    def _reset_vars(self):
        self._is_viewing = False
        self._view_x, self._view_y = self._player[self._cu].rect.center

    def run(self):
        game_over = False
        while not game_over:

            self._clock.tick(self._fps)
            self._key_input = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        self._key_input = button.handle_event()

                # if 'down' in self._button_up.handleEvent(event):
                #     pipo = list(pygame.key.get_pressed())
                #     pipo[pygame.K_UP] = pygame.K_UP
                #     self._player[self._cu].handle_movement(pipo)
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    if event.key == pygame.K_F10:
                        self._map.show_grid()
                    if event.key == pygame.K_F11:
                        self._map.show_info(1)
                    if event.key == pygame.K_F12:
                        if self._debug:
                            self._debug = False
                        else:
                            self._debug = True
                    if event.key == pygame.K_SPACE:
                        self._player[self._cu].align_to_grid(GRIDSIZE)
                    if event.key == pygame.K_v:
                        if self._is_viewing:
                            self._is_viewing = False
                            self._scroll_map(self._view_x, self._view_y, *self._player[self._cu].rect.center)
                        else:
                            self._is_viewing = True
                            self._view_x, self._view_y = self._player[self._cu].rect.center
                    if event.key == pygame.K_c:
                        if self._is_viewing:
                            self._is_viewing = False
                            self._scroll_map(self._view_x, self._view_y, *self._player[self._cu].rect.center)
                        else:
                            self._end_of_turn()

            if self._is_viewing:
                self._view_map(self._key_input)
            else:
                if self._key_input is None:
                    continue
                self._player[self._cu].set_speed(self._key_input)
                self._player[self._cu].set_fallback()
                self._player[self._cu].handle_movement(self._key_input)
                self._check_obstacle()

                self._pointer.update(self._player[self._cu].rect.center)
                self._map.center_window(self._player[self._cu].rect.center)

            self._draw()

        pygame.quit()

    def _draw(self):
        self._show_buttons()
        self._map.show_info(0)
        self._map.draw_group(self._window)
        self._screen.blit(self._window, WINDOWPOS)
        if self._debug:
            self._show_debug()
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))

    def _show_buttons(self):
        for count, key in enumerate(self._keys):
            if self._key_input[key]:
                self._buttons[count].bgcolor = DARKGRAY
            else:
                self._buttons[count].bgcolor = BLACK

        for button in self._buttons:
            button.draw(self._background)

    def _show_debug(self):
        # noinspection PyProtectedMember
        text = ("FPS:            {}".format(int(self._clock.get_fps())),
                "press_up:       {}".format(self._player[self._cu]._press_up),
                "press_down:     {}".format(self._player[self._cu]._press_down),
                "press_left:     {}".format(self._player[self._cu]._press_left),
                "press_right:    {}".format(self._player[self._cu]._press_right),
                "direction:      {}".format(self._player[self._cu]._direction),
                "movespeed:      {}".format(self._player[self._cu]._movespeed),
                "cu:             {}".format(self._cu),
                "start_pos.x:    {}".format(self._map.start_pos[0].left if self._map.start_pos != [] else "None"),
                "start_pos.y     {}".format(self._map.start_pos[0].top if self._map.start_pos != [] else "None"),
                "player.x:       {}".format(self._player[self._cu].rect.left),
                "player.y:       {}".format(self._player[self._cu].rect.top),
                "view.x:         {}".format(self._view_x),
                "view.y:         {}".format(self._view_y),
                "step_count:     {}".format(self._player[self._cu]._step_count),
                "step_animation: {}".format(self._player[self._cu]._step_animation),
                "step_delay:     {}".format(self._player[self._cu]._step_delay),
                "is_viewing:     {}".format(self._is_viewing),
                )
        for count, line in enumerate(text):
            self._screen.blit(self._debugfont.render(line, True, WHITE), (0, count * 10))

    def _view_map(self, keys):
        if keys[pygame.K_UP]:
            self._view_y -= VIEWSPEED
        if keys[pygame.K_DOWN]:
            self._view_y += VIEWSPEED
        if keys[pygame.K_LEFT]:
            self._view_x -= VIEWSPEED
        if keys[pygame.K_RIGHT]:
            self._view_x += VIEWSPEED

        if self._view_x < 0:
            self._view_x = 0
        if self._view_y < 0:
            self._view_y = 0
        if self._view_x > self._map.width:
            self._view_x = self._map.width
        if self._view_y > self._map.height:
            self._view_y = self._map.height

        self._pointer.update((self._view_x, self._view_y))
        self._map.center_window((self._view_x, self._view_y))

    def _scroll_map(self, start_x, start_y, end_x, end_y):
        step_x = (start_x - end_x) / SCROLLSPEED
        step_y = (start_y - end_y) / SCROLLSPEED
        tmp_x = start_x
        tmp_y = start_y
        for _ in range(SCROLLSPEED):
            self._clock.tick(self._fps)
            tmp_x -= step_x
            tmp_y -= step_y
            self._pointer.update((tmp_x, tmp_y))
            self._map.center_window((tmp_x, tmp_y))
            self._draw()

    def _check_obstacle(self):
        # loop tegen de rand van een obstacle aan
        # er mag maar 1 obstacle in deze lijst zijn
        if len(self._player[self._cu].rect.collidelistall(self._map.obstacles)) == 1:
            # obj_nr is het nummer van de betreffende obstacle
            obj_nr = self._player[self._cu].rect.collidelist(self._map.obstacles)
            self._player[self._cu].move_side(self._map.obstacles[obj_nr])

        # loop tegen de rand van een low obstacle aan, bijv water
        if len(self._player[self._cu].rect.collidelistall(self._map.low_obst)) == 1:
            obj_nr = self._player[self._cu].rect.collidelist(self._map.low_obst)
            self._player[self._cu].move_side(self._map.low_obst[obj_nr])

        # loop tegen de rand van je moverange
        if pygame.sprite.collide_mask(self._player[self._cu], self._moverange):
            self._player[self._cu].fallback()

        # loop tegen een obstacle of low_obst aan
        while self._player[self._cu].rect.collidelist(self._map.obstacles) > -1 or \
                self._player[self._cu].rect.collidelist(self._map.low_obst) > -1:
            self._player[self._cu].move_back()

        # voor als je toch perongeluk buiten je moverange komt (niet meer nodig)
        # if abs(self._player[self._cu].rect.top - self._map.start_pos[0].top) > MOVERANGESIZE / 2 or \
        #    abs(self._player[self._cu].rect.left - self._map.start_pos[0].left) > MOVERANGESIZE / 2:
        #     self._player[self._cu].rect.topleft = self._map.start_pos[0].topleft
