import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Mange Bullets"""
    def __init__(self, HVM_game):
        """Create a bullet"""
        super().__init__()
        self.screen = HVM_game.screen
        self.color = (60, 60, 60)

        #create a bullet rect at 0,0
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = HVM_game.helo.rect.midright

        #store the bullets position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        self.x += 3
        self.y += 1
        self.rect.x = self.x
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)