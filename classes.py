import pygame

# class for game window
class Window:
    width = 500
    height = 500
    windowScreen = pygame.display.set_mode([width, height])

    def screen(self):
        return self.windowScreen


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (
            point.x >= self.x - self.w
            and point.x < self.x + self.w
            and point.y >= self.y - self.h
            and point.y < self.y + self.h
        )


class QuadTree:
    def __init__(self, boundary, count):
        self.boundary = boundary
        self.capacity = count
        self.points = []
        self.divided = False

    # divide the
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
        pygame.draw.line(Window().screen(), (0, 255, 0), (x, y - h), (x, y + h))
        pygame.draw.line(Window().screen(), (0, 255, 0), (x - w, y), (x + w, y))

        # make 4 new quadtrees
        self.Q1 = QuadTree(q1, self.capacity)
        self.Q2 = QuadTree(q2, self.capacity)
        self.Q3 = QuadTree(q3, self.capacity)
        self.Q4 = QuadTree(q4, self.capacity)

        self.divided = True

    def insert(self, point):
        if self.boundary.contains(point) == False:
            return False
        if len(self.points) > self.capacity:
            self.points.append(point)
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
