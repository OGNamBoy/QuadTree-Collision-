import pygame
import random
from classes import *

pygame.init()


width = 400
height = 400
boundary = Rectangle(200, 200, 200, 200)
quadTree = QuadTree(boundary, 4)
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.draw.circle(screen, (255, 0, 0), event.pos, 3, 0)
            point = Point(event.pos[0], event.pos[1])
            quadTree.insert(point)
        elif event.type == pygame.QUIT:
            running = False
    pygame.display.update()
