import sys
import pygame
from settings import Settings
from castle import Castle
from gamestats import GameStats
from button import Button
from bullet import Bullet
from helo import Helo
from tank import Tank
from round import Round
from health_bar_lable import Lable

class HVM:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Helicopter VS Man")
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.castle = Castle()
        self.helo = Helo(self)
        self.tank = Tank(self)
        self.stats = GameStats(self)
        self.bullets = pygame.sprite.Group()
        self.rounds = pygame.sprite.Group()
        self.round = Round(self)



        #makes the play button
        self.play_button = Button(self, "Press to Play")
        self.health_lable = Lable(self, "Castle Health")
    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.helo.update()
                self.tank.update()
                self._update_bullets()
                self._update_rounds()
            self.update_screen()
    def _update_bullets(self):
        self.bullets.update()
        #get rid of gone bullets
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_rounds(self):
        self.rounds.update()
        # get rid of gone rounds and checks collisons
        #Preston Helped me figure out my collisions
        for round in self.rounds.copy():
            if round.rect.colliderect(0, 500, 204, 182):
                self.castle.get_damage()
                print(f"{self.castle.current_health}")
            if round.rect.right < self.screen_rect.left:
                self.rounds.remove(round)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    def _check_play_button(self, mouse_pos):
        """starts the game when player clicks on start"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keyup_events(self,event):
        #respond to key releases
        if event.key == pygame.K_RIGHT:
            self.helo.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.helo.moving_left = False
        elif event.key == pygame.K_d:
            self.tank.moving_right = False
        elif event.key == pygame.K_a:
            self.tank.moving_left = False
        elif event.key == pygame.K_UP:
            self.helo.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.helo.moving_down = False
    def _check_keydown_events(self,event):
        #respond to key presses
        if event.key == pygame.K_RIGHT:
            self.helo.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.helo.moving_left = True
        elif event.key == pygame.K_UP:
            self.helo.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.helo.moving_down = True
        elif event.key == pygame.K_d:
            self.tank.moving_right = True
        elif event.key == pygame.K_a:
            self.tank.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_s:
            self._fire_round()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_round(self):
        if len(self.rounds) < self.settings.tank_rounds_allowed:
            new_round = Round(self)
            self.rounds.add(new_round)

#creates and updates halth bar based in castle health
    def advanced_health(self):
        transition_width = 0
        transition_color = (255,0,0)
        if self.castle.current_health > self.castle.target_health:
            self.castle.current_health -= self.castle.health_change_speed
            transition_width = int((self.castle.target_health - self.castle.current_health) / self.castle.health_ratio)
            transition_color = (255,255,0)
        health_bar_rect = pygame.Rect(10,45, self.castle.current_health/self.castle.health_ratio,25)
        transition_bar_rect = pygame.Rect(health_bar_rect.right, 45 , transition_width,25)
        pygame.draw.rect(self.screen,(0,255,0), health_bar_rect)
        pygame.draw.rect(self.screen, transition_color, transition_bar_rect)
        pygame.draw.rect(self.screen, (0, 0, 0),(10,45,self.castle.health_bar_length,25),4)

    def update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        background = pygame.image.load("images/backgroundColorGrass.png")
        DEFAULT_IMAGE_SIZE = (1280, 720)
        image = pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
        # redraw the screen during each pass through the loop
        self.screen.blit(image, (0,0))
        self.castle.draw(self.screen)
        self.helo.blitme()
        self.tank.blitme()
        #draws the button is the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.health_lable.draw_button()
        if self.stats.game_active:
            self.health_lable.draw_button()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for round in self.rounds.sprites():
            round.draw_bullet()
        self.advanced_health()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    HM = HVM()
    HM.run_game()