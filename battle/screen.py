
import os
from random import randint

import pygame

from battle.hero import Hero
from battle.map import Map

import data
from output import Output


class BattleWindow(object):
    def __init__(self, width=900, height=800, fps=60):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.font = pygame.font.SysFont('mono', 14)

        self.map = Map('resources/maps/area01/new.tmx', width, height, 3)

        self.player = []
        self.player.append(Hero((320, 320), data.heroes.alagos.BMP))
        self.map.group.add(self.player[0])

        # i = 0
        # for hero_raw in Output.HERO_SORT:
        #     hero = data.heroes[hero_raw]
        #     if hero in data.party:
        #         self.player.append(Hero((320+randint(1, 9)*30, 320+randint(1, 9)*30), hero.BMP))
        #         self.map.group.add(self.player[i])
        #         i += 1

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

            text = "Press ESC to quit.{}FPS: {:6.3}".format(" "*5, self.clock.get_fps())
            pygame.display.set_caption(text)

            # for i in range(len(self.player)):
            self.player[0].set_speed()
            self.player[0].handle_movement()

            # loop tegen de rand van een wall aan
            if self.player[0].rect.collidelist(self.map.walls) > -1 and \
                    len(self.player[0].rect.collidelistall(self.map.walls)) == 1:   # er mag maar 1 wall in de lijst
                obj_nr = self.player[0].rect.collidelist(self.map.walls)            # obj_nr is het nr van de betr. wall
                self.player[0].move_side(self.map.walls[obj_nr])

            # loop tegen een wall aan
            while self.player[0].rect.collidelist(self.map.walls) > -1:
                self.player[0].move_back()

            self.map.group.center(self.player[0].rect.center)
            self.map.group.draw(self.screen)

            # self.screen.blit(self.font.render("press_up: {}".format(self.player[0].press_up),
            #                                   True, (0, 0, 0)), (0, 0))
            # self.screen.blit(self.font.render("press_down: {}".format(self.player[0].press_down),
            #                                   True, (0, 0, 0)), (0, 20))
            # self.screen.blit(self.font.render("press_left: {}".format(self.player[0].press_left),
            #                                   True, (0, 0, 0)), (0, 40))
            # self.screen.blit(self.font.render("press_right: {}".format(self.player[0].press_right),
            #                                   True, (0, 0, 0)), (0, 60))

            pygame.display.flip()

        pygame.quit()
