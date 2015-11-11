
# todo fullscreen
# todo fps naar debug
# todo debug transparant ondergrond
# todo next unit list
# todo frames en borders

import os
from random import randint

import pygame

from battle.hero import Hero
from battle.hero import Pointer
from battle.map import Map

import data
from output import Output


SCROLLSPEED = 120


class BattleWindow(object):
    def __init__(self, width=900, height=800, fps=60):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.w, self.h = width, height
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.font = pygame.font.SysFont('courier', 11)

        self.map = Map('resources/maps/area01/new.tmx', self.w, self.h, 3)

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

    def run(self):
        debug = False
        game_over = False
        while not game_over:

            self.clock.tick(self.fps)
            text = "Press ESC to quit.{}FPS: {:6.3}".format(" "*5, self.clock.get_fps())
            pygame.display.set_caption(text)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    if event.key == pygame.K_F12:
                        if debug:
                            debug = False
                        else:
                            debug = True
                    if event.key == pygame.K_SPACE:
                        self.player[self.cu].align_to_grid()
                    if event.key == pygame.K_c:
                        self.end_of_turn()

            self.player[self.cu].set_speed()
            self.player[self.cu].handle_movement()
            self.check_obstacle()

            self.pointer.update(self.player[self.cu].rect.center)
            self.map.group.center(self.player[self.cu].rect.center)
            self.map.group.draw(self.screen)
            if debug:
                self.debug()

            pygame.display.flip()

        pygame.quit()

    def debug(self):
        self.screen.blit(self.font.render("press_up:    {}".format(self.player[self.cu].press_up),
                                          True, (255, 255, 255)), (0, 0))
        self.screen.blit(self.font.render("press_down:  {}".format(self.player[self.cu].press_down),
                                          True, (255, 255, 255)), (0, 10))
        self.screen.blit(self.font.render("press_left:  {}".format(self.player[self.cu].press_left),
                                          True, (255, 255, 255)), (0, 20))
        self.screen.blit(self.font.render("press_right: {}".format(self.player[self.cu].press_right),
                                          True, (255, 255, 255)), (0, 30))

    def end_of_turn(self):
        self.player[self.cu].align_to_grid()
        start_x, start_y = self.player[self.cu].rect.center
        self.map.add_obstacle(self.player[self.cu].rect)
        self.cu += 1
        if self.cu > 4:
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
            tmp_x -= step_x
            tmp_y -= step_y
            self.pointer.update((tmp_x, tmp_y))
            self.map.group.center((tmp_x, tmp_y))
            self.map.group.draw(self.screen)
            pygame.display.flip()

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
