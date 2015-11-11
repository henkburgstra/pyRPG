
import os
from random import randint

import pygame

from battle.hero import Hero
from battle.hero import Pointer
from battle.map import Map

import data
from output import Output


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
                self.map.walls.append(pygame.Rect(self.player[i].rect.x, self.player[i].rect.y,
                                                  self.player[i].rect.width, self.player[i].rect.height))
                i += 1

        self.cu = 0

        self.pointer = Pointer(self.player[self.cu].rect.center)
        self.map.group.add(self.pointer)

        # de walls van de player die aan de beurt is weer verwijderen.
        self.map.walls.remove(pygame.Rect(self.player[self.cu].rect.x, self.player[self.cu].rect.y,
                                          self.player[self.cu].rect.width, self.player[self.cu].rect.height))

    def run(self):
        debug = False
        game_over = False
        while not game_over:

            self.clock.tick(self.fps)

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
                        self.player[self.cu].align_to_grid()
                        self.map.walls.append(pygame.Rect(self.player[self.cu].rect.x,
                                                          self.player[self.cu].rect.y,
                                                          self.player[self.cu].rect.width,
                                                          self.player[self.cu].rect.height))
                        self.cu += 1
                        if self.cu > 4:
                            self.cu = 0
                        self.map.walls.remove(pygame.Rect(self.player[self.cu].rect.x,
                                                          self.player[self.cu].rect.y,
                                                          self.player[self.cu].rect.width,
                                                          self.player[self.cu].rect.height))

            text = "Press ESC to quit.{}FPS: {:6.3}".format(" "*5, self.clock.get_fps())
            pygame.display.set_caption(text)

            self.player[self.cu].set_speed()
            self.player[self.cu].handle_movement()

            # loop tegen de rand van een wall aan
            if self.player[self.cu].rect.collidelist(self.map.walls) > -1 and \
                    len(self.player[self.cu].rect.collidelistall(self.map.walls)) == 1:
                    # er mag maar 1 wall in deze lijst hierboven zijn
                obj_nr = self.player[self.cu].rect.collidelist(self.map.walls)  # obj_nr is het nr van de betr. wall
                self.player[self.cu].move_side(self.map.walls[obj_nr])

            # loop tegen een wall aan
            while self.player[self.cu].rect.collidelist(self.map.walls) > -1:
                self.player[self.cu].move_back()

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
