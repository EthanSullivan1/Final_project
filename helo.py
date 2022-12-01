
import pygame
from pygame.sprite import Sprite
class Helo(Sprite):
    """A class to manage the ship"""
    def __init__(self, HVM_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = HVM_game.screen
        self.screen_rect = HVM_game.screen.get_rect()
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/helo.png')
        self.rect = self.image.get_rect()

        #Start each new ship at the center of the screen
        self.rect.center = self.screen_rect.center
        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update moving the ships position based on the movement flag"""
        #updates the ships x/y value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5
        #update the rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
