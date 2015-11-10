
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
        pygame.display.set_caption("Press ESC to quit")
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 14)

        self.map = Map('resources/maps/area01/new.tmx', width, height, 3)

        self.player = []
        self.player.append(Hero((0, 0), data.heroes.alagos.BMP))
        self.map.group.add(self.player[0])

        # i = 0
        # for hero_raw in Output.HERO_SORT:
        #     hero = data.heroes[hero_raw]
        #     if hero in data.party:
        #         self.player.append(Hero((200+randint(1, 9)*30, 200+randint(1, 9)*30), hero.BMP))
        #         self.group.add(self.player[i])
        #         i += 1

    def run(self):
        game_over = False
        while not game_over:

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True

            text = "FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(self.clock.get_fps(), " "*5, self.playtime)
            pygame.display.set_caption(text)

            # for i in range(len(self.player)):
            self.player[0].set_speed()
            self.player[0].handle_movement()

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
