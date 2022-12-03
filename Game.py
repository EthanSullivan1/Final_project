#imports all classes used so minimize size of main game file
import sys
import pygame
import time
import random
from settings import Settings
from castle import Castle
from gamestats import GameStats
from button import Button
from bullet import Bullet
from helo import Helo
from tank import Tank
from round import Round
from health_bar_lable import Lable
from tank_lives_lable import TLable
from powerup import Health_power
from s_screen import Start_screen
from i_screen import I_screen
from C_buton import C_button
from C_screen import C_screen
import sounds

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
        self.power_up = Health_power(self)
        self.power_ups = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.t = 0
        self.C_screen = C_screen()
        self.INS = I_screen()
        self.sounds = sounds




        #makes the play button
        self.play_button = Button(self, "Press to Play")
        self.health_lable = Lable(self, "Castle Health")
        self.tank_lable = TLable(self, "Tank Lives")
        self.instructions = Start_screen(self, "Instructions")
        self.control_button = C_button(self, "Game Controls")

    #main game loop
    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.Clock()
                self.helo.update()
                self.tank.update()
                self._update_bullets()
                self._update_rounds()
                self._check_helo_PU_collissions()
            self.update_screen()

    def Clock(self):
        self.clicks = pygame.time.get_ticks()
        self.clicks =  pygame.time.get_ticks()

    #updates bullet position (allows it to move across screen)
    def _update_bullets(self):
        self.bullets.update()
        #get rid of gone bullets
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
            if bullet.rect.colliderect(self.tank.rect.x, self.tank.rect.y, 82, 60):
                self.tank.tank_health -= 10
                self.bullets.remove(bullet)
                self.sounds.boom(self)
                print(f"{self.tank.tank_health}")

    # updates round position (allows it to move across screen)
    def _update_rounds(self):
        self.rounds.update()
        # get rid of gone rounds and checks collisons
        #Preston Helped me figure out my collisions
        for round in self.rounds.copy():
            if round.rect.colliderect(0, 500, 204, 182):
                self.castle.get_damage()
                self.sounds.boom(self)
                print(f"{self.castle.current_health}")
            if round.rect.right < self.screen_rect.left:
                self.rounds.remove(round)

    #checks all keydown/up/mouse events
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
                self._check_instruction_button(mouse_pos)
                self._check_control_button(mouse_pos)

    #checks to see if play button is clicked
    def _check_play_button(self, mouse_pos):
        """starts the game when player clicks on start"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
            self.sounds.boo(self)

    #sees if keys are released
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

    #sees if keys/ mouse is pressed
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

    #shoots a bullet
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sounds.zoom(self)

    #shoots a round
    def _fire_round(self):
        if len(self.rounds) < self.settings.tank_rounds_allowed:
            new_round = Round(self)
            self.rounds.add(new_round)
            self.sounds.zoom(self)

    #creates and updates health bar based in castle health
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

    #creates a power up at random x location along the x-axis
    def make_power_up(self):
        power_up = Health_power(self)
        self.power_up.rect.x = random.randint(0, 1000)
        self.power_up.rect.y = 0
        self.power_ups.add(power_up)

    #sees if the Helo hits the power up
    def _check_helo_PU_collissions(self):
        PU_collisions = pygame.sprite.spritecollideany(self.helo, self.power_ups)
        if PU_collisions:
            self.castle.get_health()
            self.power_ups.empty()
            self.sounds.bing(self)
            print(self.castle.current_health)
        if not self.power_ups:
            if self.clicks >= self.t:
                self.make_power_up()
                self.t += (random.randint(10, 15)*1000) + 11000
        self._check_PU_bottom()

    #gets rid of the power up once it goes off screen
    def _check_PU_bottom(self):
        screen_rect = self.screen.get_rect()
        for power_up in self.power_ups.sprites():
            if power_up.rect.bottom >= screen_rect.bottom:
                self.power_ups.empty()
                print("gone")

    #draws the powerup
    def draw_PU(self):
        self.power_ups.draw(self.screen)

    #sees if instruction button is hit
    def _check_instruction_button(self, mouse_pos):
        """starts the game when player clicks on start"""
        if self.instructions.rect.collidepoint(mouse_pos):
            self.INS.draw()
            time.sleep(5)

    #sees if control button is hit
    def _check_control_button(self, mouse_pos):
        """starts the game when player clicks on start"""
        if self.control_button.rect.collidepoint(mouse_pos):
            self.C_screen.draw()
            time.sleep(5)


    #updaets everything on the screen depednign on game_status and other factors
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
            #Start_screen.
            self.instructions.draw_button()
            self.control_button.draw_button()
            self.play_button.draw_button()
        #draws lables for health and lives left
        elif self.stats.game_active:
            self.screen.blit(image, (0, 0))
            self.castle.draw(self.screen)
            self.helo.blitme()
            self.tank.blitme()
            self.health_lable.draw_button()
            self.tank_lable.draw_button()
            self.advanced_health()
            self.tank.draw_lives()
            self.advanced_health()
            self.tank.draw_lives()
            self.draw_PU()
            self.power_ups.update()
            self.health_lable.draw_button()
            self.tank_lable.draw_button()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for round in self.rounds.sprites():
            round.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    HM = HVM()
    HM.run_game()
