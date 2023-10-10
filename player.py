from settings import *
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.k_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.k_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.k_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.k_d]:
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        #Angle control with keys
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
    
    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 20, self.y * 20 ),
                     (self.x * 20 + WIDTH * math.cos(self.angle),
                      self.y * 20 + WIDTH * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen, 'green', (self.x *20, self.y * 20), 15)

    def update(self):
        self.movement()

    @property 
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)