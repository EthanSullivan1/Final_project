import pygame
from settings import Settings

class C_screen():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.C_screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Helicopter VS Man")
        self.c_screen_rect = self.C_screen.get_rect()
        self.image = pygame.image.load("images/Game_controls.jpg")
        self.scaled_image = pygame.transform.scale(self.image, (1280, 720))
        self.image_rect = self.scaled_image.get_rect()

    def draw(self):
        self.C_screen.blit(self.scaled_image, self.c_screen_rect)
        pygame.display.flip()