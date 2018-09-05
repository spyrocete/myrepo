import game
import coin
import player
import mapfile
import world
import pygame
import enemy
import enemy2
import weakwall
import door

class Platformer(game.Game):
    def __init__(self, name, map_filename, width, height, frames_per_second):
        game.Game.__init__(self, name, width, height, frames_per_second)

        # parse the map data
        data = mapfile.MapFile(map_filename)

        # create the world
        self.world = world.World(data)

        # create the sprites
        for elt in data.objects:
            # is this the player?
            if elt.kind == 'player':
                p = player.Player(self.world, elt)
               
                self.world.addSprite(p)
               

                # the world revolves around the player
                self.world.x = p.x + p.width / 2 - width / 2
                self.world.y = p.y + p.height / 2 - height / 2

            # is this a coin?
            elif elt.kind == 'coin':
                c = coin.Coin(self.world, elt)
                self.world.addSprite(c)

            elif elt.kind == 'enemy':
                e = enemy.Enemy(self.world, elt)
                self.world.addSprite(e)
            
            elif elt.kind == 'enemy2':
                e2 = enemy2.Enemy2(self.world, elt)
                self.world.addSprite(e2)
            
            
            elif elt.kind == 'weakwall':
                w = weakwall.Weakwall(self.world, elt)
                self.world.addSprite(w)

            elif elt.kind == 'door':
                d = door.Door(self.world, elt)
                self.world.addSprite(d)


            else:
                print 'Sprite of unknown type {} found'.format(elt.kind)

    def game_logic(self, keys, newkeys):
        self.world.game_logic(keys, newkeys)

    def paint(self, surface):
        self.world.paint(surface)

def main():
    p = Platformer('Pally', 'simplemap.tmx', 480, 480, 30)
    p.main_loop()

main()
