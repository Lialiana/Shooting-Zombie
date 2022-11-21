
import pygame, sys, os, time
import button
from pygame.locals import *
import math
import random


pygame.init()

#create game window
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("testing folder/font.ttf", 40)

#define colours
TEXT_COL = (0, 0, 0)

#load button images
play_img = pygame.image.load("testing folder/images/play_button.png").convert_alpha()
settings_img = pygame.image.load("testing folder/images/setting_button.png").convert_alpha()
about_img = pygame.image.load("testing folder/images/about_button.png").convert_alpha()
quit_img = pygame.image.load("testing folder/images/quit_button.png").convert_alpha()
video_img = pygame.image.load('testing folder/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('testing folder/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('testing folder/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('testing folder/images/button_back.png').convert_alpha()

#create button instances
play_button = button.Button(230, 90, play_img, 1)
settings_button = button.Button(230, 180, settings_img, 1)
about_button = button.Button(230,270, about_img, 1)
quit_button = button.Button(230, 360, quit_img, 1) 
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def game_over():
    game_over_text = font.render(f"GAME OVER", True, (200,200,200))
    screen.blit(game_over_text, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    screen.fill((52,78,91))
    pygame.display.update()
    time.sleep(10)
    pygame.quite()

    for character in badguys:
        character.kill()

    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((255, 255, 255))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if play_button.draw(screen):
        # menu_state = "resume"
        menu_state = "play"
      if settings_button.draw(screen):
        menu_state = "settings" 
      if about_button.draw(screen):
        menu_state = "about" 
      if quit_button.draw(screen):
        run = False

    if menu_state == "play":

      pygame.init()
      pygame.mixer.init() 
      width, height = 640, 480
      screen=pygame.display.set_mode((width, height))
      keys = [False, False, False, False]
      playerpos=[150,100]
      acc=[0,0] 
      arrows=[] 

      gametime = 90000


      badtimer=100
      badtimer1=0
      badguys=[[1100,146]]
      healthvalue=194



      player = pygame.image.load("testing folder/images/player01.png")
      grass = pygame.image.load("testing folder/images/grass.png")
      castle = pygame.image.load("testing folder/images/brain.png")
      arrow = pygame.image.load("testing folder/images/bullet.png")
      badguyimg1 = pygame.image.load("testing folder/images/zom01.png")

      badguyimg=badguyimg1

      healthbar = pygame.image.load("testing folder/images/healthbar.png")
      health = pygame.image.load("testing folder/images/health.png")

      gameover = pygame.image.load("testing folder/images/gameover.png")
      youwin = pygame.image.load("testing folder/images/youwin.png")

      
      player_width = player.get_width()/2

      hit = pygame.mixer.Sound("testing folder/sounds/mixkit-complex-desire-1093.mp3")
      enemy = pygame.mixer.Sound("testing folder/sounds/grenade blast.wav")
      shoot = pygame.mixer.Sound("testing folder/sounds/bullet.wav")
      hit.set_volume(0.05)
      enemy.set_volume(0.05)
      shoot.set_volume(0.05)
      pygame.mixer.music.load('testing folder/sounds/jump.mp3') 
      pygame.mixer.music.play(-1, 0.0)
      pygame.mixer.music.set_volume(0.25)
        

 
      running = 1
      exitcode = 0

      while running:

          badtimer-=1
  
          screen.fill(0)

          for x in range(width//grass.get_width()+1):
              for y in range(height//grass.get_height()+1):
                  screen.blit(grass,(x*100,y*100))

          screen.blit(castle,(0,30))
          screen.blit(castle,(0,120))
          screen.blit(castle,(0,230))
          screen.blit(castle,(0,345 ))

          position = pygame.mouse.get_pos()
          angle = math.atan2(position[1]-(playerpos[1]+12),position[0]-(playerpos[0]+6))
          playerrot = pygame.transform.rotate(player, 360-angle*57.29)
          playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
          screen.blit(playerrot, playerpos1) 


          for bullet in arrows:
              index=0
              velx=math.cos(bullet[0])*10
              vely=math.sin(bullet[0])*10
              bullet[1]+=velx
              bullet[2]+=vely
              if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                  arrows.pop(index)
              index+=1
              for projectile in arrows:
                  arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                  screen.blit(arrow1, (projectile[1], projectile[2]))

          if badtimer==0:
              badguys.append([width, random.randint(50,(height-50))])
              badtimer=100-(badtimer1*2)
              if badtimer1>=35:
                  badtimer1=35
              else:
                  badtimer1+=5
          index=0
          

          for badguy in badguys:
              if badguy[0]<-14:
                  badguys.pop(index)
              badguy[0]-=7

      
              badrect=pygame.Rect(badguyimg.get_rect())
              badrect.top=badguy[1]
              badrect.left=badguy[0]
              if badrect.left<14: 
                  hit.play() 
                  healthvalue -= random.randint(0,50)
                  badguys.pop(index)
              

              index1=0
              for bullet in arrows:
                  bullrect=pygame.Rect(arrow.get_rect())
                  bullrect.left=bullet[1]
                  bullrect.top=bullet[2]
                  if badrect.colliderect(bullrect): 
                      enemy.play()
                      acc[0]+=1
                      badguys.pop(index)
                      arrows.pop(index1)
                  index1+=1
            
    
              index+=1

          for badguy in badguys:
              screen.blit(badguyimg, badguy)

  
          font = pygame.font.Font(None, 24)
 
          survivedtext = font.render(str((gametime-pygame.time.get_ticks())//60000) + ":" + str((gametime-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
          textRect = survivedtext.get_rect()
          textRect.topright=[(width-5),5]
          screen.blit(survivedtext, textRect)


          screen.blit(healthbar, (5,5))
          for health1 in range(healthvalue):
              screen.blit(health, (health1+8,8))


          pygame.display.flip()

          for event in pygame.event.get():
 
              if event.type==pygame.QUIT:
       
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

          # 9 - Move player
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
              print(arrows)
              
          #10 - Win/Lose check
          # win
          if pygame.time.get_ticks()>=gametime:
              game_over()
   
          if healthvalue<=0:
              game_over()
          if acc[1]!=0:
              accuracy=acc[0]*1.0/acc[1]*100
          else:
              accuracy=0
      
      if exitcode==0:
          pygame.font.init()
          font = pygame.font.Font(None, 24)
          text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
          textRect = text.get_rect()
          textRect.centerx = screen.get_rect().centerx
          textRect.centery = screen.get_rect().centery+24
          screen.blit(gameover, (0,0))
          screen.blit(text, textRect)
      else:
          pygame.font.init()
          font = pygame.font.Font(None, 24)
          text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
          textRect = text.get_rect()
          textRect.centerx = screen.get_rect().centerx
          textRect.centery = screen.get_rect().centery+24
          screen.blit(youwin, (0,0))
          screen.blit(text, textRect)
      while 1:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  exit(0)
    pygame.display.flip()




    if menu_state == "options":

      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press space button to pause", font, TEXT_COL, 160, 250)


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()