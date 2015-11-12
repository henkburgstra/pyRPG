
# todo next unit list
# todo frames en borders
# todo moveranges

import os
from random import randint

import pygame

from battle.hero import Hero
from battle.hero import Pointer
from battle.map import Map
from battle.map import Grid

import data
from output import Output

SCREENSIZE = 1600, 800  # 1920, 1080
WINDOWSIZE = 800, 600
WINDOWPOS = 100, 100

FPS = 60
SCROLLSPEED = 20        # lager is sneller
LAYER = 3

WHITE = 255, 255, 255
BLACK = 0, 0, 0
GRAY = 128, 128, 128


class BattleWindow(object):
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, pygame.DOUBLEBUF)  # | pygame.FULLSCREEN)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(BLACK)
        self.background = self.background.convert()
        self.window = pygame.Surface(WINDOWSIZE)
        self.window = self.window.convert()

        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.font = pygame.font.SysFont('courier', 11)
        self.debug = False

        self.map = Map('resources/maps/area01/new.tmx', LAYER, *WINDOWSIZE)

        self.player = []
        i = 0
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self.player.append(Hero((320+randint(1, 9)*32, 320+randint(1, 9)*32), hero.BMP))
                self.map.group.add(self.player[i])
                self.map.add_obstacle(self.player[i].rect)
                i += 1

        self.cu = 0
        # de obstacle van de player die aan de beurt is weer verwijderen.
        self.map.del_obstacle(self.player[self.cu].rect)

        self.pointer = Pointer()
        self.map.group.add(self.pointer)

        self.grid = Grid(self.map.width, self.map.height)

    def run(self):
        game_over = False
        while not game_over:

            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    if event.key == pygame.K_F10:
                        if self.grid.show:
                            self.grid.show = False
                            self.map.group.remove(self.grid)
                        else:
                            self.grid.show = True
                            self.map.group.add(self.grid)
                    if event.key == pygame.K_F12:
                        if self.debug:
                            self.debug = False
                        else:
                            self.debug = True
                    if event.key == pygame.K_SPACE:
                        self.player[self.cu].align_to_grid()
                    if event.key == pygame.K_c:
                        self.end_of_turn()

            self.player[self.cu].set_speed()
            self.player[self.cu].handle_movement()
            self.check_obstacle()

            self.pointer.update(self.player[self.cu].rect.center)
            self.map.group.center(self.player[self.cu].rect.center)
            self.draw()

        pygame.quit()

    def draw(self):
        self.map.group.draw(self.window)
        if self.debug:
            self.show_debug()
        self.screen.blit(self.window, WINDOWPOS)
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

    def show_debug(self):
        text = ("FPS:         {}".format(int(self.clock.get_fps())),
                "press_up:    {}".format(self.player[self.cu].press_up),
                "press_down:  {}".format(self.player[self.cu].press_down),
                "press_left:  {}".format(self.player[self.cu].press_left),
                "press_right: {}".format(self.player[self.cu].press_right)
                )
        i = 0
        for line in text:
            self.screen.blit(self.font.render(line, True, WHITE), (0, i))
            i += 10

    def end_of_turn(self):
        self.player[self.cu].align_to_grid()
        start_x, start_y = self.player[self.cu].rect.center
        self.map.add_obstacle(self.player[self.cu].rect)
        self.cu += 1
        if self.cu > len(data.party) - 1:
            self.cu = 0
        end_x, end_y = self.player[self.cu].rect.center
        self.map.del_obstacle(self.player[self.cu].rect)
        self.scroll_map(start_x, start_y, end_x, end_y)

    def scroll_map(self, start_x, start_y, end_x, end_y):
        step_x = (start_x - end_x) / SCROLLSPEED
        step_y = (start_y - end_y) / SCROLLSPEED
        tmp_x = start_x
        tmp_y = start_y
        for _ in range(SCROLLSPEED):
            self.clock.tick(self.fps)
            tmp_x -= step_x
            tmp_y -= step_y
            self.pointer.update((tmp_x, tmp_y))
            self.map.group.center((tmp_x, tmp_y))
            self.draw()

    def check_obstacle(self):
        # loop tegen de rand van een obstacle aan
        if self.player[self.cu].rect.collidelist(self.map.obstacles) > -1 and \
                len(self.player[self.cu].rect.collidelistall(self.map.obstacles)) == 1:
                # er mag maar 1 obstacle in deze lijst hierboven zijn
            # obj_nr is het nummer van de betreffende obstacle
            obj_nr = self.player[self.cu].rect.collidelist(self.map.obstacles)
            self.player[self.cu].move_side(self.map.obstacles[obj_nr])

        # loop tegen een obstacle aan
        while self.player[self.cu].rect.collidelist(self.map.obstacles) > -1:
            self.player[self.cu].move_back()
