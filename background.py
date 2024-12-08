import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (255, 255, 255)
        self.coordinates = (0, 0)
        self.size = 3
        self.random_coordinates()
        self.random_radius()
        self.random_color()

    def random_coordinates(self):
        self.coordinates = (random.randint(0, self.settings.screen_width),
            random.randint(0, self.settings.screen_height))

    def random_radius(self):
        self.size = random.randint(1, 2)

    def random_color(self):
        rg = random.randint(100, 255)
        self.color = (rg, rg,
                        random.randint(150, 255))

    def draw_star(self):
        pygame.draw.circle(self.screen, self.color, self.coordinates, self.size)