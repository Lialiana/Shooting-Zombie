import pygame
from pygame.locals import KEYDOWN, QUIT, K_SPACE, K_q, K_e
import random
from man import Man 
from bullets import Bullets 
from zombie import Zombies 
from button import Button 
from texts import Text, Message, BlinkingText, MessageBox

# setup
pygame.init()
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.mixer.init()
clock = pygame.time.Clock()
FPS = 100

#fonts

title_font = "Fonts/Aladin-Regular.ttf"
instructions_font = 'Font/BubblegunSans-Regular.ttf'


woybrain = Message(WIDTH//2 + 50, HEIGHT//2 - 90, 90, "WoyBrain", title_font, (255, 255, 255), win)
left_key = Message(WIDTH//2 + 10, HEIGHT//2 - 90, 20, "Press left arrow key to go left", instructions_font, (255, 255, 255), win)
right_key = Message(WIDTH//2 + 10, HEIGHT//2 - 65, 20, "Press right arrow key to go right", instructions_font, (255, 255, 255), win)
up_key = Message(WIDTH//2 + 10, HEIGHT//2 - 45, 20, "Press up arrow key to jump", instructions_font, (255, 255, 255), win)
space_key = Message(WIDTH//2 + 10, HEIGHT//2 - 25, 20, "Press space key to shoot", instructions_font, (255, 255, 255), win)
g_key = Message(WIDTH//2 + 10, HEIGHT//2 - 5, 20, "Press g key to throw grenade", instructions_font, (255, 255, 255), win)
game_won_msg = Message(WIDTH//2 + 10, HEIGHT//2 - 5, 20, "You have won the game", instructions_font, (255, 255, 255), win)

t = Text(instructions_font, 18)
font_color = (12, 12, 12)
play = t.render('Play', font_color)
about = t.render('About', font_color)
controls = t.render('Controls', font_color)
exit = t.render('Exit', font_color)
main_menu = t.render('Main Menu', font_color)

ButtonBG = pygame.image.load('Assets/ButtonBG.png')
bwidth = ButtonBG.get_width()

play_btn = Button(WIDTH//2 - bwidth//4, HEIGHT//2, ButtonBG, 0.5, play, 10)
about_btn = Button(WIDTH//2 - bwidth//4, HEIGHT//2 + 35, ButtonBG, 0.5, about, 10)
controls_btn = Button(WIDTH//2 - bwidth//4, HEIGHT//2 + 70, ButtonBG, 0.5, controls, 10)
exit_btn = Button(WIDTH//2 - bwidth//4, HEIGHT//2 + 105, ButtonBG, 0.5, exit, 10)
main_menu_btn = Button(WIDTH//2 - bwidth//4, HEIGHT//2 + 130, ButtonBG, 0.5, main_menu, 20)

