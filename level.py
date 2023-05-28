import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row, column in enumerate(WORLD_MAP):
            for col, cell in enumerate(column):
                x = col * TILESIZE
                y = row * TILESIZE
                if cell == 'x':
                    Tile(self, x, y)
                if cell == 'p':
                    Player(self, x, y)

    def run(self):
        # update an draw the game
        pass
