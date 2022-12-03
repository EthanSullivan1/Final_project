
import pygame
from settings import Settings
import pygame.font

class Start_screen:
    def __init__(self, HVM_game, msg):
        pygame.init()
        self.settings = Settings()
        self.s_screen = HVM_game.screen
        pygame.display.set_caption("Helicopter VS Man")
        self.s_screen_rect = self.s_screen.get_rect()
        self.width, self.height = 110, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.button_color = (0,0,0)

        # Build the lable rect and centers it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        #NATHAN HELPED ME FIGURE OUT HOW THE RECTS WORK
        self.rect.centerx = self.s_screen_rect.centerx
        self.rect.y = (self.s_screen_rect.centery)-50

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turns the message into  a rendered image"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draws a blank button then the msg
        self.s_screen.fill((0,0,0))
        self.s_screen.fill(self.button_color, self.rect)
        self.s_screen.blit(self.msg_image, self.msg_image_rect)