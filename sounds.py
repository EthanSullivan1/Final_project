import pygame

pygame.mixer.init()
sounds = {
'explosion': pygame.mixer.Sound("Audio/explosion.wav"),
'game': pygame.mixer.Sound('Audio/game_audio.wav'),
'power_up': pygame.mixer.Sound('Audio/power_up.wav'),
'rocket': pygame.mixer.Sound('Audio/rocket.wav')
}
pygame.mixer.Sound.set_volume(sounds['game'], float(.3))
pygame.mixer.Sound.set_volume(sounds['rocket'], float(1))
pygame.mixer.Sound.set_volume(sounds['rocket'], float(1))
pygame.mixer.Sound.set_volume(sounds['rocket'], float(1))
def boo(self):
    sounds['game'].play()
def boom(self):
    sounds['explosion'].play()
def bing(self):
    sounds['power_up'].play()
def zoom(self):
    sounds['rocket'].play()

