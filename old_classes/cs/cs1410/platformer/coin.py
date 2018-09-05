from sprite import Sprite
import sys

class Coin(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Coin: must be created from tile object'
            sys.exit(1)
        self.world = world
        self.gid = obj.gid
        self.o_gid = self.gid
        tile = world.data.tiles[self.gid]

        Sprite.__init__(self,
                world,
                obj.kind,
                '{} ({},{})'.format(obj.kind, obj.x, obj.y),
                tile.get_width(), tile.get_height(),
                obj.x, obj.y,
                (0.0, 0.0))

    def paint(self, surface):
        self.paintTile(surface, self.world.data.tiles[self.gid])

    def game_logic(self, keys, newkeys):
        self.switch += 1
        if self.switch % 30 == 0:
            self.gid += 1
            self.switch = 0
        elif self.switch % 15 == 0:
            self.gid = self.o_gid

class Door(Coin):
    def __init__():
        Coin.__init__(self, world, obj)
    
        Coin.paint(self, surface)
        Coin.game_logic(self, keys, newkeys)

