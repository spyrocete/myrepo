from sprite import Sprite
import sys

class Door(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Door: must be created from tile object'
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
        pass
