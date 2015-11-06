
import os
from random import randint

import pygame
import pytmx
import pyscroll
import pyscroll.data

from battle.hero import Hero
from battle.map import Background

import data
from output import Output


class BattleWindow(object):
    def __init__(self, width=800, height=600, fps=60):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        tmx_data = pytmx.load_pygame('resources/maps/area01/new.tmx')
        self.walls = []
        for an_object in tmx_data.objects:
            self.walls.append(pygame.Rect(an_object.x, an_object.y, an_object.width, an_object.height))
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, (self.width, self.height), clamp_camera=True)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 14)

        # self.background = Background('resources/maps/area01/map01_01.png', [0, 0])

        self.player = []
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self.player.append(Hero((200+randint(1, 9)*30, 200+randint(1, 9)*30), hero.BMP))

        self.group.add(self.player[0])

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

            self.player[0].handle_movement()

            text = "FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(self.clock.get_fps(), " "*5, self.playtime)
            pygame.display.set_caption(text)

            self.screen.blit(self.background.image, self.background.rect)
            for i in range(len(self.player)):
                self.screen.blit(self.player[i].image, self.player[i].rect)

            # self.screen.blit(self.font.render("press_up: {}".format(self.player.press_up),
            #                                   True, (0, 0, 0)), (0, 0))
            # self.screen.blit(self.font.render("press_down: {}".format(self.player.press_down),
            #                                   True, (0, 0, 0)), (0, 20))
            # self.screen.blit(self.font.render("press_left: {}".format(self.player.press_left),
            #                                   True, (0, 0, 0)), (0, 40))
            # self.screen.blit(self.font.render("press_right: {}".format(self.player.press_right),
            #                                   True, (0, 0, 0)), (0, 60))

            pygame.display.flip()

        pygame.quit()
