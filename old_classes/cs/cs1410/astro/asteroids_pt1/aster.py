import config
import pygame
import math
from random import randint, uniform, choice
from polygon import Polygon
from point import Point


class Rock(Polygon):
    def __init__(self):
        self.shield = 0
        posxran = randint(0,1)
        posyran = randint(0,1)
        
        if posxran and posyran:
            pos = Point(randint(0, config.SCREEN_X/2-50),randint(0, config.SCREEN_Y/2-50))
        if posxran and not posyran:
            pos = Point(randint(0, config.SCREEN_X/2-50),randint(config.SCREEN_Y/2+50,config.SCREEN_Y))            
        if posyran and not posxran:
            pos = Point(randint(config.SCREEN_X/2+50,config.SCREEN_X),randint(0, config.SCREEN_Y/2-50))
        if not posxran and not posyran:
            pos = Point(randint(config.SCREEN_X/2+50,config.SCREEN_X),randint(config.SCREEN_Y/2+50,config.SCREEN_Y))
        
        rotation = uniform(0.0,359.99)
        self.pull = Point(float(uniform(-1,1))*uniform(config.ROCK_MIN_SPEED, config.ROCK_MAX_SPEED),
                          float(uniform(-1,1))*uniform(config.ROCK_MIN_SPEED, config.ROCK_MAX_SPEED))
        self.rotationspeed = choice([1,-1]) * uniform(config.ROCK_MIN_ROTATION_SPEED,
                                config.ROCK_MAX_ROTATION_SPEED)

        shape = []
        s = randint(1,3)
        if s == 1:
            ## origional asteroids
            for rad_points in range(config.ROCK_POLYGON_SIZE+1):
                radius = uniform(config.ROCK_MIN_RADIUS, config.ROCK_MAX_RADIUS)
                radian = math.radians(rad_points*360/config.ROCK_POLYGON_SIZE)
                x = math.cos(radian)*radius
                y = math.sin(radian)*radius
                shape.append(Point(x,y))

        if s == 2:
            ##square
            size = (uniform(config.ROCK_MIN_RADIUS, config.ROCK_MAX_RADIUS)+config.ROCK_POLYGON_SIZE)*2
            shape = [Point(-size/2,-size/2),Point(-size/2,size/2),Point(size/2,size/2),Point(size/2,-size/2)]
            
        if s == 3:
            ##triangle
            size = (uniform(config.ROCK_MIN_RADIUS, config.ROCK_MAX_RADIUS)+config.ROCK_POLYGON_SIZE)*2
            shape = [Point(0,size/2),Point(-size/2,-size/2),Point(size/2,-size/2)]
        Polygon.__init__(self, shape, pos, rotation, config.ROCK_COLOR)


    def collide(self,ship):
        if self.active:
            sship = ship
            ship = ship.getPoints()
            if self.contains(ship[0]) or self.contains(ship[1]) or self.contains(ship[2]) or self.contains(ship[3]):
                sship.shield -= 1
                print sship.shield
                self.active = False

    
    def game_logic(self,ship):
        if not self.active:
            return
        self.rotate(self.rotationspeed)
        self.move()
        self.collide(ship)
