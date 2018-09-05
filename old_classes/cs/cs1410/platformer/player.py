from sprite import Sprite
import pygame
import sys

class Player(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Player: must be created from tile object'
            sys.exit(1)
        self.right = True
        self.jump = False
        self.stopped = True
        self.world = world
        self.gid = obj.gid
        self.o_gid = self.gid
        self.new_gid = self.gid
        self.crush = False
        self.screenwidth = 0
        self.teleport = False

        
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
        self.screenwidth = surface.get_width()
    def game_logic(self, keys, newkeys):
        if self.dx == 0.0:
            self.stopped = True
        if self.dy == 0.0:
            self.jump = False
            if pygame.K_UP in newkeys:
                self.addForce('uparrow', (0.0, -70.0), 'onetime')
                self.jump = True
        if pygame.K_DOWN in keys:
            self.addForce('downarrow', (0.0, -3.0), 'onetime')
        if pygame.K_LEFT in keys:
            self.addForce('leftarrow', (-3.0, 0.0), 'onetime')
            self.right = False
        if pygame.K_RIGHT in keys:
            self.addForce('rightarrow', (3.0, 0.0), 'onetime')
            self.right = True
        if pygame.K_f in keys:
            self.crush = True
        if pygame.K_d in keys:
            self.crush = False
        if pygame.K_t in keys:
            if self.teleport:
                self.x = 2085
            
                self.world.x = self.x - self.screenwidth / 2

        self.pswitch += 1
        if self.dy == 0.0:

            if self.pswitch % 4 == 0:
                if not self.right:
#     width of tile set  172
                    self.gid = self.o_gid + 345
                    self.new_gid = self.o_gid + 344
                    self.pswitch = 0
                if self.right:
                    self.gid = self.o_gid
                    self.new_gid = self.o_gid + 1
          #  if self.stopped:
           #     self.gid = self.o_gid + 172
            elif self.pswitch % 2 == 0:
                self.gid = self.new_gid


        (x, y) = (self.x, self.y)
        self.move()

        # move the world to match our motion
        (dx, dy) = (self.x - x, self.y - y)
        self.world.x += dx
        self.world.y += dy

    def handleCollisionWith(self, name, other):
        # stop when we hit a wall/edge
        if name == 'boundary' or name == 'solid':
            return True

        if other.kind == 'coin':
           print 'I got a coin!'
           self.world.removeSprite(other)
           

        if other.kind == 'weakwall':
            if self.crush:
                print 'you brook that wall'
                self.world.removeSprite(other)
            return True
        
        if other.kind == 'door':
            self.teleport = True
            return True

        return False
