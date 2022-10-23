import pygame
from man import Man 
from bullets import Bullets 
from zombie import Zombies 
from button import Button 

pygame.init()
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

clock = pygame.time.Clock()
FPS = 100

#images**************