import math
import pygame



class Bullets(pygame.sprite.Sprite):
    def __init__(self, image, position, **kwargs):     
        pygame.sprite.Sprite.__init__(self)
        self.angle = position[0]
        self.image = pygame.transform.rotate(image, 360 - position[0]*57.29)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position[1:]
        self.speed = 10
    
    def update(self, screensize):
        velx = math.cos(self.angle)*self.speed
        vely = math.sin(self.angle)*self.speed
        self.rect.left +=velx
        self.rect.top +=vely
        if self.rect.right < 0 or self.rect.left > screensize[0] or self.rect.top > screensize[1] or self. rect.bottom < 0:
            return True
        return False