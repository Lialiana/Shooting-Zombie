import pygame
from pygame.locals import KEYDOWN, QUIT, K_SPACE, K_q, K_e
import random
from man import Man 
from bullets import Bullets 
from zombie import Zombies 
from button import Button 

pygame.init()
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.mixer.init()
clock = pygame.time.Clock()
FPS = 100

gunshot_sound = pygame.mixer.Sound

#images**************
