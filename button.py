import pygame.font

class Button:
    def __init__(self, HVM_game, msg):
        self.screen = HVM_game.screen
        self.screen_rect = self.screen.get_rect()

        #sets dimensions and properties of button
        self.width, self.height = 220, 50
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #Build the button rect and centers it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = (self.screen_rect.centery) - 150

        #preps the button mesg
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """turns the message into  a rendered image"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draws a blank button then the msg
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
