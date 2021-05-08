import pygame
import random
from classes import *

pygame.init()

# setting boundary and making the initial quadtree
width = 200
height = 200
boundary = Rectangle(200, 200, width, height)
quadTree = QuadTree(boundary, 4)


# making window for the visualization
windowSetup = Window()
screen = windowSetup.screen()

# generating a bunch of random points and inserting them into quadtree
numRandomPoints = 100
for i in range(numRandomPoints):
    x = int(round(random.uniform(0, windowSetup.width - 1)))
    y = int(round(random.uniform(0, windowSetup.height - 1)))
    point = Point(x, y)
    quadTree.insert(point)
    pygame.draw.circle(screen, (255, 0, 0), point.coordinates, 3, 0)

# keep visualization window running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
