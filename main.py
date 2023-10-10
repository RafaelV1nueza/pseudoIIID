import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)                          #Set Resolution
        self.clock = pg.time.Clock()                                    #Initialize clock ingame
        self.delta_time = 1                                             #Initialize delta time(time between frames)
        self.new_game()                                                 #new instance of game

    def new_game(self):
        self.map = Map(self)                                            #Initialize map class
        self.player = Player(self)                                      #Initialize player class    
        self.raycasting = RayCasting(self)                                  #Initialize raycasting in game

    def update(self):
        self.player.update()                                            #Update player angle and X,y
        self.raycasting.update()                                        # Update raycast
        pg.display.flip()                                               #Update display
        self. delta_time = self.clock.tick(FPS)                         #Set delta time to time between fps tick
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')          #Caption game window with fps

    def draw(self):
        self.screen.fill('black')                                       #black screen
        self.map.draw()                                                 #draw instance in map class
        self.player.draw()                                              #draw player

    def check_event(self):
        for event in pg.event.get():                                    #Exit game propery
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT()
                sys.exit()     

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()