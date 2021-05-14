# program that takes user mouse input to insert points into a quadTree

import pygame
from classes import *

pygame.init()

window = Window()
width = window.width
height = window.height
screen = window.screen
boundary = Rectangle(width / 2, width / 2, width / 2, height / 2)
quadTree = QuadTree(boundary, 4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:

            point = Point(event.pos[0], event.pos[1], 0, 0)
            pygame.draw.circle(screen, Colors().Red, event.pos, 3, 0)
            quadTree.insert(point)

        elif event.type == pygame.QUIT:
            running = False
    pygame.display.update()
