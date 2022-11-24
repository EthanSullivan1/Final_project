import sys
import pygame
from settings import Settings
from castle import Castle
import time
#from helo import Helo

class HVM():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Helicopter VS Man")
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.castle = Castle()
        #self.helo = Helo(self)
    def run_game(self):
        while True:
            self.check_events()
            #self.helo.update()
            self.update_screen()
            pygame.display.flip()
            time.sleep(5)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #     self._check_keyup_events(event)
            sys.exit()
    # def _check_keyup_events(self,event):
    #     #respond to key releases
    #     if event.key == pygame.K_RIGHT:
    #         self.helo.moving_right = False
    #     elif event.key == pygame.K_LEFT:
    #         self.helo.moving_left = False
    #     elif event.key == pygame.K_UP:
    #         self.helo.moving_up = False
    #     elif event.key == pygame.K_DOWN:
    #         self.helo.moving_down = False
    def _check_keydown_events(self,event):
        #respond to key presses
        # if event.key == pygame.K_RIGHT:
        #     self.helo.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.helo.moving_left = True
        # elif event.key == pygame.K_UP:
        #     self.helo.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #     self.helo.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        background = pygame.image.load("images/backgroundColorGrass.png")
        DEFAULT_IMAGE_SIZE = (1280, 720)
        image = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
        self.screen.blit(image, (0,0))
        self.castle.draw(self.screen)
        #self.helo.blitme()
        # redraw the screen during each pass through the loop
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    HM = HVM()
    HM.run_game()