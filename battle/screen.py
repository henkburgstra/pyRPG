
# todo next unit list
# todo frames en borders
# todo moveranges

import os
from random import randint

import pygame

from battle.map import Map
from battle.hero import Hero
from battle.drawings import Pointer

import data
from output import Output

SCREENSIZE = 1600, 800  # 1920, 1080
WINDOWSIZE = 800, 600
WINDOWPOS = 100, 100

FPS = 60
SCROLLSPEED = 20        # lager is sneller
DEFAULTLAYER = 3
POINTERLAYER = 4
GRIDSIZE = 16

WHITE = 255, 255, 255
BLACK = 0, 0, 0


class BattleWindow(object):
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self._screen = pygame.display.set_mode(SCREENSIZE, pygame.DOUBLEBUF)  # | pygame.FULLSCREEN)
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(BLACK)
        self._background = self._background.convert()
        self._window = pygame.Surface(WINDOWSIZE)
        self._window = self._window.convert()

        self._clock = pygame.time.Clock()
        self._fps = FPS
        self._font = pygame.font.SysFont('courier', 11)

        self._debug = False

        self._map = Map('resources/maps/area01/new.tmx', DEFAULTLAYER, *WINDOWSIZE)

        self._player = []
        i = 0
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self._player.append(Hero((320 + randint(1, 9) * 32, 320 + randint(1, 9) * 32), hero.BMP))
                self._map.group.add(self._player[i])
                self._map.add_object(self._player[i].rect, self._map.heroes)
                self._map.add_object(self._player[i].rect, self._map.obstacles)
                i += 1

        self._cu = 0
        # de obstacle van de player die aan de beurt is weer verwijderen.
        self._map.add_object(self._player[self._cu].rect, self._map.start_pos)
        self._map.del_object(self._player[self._cu].rect, self._map.heroes)
        self._map.del_object(self._player[self._cu].rect, self._map.obstacles)

        self._pointer = Pointer(POINTERLAYER)
        self._map.group.add(self._pointer)

    def run(self):
        game_over = False
        while not game_over:

            self._clock.tick(self._fps)

            for event in pygame.event.get():
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
                    if event.key == pygame.K_c:
                        self._end_of_turn()

            self._player[self._cu].set_speed()
            self._player[self._cu].handle_movement()
            self._check_obstacle()

            self._pointer.update(self._player[self._cu].rect.center)
            self._map.group.center(self._player[self._cu].rect.center)
            self._draw()

        pygame.quit()

    def _draw(self):
        self._map.group.draw(self._window)
        self._screen.blit(self._window, WINDOWPOS)
        if self._debug:
            self._show_debug()
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))

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
                "start_pos.x:    {}".format(self._map.start_pos[0].left),
                "start_pos.y     {}".format(self._map.start_pos[0].top),
                "player.x:       {}".format(self._player[self._cu].rect.left),
                "player.y:       {}".format(self._player[self._cu].rect.top),
                "step_count:     {}".format(self._player[self._cu]._step_count),
                "step_animation: {}".format(self._player[self._cu]._step_animation),
                "step_delay:     {}".format(self._player[self._cu]._step_delay),
                )
        i = 0
        for line in text:
            self._screen.blit(self._font.render(line, True, WHITE), (0, i))
            i += 10

    def _end_of_turn(self):
        self._player[self._cu].align_to_grid(GRIDSIZE)
        start_x, start_y = self._player[self._cu].rect.center
        self._map.add_object(self._player[self._cu].rect, self._map.heroes)
        self._map.add_object(self._player[self._cu].rect, self._map.obstacles)
        self._map.start_pos = []
        self._cu += 1
        if self._cu > len(data.party) - 1:
            self._cu = 0
        end_x, end_y = self._player[self._cu].rect.center
        self._map.del_object(self._player[self._cu].rect, self._map.heroes)
        self._map.del_object(self._player[self._cu].rect, self._map.obstacles)
        self._map.add_object(self._player[self._cu].rect, self._map.start_pos)
        self._scroll_map(start_x, start_y, end_x, end_y)
        self._map.show_info(0)

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
            self._map.group.center((tmp_x, tmp_y))
            self._draw()

    def _check_obstacle(self):
        # loop tegen de rand van een obstacle aan
        if self._player[self._cu].rect.collidelist(self._map.obstacles) > -1 and \
                len(self._player[self._cu].rect.collidelistall(self._map.obstacles)) == 1:
                # er mag maar 1 obstacle in deze lijst hierboven zijn
            # obj_nr is het nummer van de betreffende obstacle
            obj_nr = self._player[self._cu].rect.collidelist(self._map.obstacles)
            self._player[self._cu].move_side(self._map.obstacles[obj_nr])

        # loop tegen een obstacle aan
        while self._player[self._cu].rect.collidelist(self._map.obstacles) > -1:
            self._player[self._cu].move_back()
