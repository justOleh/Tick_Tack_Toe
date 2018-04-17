import pygame
from settings import *

class Dagger(pygame.sprite.Sprite):
    def __init__(self):
        super(Dagger,self).__init__()

        self.image = pygame.image.load(CIRCLE_PATH)

        self.rect = self.image.get_rect()



    def uppdate(self):
        pass

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load(BACKGROUND_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2