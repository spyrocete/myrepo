
import config
from game import Game
from ship import Ship
from aster import Rock

class Asteroids(Game):
    def __init__(self, name, screen_x, screen_y, frames_per_second):
        Game.__init__(self, name, screen_x, screen_y)
        self.ship =Ship(self.screen)
        self.asteroid_list = []
        while len(self.asteroid_list) < config.ROCK_COUNT:
            self.asteroid_list.append(Rock())

    def game_logic(self, keys, newkeys):
        ## Responsible for updating all game logic ##
        self.ship.game_logic(keys, newkeys)
        
        times = len(self.asteroid_list)
        while times > 0:
            self.asteroid_list[times-1].game_logic(self.ship)
            times = times - 1

    def paint(self, surface):
        ## lets every object draw itself ##
        surface.fill(config.BACKGROUND_COLOR)
        self.ship.paint(surface)
        times = len(self.asteroid_list)
        while times > 0:
            self.asteroid_list[times-1].paint(surface)
            times = times - 1


def main():
    x = Asteroids(config.TITLE, config.SCREEN_X, config.SCREEN_Y,\
                       config.FRAMES_PER_SECOND)
    x.main_loop()


main()
