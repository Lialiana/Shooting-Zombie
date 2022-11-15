


# Importing important libraries

import pygame, sys


# Setting up an environment to initialize pygame

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Watch out your brain')
screen = pygame.display.set_mode((1100, 700),0,32)
 
#setting font settings
font = pygame.font.SysFont('Bolder', 30)
 

# A function that can be used to write text on our screen and buttons

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((50,0,100))
        draw_text('Main Menu', font, (255,255,255), screen, 500, 100)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(450, 150, 200, 50)
        button_2 = pygame.Rect(450, 250, 200, 50)
        button_3 = pygame.Rect(450, 350, 200, 50)


        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                help()
        pygame.draw.rect(screen, (200, 0, 200), button_1)
        pygame.draw.rect(screen, (200, 0, 200), button_2)
        pygame.draw.rect(screen, (200, 0, 200), button_3)

        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), screen, 520, 165)
        draw_text('OPTIONS', font, (255,255,255), screen, 510, 265)
        draw_text('HELP', font, (255,255,255), screen, 520, 365)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 

# This function is called when the "PLAY" button is clicked.

def game():
    running = True
    while running:
        # screen.fill((0,0,0))
       
        # draw_text('GAME SCREEN', font, (255, 255, 255), screen, 500, 120)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            pygame.display.update()
            mainClock.tick(60)
    

        


# This function is called when the "OPTIONS" button is clicked.

def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('OPTIONS SCREEN', font, (255, 255, 255), screen, 500, 140)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)


def help():
    running = True
    while running:
        screen.fill((255,0,0))
 
        draw_text('HELP SCREEN', font, (0, 0, 0), screen, 500, 160)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()