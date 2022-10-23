import math
import pygame

class Zombies(pygame.sprite.Sprite):
    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position
        self.speed = 7
        
    def update(self):
        self.rect.left -=self.speed
        if self.rect.left < 64:
            return True
        return False
        