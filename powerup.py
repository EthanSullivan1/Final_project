import random

import pygame
from pygame.sprite import Sprite

class Health_power(Sprite):
    """Mange Bullets"""
    def __init__(self, HVM_game):
        """Create a bullet"""
        super().__init__()
        self.screen = HVM_game.screen

        #create a bullet rect at the top the screen

        self.default = pygame.image.load("images/health.png")
        self.image = pygame.transform.scale(self.default, (50,50))
        self.rect = self.image.get_rect()
        self.rect.top = HVM_game.helo.rect.top
        self.rect.x = random.randint(0,1000)
        self.rect.y = 0

        #store the power-ups position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        self.y += 1
        self.rect.y = self.y


    def draw_powerup(self):
        self.screen.blit(self.image, self.rect)