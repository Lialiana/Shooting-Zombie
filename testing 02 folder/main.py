import pygame, sys, os, time
from button import Button
from pygame.locals import *
import math
import random

pygame.init()

SCREEN = pygame.display.set_mode((640, 480)) # 1280, 720
pygame.display.set_caption("MAIN MENU")

BG = pygame.image.load("testing 02 folder/assets/zombie_bg3.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("testing 02 folder/assets/DalelandsUncialBold-82zA.ttf", 40)


def main_play():
        width, height = 640, 480
        screen=pygame.display.set_mode((width, height))
        
        keys = [False, False, False, False]
        playerpos=[100,100]
        acc=[0,0] 
        arrows= []
        num_arrows = 500
        timestart = pygame.time.get_ticks()  # added 
        gametime = 60000
        badtimer=100
        badtimer1=0
        badguys=[[640,100]]
        healthvalue=194 # 194  


        player = pygame.image.load("testing 02 folder/assets/soldier_silencer.png")
        bg = pygame.image.load("testing 02 folder/assets/zombie_bg1.png")
        brain = pygame.image.load("testing 02 folder/assets/military_tanks.png")
        arrow = pygame.image.load("testing 02 folder/assets/weapon_silencer.png")
        badguyimg1 = pygame.image.load("testing 02 folder/assets/zoimbie.png")
        badguyimg=badguyimg1
        healthbar = pygame.image.load("testing 02 folder/assets/healthbar.png")
        health = pygame.image.load("testing 02 folder/assets/health.png")

        # gameover = pygame.image.load("testing 02 folder/images/gameover.png")
        # youwin = pygame.image.load("testing 02 folder/images/youwin.png")

        
        player_width = player.get_width()/2

        hit = pygame.mixer.Sound("testing 02 folder/sounds/mixkit-complex-desire-1093.mp3")
        enemy = pygame.mixer.Sound("testing 02 folder/sounds/ghost_shot.mp3")
        shoot = pygame.mixer.Sound("testing 02 folder/sounds/9_mm_gunshot-mike-koenig-123.wav")
        hit.set_volume(0.05) 
        enemy.set_volume(0.05)
        shoot.set_volume(0.05)
        pygame.mixer.music.load('testing 02 folder/sounds/explosion.mp3') 
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.25)
            

        running = 1
        # exitcode = 0

        while running:

            badtimer-=1
    
            screen.fill(0)

            for x in range(width//bg.get_width()+1):
                for y in range(height//bg.get_height()+1):
                    screen.blit(bg,(x*100,y*100))

            screen.blit(brain,(0,10))
            screen.blit(brain,(0,120))
            screen.blit(brain,(0,230))
            screen.blit(brain,(0,345))

            position = pygame.mouse.get_pos()
            angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26)) 
            playerrot = pygame.transform.rotate(player, 360-angle*57.29)
            playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
            screen.blit(playerrot, playerpos1) 


            for bullet in list(arrows):   # added list
                # index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                    arrows.remove(bullet)
                    # arrows.pop(index)
                # index+=1
                if num_arrows <= 0:  # added if num 
                    running=0
                for projectile in arrows:
                    arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                    screen.blit(arrow1, (projectile[1], projectile[2]))

            if badtimer==0:
                badguys.append([width, random.randint(50,(height-50))])
                badtimer=200-(badtimer1*2)  #100 
                if badtimer1>=40:  # 35
                    badtimer1=40
                else:
                    badtimer1+=2  # 5 
            index=0
            

            for badguy in badguys:
                if badguy[0]<-64:    
                    badguys.pop(index)
                badguy[0]-=7

        
                badrect=pygame.Rect(badguyimg.get_rect())
                badrect.top=badguy[1]
                badrect.left=badguy[0]
                if badrect.left<64: 
                    hit.play() 
                    healthvalue -= random.randint(5,20)
                    # badguys.pop(index)
                    badguys.pop(index)


                index1=0
                for bullet in arrows:
                    bullrect=pygame.Rect(arrow.get_rect())
                    bullrect.left=bullet[1]
                    bullrect.top=bullet[2]
                    if badrect.colliderect(bullrect): 
                        enemy.play()
                        acc[0]+=1
            
                        arrows.pop(index)
                    index1+=1

            for badguy in badguys:
                screen.blit(badguyimg, badguy)

    
            font = pygame.font.Font(None, 24)
            time_remaining = 90000 - (pygame.time.get_ticks()-timestart)  # added
            survivedtext = font.render(str((gametime-pygame.time.get_ticks())//60000) + ":" + str((gametime-pygame.time.get_ticks())//1000%60).zfill(2), True, (255,255,255))
            textRect = survivedtext.get_rect()
            
            textRect.topright= [635, 5] # [(width-5),5]
            screen.blit(survivedtext, textRect)
            arrowstext = font.render("Remaining arrows: " + str(num_arrows), True, (255, 255, 255)) # added
            arrowsTextRect = arrowstext.get_rect() # added
            arrowsTextRect.topright = [635, 20]
            screen.blit(arrowstext, arrowsTextRect)

                # 5,5
            screen.blit(healthbar, (5,5))
            for health1 in range(healthvalue):
                screen.blit(health, (health1+8,8))


            pygame.display.flip()

            for event in pygame.event.get():
    
                if event.type==pygame.QUIT:
                    # add new
                    # running = False
                    pygame.quit() 
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key==K_w:
                        keys[0]=True
                    elif event.key==K_a:
                        keys[1]=True
                    elif event.key==K_s:
                        keys[2]=True
                    elif event.key==K_d:
                        keys[3]=True
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_w:
                        keys[0]=False
                    elif event.key==pygame.K_a:
                        keys[1]=False
                    elif event.key==pygame.K_s:
                        keys[2]=False
                    elif event.key==pygame.K_d:
                        keys[3]=False

            # Move player
            if keys[0]:
                playerpos[1]-=5
                
            elif keys[2]:
                playerpos[1]+=5
        
            if keys[1]:
                playerpos[0]-=5
        
            elif keys[3]:
                playerpos[0]+=5

            if event.type==pygame.MOUSEBUTTONDOWN:
                shoot.play()
                position=pygame.mouse.get_pos()
                acc[1]+=1
                arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
                num_arrows -= 1


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        if play:
            main_play()
        # PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        # PLAY_TEXT = get_font(20).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 140))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(320, 300),  # 640, 260
                            text_input="BACK", font=get_font(20), 
                            base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

game_over = False
def game_over():
   while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True

    if not game_over:
        rect_x += rect_change_x
        rect += rect_change_y
        if rect_y > 450




   
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(5).render("Welcome To WoyBrain Game.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 140)) # 640, 260
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(320, 300),  
                            text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 50)) # 640, 100

        PLAY_BUTTON = Button(image=pygame.image.load("testing 02 folder/assets/Play Rect.png"), pos=(320, 150),  # 640, 250
                            text_input="PLAY", font=get_font(20), base_color="White", hovering_color="Red")
        ABOUT_BUTTON = Button(image=pygame.image.load("testing 02 folder/assets/About Rect.png"), pos=(320, 275), # 640, 400
                            text_input="ABOUT", font=get_font(20), base_color="White", hovering_color="Red")
        QUIT_BUTTON = Button(image=pygame.image.load("testing 02 folder/assets/Quit Rect.png"), pos=(320, 400),  # 640, 550
                            text_input="QUIT", font=get_font(20), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, ABOUT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()