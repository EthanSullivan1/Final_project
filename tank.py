
import pygame
import sys
class Tank:
    """A class to manage the ship"""
    def __init__(self, HVM_game):
        """Initialize the ship and set its starting position."""
        self.screen = HVM_game.screen
        self.screen_rect = HVM_game.screen.get_rect()
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/tanks_tankDesert2.png')
        self.life1 = pygame.image.load('images/Life_1.png')
        self.life2 = pygame.image.load('images/Life_2.png')
        self.life3 = pygame.image.load('images/Life_3.png')
        self.lost = pygame.image.load('images/lost_life.png')
        self.rect = self.image.get_rect()
        self.lives_left = 3
        self.tank_health = 30
        #Start each new ship at the bottom right of the screen
        self.rect.bottomright = self.screen_rect.bottomright
        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update moving the ships position based on the movement flag"""
        #updates the ships x/y value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5

        #update the rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y - 30

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, (self.rect))

    def draw_lives(self):
        if self.tank_health <= 0:
            self.screen.blit(self.lost, (975,40))
            self.screen.blit(self.lost, (1075, 40))
            self.screen.blit(self.lost, (1175, 40))
            sys.exit()
        elif self.tank_health <= 10:
            self.screen.blit(self.life1, (975,40))
            self.screen.blit(self.lost, (1075, 40))
            self.screen.blit(self.lost, (1175, 40))
        elif self.tank_health <= 20:
            self.screen.blit(self.life1, (975,40))
            self.screen.blit(self.life2, (1075, 40))
            self.screen.blit(self.lost, (1175, 40))
        elif self.tank_health <= 30:
            self.screen.blit(self.life1, (975,40))
            self.screen.blit(self.life2, (1075, 40))
            self.screen.blit(self.life3, (1175, 40))

