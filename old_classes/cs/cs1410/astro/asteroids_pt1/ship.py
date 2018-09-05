import pygame
import config
import math
from random import randint,uniform
from polygon import Polygon
from point import Point

class Ship(Polygon):
    def __init__(self,surface):
        ship_points = [Point(25,0), Point(-20,8), Point(-25,0), Point(-20,-8)]
        Polygon.__init__(self, ship_points, Point(config.SCREEN_X/2,config.SCREEN_Y/2), config.SHIP_INITIAL_DIRECTION, config.SHIP_COLOR)
        self.pull = Point(0,0)
        self.rotation +=360
        self.rotation = self.rotation%360
        self.shield = 5
        self.screen = surface
##    def __init__(self, position, rotation, color):
##        self.position = position
##        self.rotation = rotation
##        self.points = []
##        self.color = color
##        outline = [(4,0),(3,1),(2,0),(0,1),(-3,2),(0,-1),(1,0),(4,0)]
##        for i in outline:
##            self.points.append(Point(i[0], i[1]))
##        Polygon.__init__(self.outline, self.position, self.rotation, self.color)


##    def paint(self, surface):
##        outline = []
##        points = self.getPoints();
##        for i in points:
##            outline.append(i.pair())
##        pygame.draw.polygon(surface,Polygon.color, outline, width=0)

    def acceleration(self, pos):
        x = self.pull.x + pos * math.cos(math.radians(self.rotation))
        y = self.pull.y + pos * math.sin(math.radians(self.rotation))

        self.pull = Point(x,y)
                        

    def game_logic(self, keys, newkeys):
        if pygame.K_LEFT in keys:
            self.rotate(-config.SHIP_ROTATION_RATE)
        if pygame.K_RIGHT in keys:
            self.rotate(config.SHIP_ROTATION_RATE)
        if pygame.K_UP in keys:
            self.acceleration(config.SHIP_ACCELERATION_RATE)
        if pygame.K_DOWN in keys:
            self.acceleration(-config.SHIP_ACCELERATION_RATE)

        self.move()
