import pygame

class Castle():
    #Makes a castle
    def __init__(self):
        self.undam = pygame.image.load("images/castle.png")
        self.light_dam = pygame.image.load("images/Light_dam_castle.png")
        self.heavy_dam = pygame.image.load("images/heavy_dam_castle.png")
        self.destroyed = pygame.image.load("images/destroyed_castle.png")
        self.image = self.undam
        self.rect = self.image.get_rect()
        self.health = 1000

    def draw(self,surface):
        if self.health < 0:
            self.image = self.undam
        if self.health < -400:
            self.image = self.light_dam
        if self.health < -700:
            self.image = self.heavy_dam
        if self.health < -1000:
            self.image = self.destroyed
        surface.blit(self.image, (0,500))
