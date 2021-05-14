# file that stores all the classes to be used in other files

import pygame
from scipy.spatial import distance

# class for game window so i can update the size and have it transfer to other files
class Window:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode([self.width, self.height])


# class for colors for easier readability in other files
class Colors:
    def __init__(self):
        self.Red = (255, 0, 0)
        self.Green = (0, 255, 0)
        self.Blue = (0, 0, 255)
        self.Black = (0, 0, 0)
        self.White = (255, 255, 255)


class Point:
    def __init__(self, x, y, directionX, directionY):
        self.x = x
        self.y = y
        self.r = 4
        self.coordinates = (x, y)
        self.xDirection = directionX
        self.yDirection = directionY
        self.highlight = False

    # draw the points on the screen
    def render(self):
        if self.highlight == False:
            pygame.draw.circle(
                Window().screen, Colors().Red, self.coordinates, self.r, 0
            )

        else:
            pygame.draw.circle(
                Window().screen, Colors().Blue, self.coordinates, self.r, 0
            )

    # used for render function to determine color of point
    def setHighlight(self, value):
        self.highlight = value

    # checks if two points are touching
    def intersects(self, other):
        p = (self.x, self.y)
        op = (other.x, other.y)
        d = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return d < (self.r + other.r) ** 2


# rectangle class primarily used to set boundaries of the quadTree
# can also be used to create a range for querying in the shape of a rectangle
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # check if point is contained within the rectangle
    def contains(self, point):
        return (
            point.x >= self.x - self.w
            and point.x < self.x + self.w
            and point.y >= self.y - self.h
            and point.y < self.y + self.h
        )


# class to create a range for querying in the shape of a circle
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.rSquared = self.r * self.r

    # check if point is within the boundary
    def contains(self, point):
        d = (self.x - point.x) ** 2 + (self.y - point.y) ** 2
        return d <= self.rSquared

    # check if made circle intersects with part of the quadTree
    def intersects(self, range):
        xDistance = abs(range.x - self.x)
        yDistance = abs(range.y - self.y)

        r = self.r
        w = range.w
        h = range.h
        edges = (xDistance - w) ** 2 + (yDistance - h) ** 2
        if xDistance > (r + w) or yDistance > (r + h):
            return False

        if xDistance <= w or yDistance <= h:
            return True

        return edges <= self.rSquared


class QuadTree:
    def __init__(self, boundary, count):
        self.boundary = boundary
        self.capacity = count
        self.points = []
        self.divided = False

    # divide the quadtree into 4 subtrees
    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        # divide the quadtree into 4 rectangles
        q1 = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        q2 = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        q3 = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        q4 = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)

        # draw the lines for the division
        pygame.draw.line(Window().screen, Colors().Green, (x, y - h), (x, y + h))
        pygame.draw.line(Window().screen, Colors().Green, (x - w, y), (x + w, y))

        # make 4 new quadtrees
        self.Q1 = QuadTree(q1, self.capacity)
        self.Q2 = QuadTree(q2, self.capacity)
        self.Q3 = QuadTree(q3, self.capacity)
        self.Q4 = QuadTree(q4, self.capacity)

        self.divided = True

    # insert a point into a quadtree or its subtrees
    def insert(self, point):
        if self.boundary.contains(point) == False:
            return False
        # if capacity isn't full, insert into the quadTree
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        # if capacity is full, subdivide then insert into one of the subTrees
        else:
            if self.divided == False:
                self.subdivide()
            if self.Q1.insert(point):
                return True
            elif self.Q2.insert(point):
                return True
            elif self.Q3.insert(point):
                return True
            elif self.Q4.insert(point):
                return True

    # return all points within a given range
    def query(self, range, found):
        if range.intersects(self.boundary) == False:
            return found
        else:
            for p in self.points:
                if range.contains(p) == True:
                    found.append(p)
        if self.divided == True:
            self.Q1.query(range, found)
            self.Q2.query(range, found)
            self.Q3.query(range, found)
            self.Q4.query(range, found)

        return found
