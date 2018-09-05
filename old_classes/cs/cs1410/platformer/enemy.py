from sprite import Sprite
import pygame
import sys

class Enemy(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Player: must be created from tile object'
            sys.exit(1)
       
        self.right = True
        self.world = world
        self.gid = obj.gid
        self.o_gid = self.gid
        self.new_gid = self.gid
        tile = world.data.tiles[self.gid]

        Sprite.__init__(self,
                world,
                obj.kind,
                '{} ({},{})'.format(obj.kind, obj.x, obj.y),
                tile.get_width(), tile.get_height(),
                obj.x, obj.y,
                (16.0, 16.0))
        self.addForce('friction', (1.0, 0.0), 'slowdown')
        self.addForce('gravity', (0.0, 1.0), 'constant')

    def paint(self, surface):
        self.paintTile(surface, self.world.data.tiles[self.gid])

    def game_logic(self,keys, newkeys):
        if self.right:
            self.x += 1
            if "boundary" in self.world.findCollisions(self) or "solid" in self.world.findCollisions(self):
                self.dx = -2.0
                self.right = False
        else: 
            self.x -= 1
            if "boundary" in self.world.findCollisions(self) or "solid" in self.world.findCollisions(self):
                self.dx = 2.0
                self.right = True
            

        self.pswitch += 1
        if self.pswitch % 4 == 0:
            if self.right:
                self.gid = self.o_gid -344
                self.new_gid = self.gid + 1
            if not self.right:
                self.gid = self.o_gid 
                self.new_gid = self.gid +1
            self.pswitch = 0
        elif self.pswitch % 2 == 0:
            self.gid = self.new_gid 

        (x, y) = (self.x, self.y)
        self.move()
        return False



    def handleCollisionWith(self, name, other):
        # stop when we hit a wall/edge
      
        if name == 'boundary' or name == 'solid':           
            return True
        
        if other.kind == 'player':
            print 'You died'
            self.world.removeSprite(other)
           # pygame.quit()
        
