# program that generates random points with random velocities
# and uses a quadTree to detect collisions

import pygame
import random
from classes import *

pygame.init()
pygame.display.set_caption("Quad-Tree Collision Detection")

# create the window and save its width and height
window = Window()
width = window.width
height = window.height
screen = window.screen

# create a list of particles
particles = [0] * 150
for i in range(len(particles)):
    # create x and y points for the particles based on the window height and
    x = random.randint(0 + Point(0, 0, 0, 0).r, width - Point(0, 0, 0, 0).r)
    y = random.randint(0 + Point(0, 0, 0, 0).r, height - Point(0, 0, 0, 0).r)
    # randomly choose trajectory of the particle
    xDir = random.randint(1, 3)
    yDir = random.randint(1, 3)
    # add particle to list
    particles[i] = Point(x, y, xDir, yDir)

# master loop for visualization of the screen
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(500)

    # make initial quadtree with the size of the screen
    boundary = Rectangle(width / 2, width / 2, width / 2, height / 2)
    quadTree = QuadTree(boundary, 4)

    for i in range(len(particles)):
        # if the particle hits one of side edges, invert the x direction
        if (
            particles[i].x >= window.width - particles[i].r
            or particles[i].x <= 0 + particles[i].r
        ):
            particles[i].xDirection = -particles[i].xDirection
        # if particle hits one of the top or bottom edges, change the y direction
        if (
            particles[i].y >= window.height - particles[i].r
            or particles[i].y <= 0 + particles[i].r
        ):
            particles[i].yDirection = -particles[i].yDirection
        # update the position of the particle
        particles[i] = Point(
            particles[i].x + particles[i].xDirection,
            particles[i].y + particles[i].yDirection,
            particles[i].xDirection,
            particles[i].yDirection,
        )
        # insert particle into the quadTree
        quadTree.insert(particles[i])

    for j in range(len(particles)):
        # create a circle shaped range with twice the radius
        circle = Circle(particles[j].x, particles[j].y, particles[j].r * 2)
        pointsInRange = []
        # return points that are within the range
        points = quadTree.query(circle, pointsInRange)
        for point in points:
            # if the particle intersects with others in the range, draw them in blue
            if particles[j].coordinates != point.coordinates and particles[
                j
            ].intersects(point):
                particles[j].setHighlight(True)

        # draw all particles, red being non collided particles
        particles[j].render()

    # keep the window running until you exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    screen.fill(Colors().Black)
