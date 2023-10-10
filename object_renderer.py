import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image,pos)

    @staticmethod
    def get_texture(path, res = (TEXTURE_SIZE,TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall_textures(self):
        return{
            1:self.get_texture('resources/walls/1_brick_wall.png'),
            2:self.get_texture('resources/walls/2_stone_brick_wall.png'),
            3:self.get_texture('resources/walls/3_grey_brick_wall.png'),
            4:self.get_texture('resources/walls/4_orange_brick_wall.png'),
            5:self.get_texture('resources/walls/5_vegetation_wall.png'),
            6:self.get_texture('resources/walls/6_wood_wall.png'),
            7:self.get_texture('resources/walls/7_fireplace_wall.png'),
            8:self.get_texture('resources/walls/8_library_wall.png')
        }

