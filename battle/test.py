

import pygame
from pytmx import load_pygame
import random


white = (255, 255, 255)


# create window
pygame.init()
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("GameName")
screen.fill(white)

tiled_map = load_pygame("../resources/maps/area01/map01_01.tmx")


layer = tiled_map.layers[0]

screen.blit(layer, (0, 0))

# # creates list of single tiles in first layer
# images = []
# for y in range(64):
#     for x in range(64):
#         image = tiled_map.get_tile_image(x, y, 0)
#         images.append(image)
#
# for y in range(64):
#     for x in range(64):
#         image = tiled_map.get_tile_image(x, y, 1)
#         images.append(image)
#
#
# # displays tiles in locations
# i = 0
# for y in range(64):
#     for x in range(64):
#         screen.blit(images[i], (x*16, y*16))
#         i += 1


# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
