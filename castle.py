import pygame
from pygame.sprite import Sprite


class Castle(Sprite):
    #Makes a castle
    def __init__(self):
        super().__init__()
        self.undam = pygame.image.load("images/castle.png")
        self.light_dam = pygame.image.load("images/Light_dam_castle.png")
        self.heavy_dam = pygame.image.load("images/heavy_dam_castle.png")
        self.destroyed = pygame.image.load("images/destroyed_castle.png")
        self.image = self.undam
        self.rect = self.image.get_rect()
        self.current_health = 2999
        self.target_health = 3000
        self.max_health = 3000
        self.health_bar_length = 400
        self.health_ratio = self.max_health/self.health_bar_length
        self.health_change_speed = 5



    def draw(self, surface):
        if self.current_health <= 0:
            self.image = self.destroyed
        elif self.current_health < 1000:
            self.image = self.heavy_dam
        elif self.current_health< 2000:
            self.image = self.light_dam
        elif self.current_health <= 3000:
            self.image = self.undam
        elif self.current_health <= 0:
            self.game_active = False
        surface.blit(self.image, (0, 500))
    def get_damage(self):
        if self.target_health > 0:
            self.target_health -= 5
            self.current_health = self.target_health


