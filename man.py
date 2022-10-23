import math
import pygame




class Man(pygame.sprite.Sprite):
    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 5
        self.rotated_position = position

    def move(self, screensize, direction):
        if direction == 'left':
            self.rect.left = max(self.rect.left-self.speed, 0)
        elif direction == 'right':
            self.rect.left = min(self.rect.left+self.speed, screensize[0])
        elif direction == 'up':
            self.rect.top = max(self.rect.top-self.speed, 0)
        elif direction == 'down':
            self.rect.top = min(self.rect.top+self.speed, screensize[1])

    def draw(self, screen, mouse_pos):
        angle = math.atan2(mouse_pos[1]-(self.rect.top+32), mouse_pos[0]-(self.rect.left+26))
        image_rotate = pygame.transform.rotate(self.image, 360-angle*57.29)
        bunny_pos = (self.rect.left-image_rotate.get_rect().width/2, self.rect.top-image_rotate.get_rect().height/2)
        self.rotated_position = bunny_pos
        screen.blit(image_rotate, bunny_pos)
        
        