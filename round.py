import pygame
from pygame.sprite import Sprite

class Round(Sprite):
    """Mange Rounds"""
    def __init__(self, HVM_game):
        """Create a round"""
        super().__init__()
        self.screen = HVM_game.screen
        self.color = (255, 0, 0)

        #create a round rect at 0,0
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midleft = HVM_game.tank.rect.midleft

        #store the rounds position
        self.x = float(self.rect.x)

    def update(self):
        """move the bullet up the screen"""
        self.x -= 5
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)