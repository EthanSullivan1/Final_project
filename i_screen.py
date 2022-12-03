
import pygame
from settings import Settings

class I_screen():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.i_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Helicopter VS Man")
        self.i_screen_rect = self.i_screen.get_rect()
        self.image = pygame.image.load("images/tanks_tankDesert2.png")
    def draw(self):
        self.i_screen.fill((0,0,0))
        self.i_screen.blit(self.image, self.i_screen_rect.center)
        pygame.display.flip()