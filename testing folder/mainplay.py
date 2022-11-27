
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

# define colours
TEXT_COL = (0, 0, 0)

# load button images
play_img = pygame.image.load("testing folder/images/play_button.png").convert_alpha()
settings_img = pygame.image.load("testing folder/images/settings_button.png").convert_alpha()
about_img = pygame.image.load("testing folder/images/about_button.png").convert_alpha()
quit_img = pygame.image.load("testing folder/images/quit_button.png").convert_alpha()
# video_img = pygame.image.load('testing folder/images/button_video.png').convert_alpha()
# audio_img = pygame.image.load('testing folder/images/button_audio.png').convert_alpha()
# keys_img = pygame.image.load('testing folder/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('testing folder/images/back_button.png').convert_alpha()

#create button instances
play_button = button.Button(230, 90, play_img, 1)
settings_button = button.Button(230, 180, settings_img, 1)
about_button = button.Button(230,270, about_img, 1)
quit_button = button.Button(230, 360, quit_img, 1) 
# video_button = button.Button(230, 75, video_img, 1)
# audio_button = button.Button(230, 150, audio_img, 1)
# keys_button = button.Button(230, 225, keys_img, 1)
back_button = button.Button(230, 300, back_img, 1)

def game_over():
    
    '''game_over_text = font.render(f"GAME OVER", True, TEXT_COL)
    screen.blit(game_over_text, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    screen.fill((50,70,90))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()'

    for character in badguys:
        character.kill()'''

    
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
      # pygame.mixer.init() 
      width, height = 640, 480
      screen=pygame.display.set_mode((width, height))
      keys = [False, False, False, False]
      playerpos=[100,100]
      acc=[0,0] 
      arrows= []
      num_arrows = 1000
      timestart = pygame.time.get_ticks()  # added 
      gametime = 60000
      badtimer=100
      badtimer1=0
      badguys=[[640,100]]
      healthvalue=194    


      player = pygame.image.load("testing folder/images/soldier_silencer.png")
      bg = pygame.image.load("testing folder/images/zombie_bg1.png")
      brain = pygame.image.load("testing folder/images/military_tanks.png")
      arrow = pygame.image.load("testing folder/images/weapon_silencer.png")
      badguyimg1 = pygame.image.load("testing folder/images/zoimbie.png")
      badguyimg=badguyimg1

      healthbar = pygame.image.load("testing folder/images/healthbar.png")
      health = pygame.image.load("testing folder/images/health.png")

      gameover = pygame.image.load("testing folder/images/gameover.png")
      youwin = pygame.image.load("testing folder/images/youwin.png")

      
      player_width = player.get_width()/2

      hit = pygame.mixer.Sound("testing folder/sounds/mixkit-complex-desire-1093.mp3")
      enemy = pygame.mixer.Sound("testing folder/sounds/grenade blast.wav")
      shoot = pygame.mixer.Sound("testing folder/sounds/bullet.wav")
      hit.set_volume(0.1) # 0.05
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

          for x in range(width//bg.get_width()+1):
              for y in range(height//bg.get_height()+1):
                  screen.blit(bg,(x*100,y*100))

          screen.blit(brain,(0,30))
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
              # badguys.append([width, random.randint(50,(height-50))])
              badguys.append([640, random.randint(50, 430)])
              #100
              badtimer=300-(badtimer1*0.5)
              if badtimer1>=35:
                  badtimer1=35
              else:
                  badtimer1+=5
          index=0
          

          for badguy in list(badguys):
              if badguy[0]<-64: 
                badguys.remove(badguy)   
                  # badguys.pop(index)
              badguy[0]-=7

      
              badrect=pygame.Rect(badguyimg.get_rect())
              badrect.top=badguy[1]
              badrect.left=badguy[0]
              if badrect.left<64: 
                  hit.play() 
                  healthvalue -= random.randint(5,20)
                  # badguys.pop(index)
                  badguys.remove(badguy)
              

              index1=0
              for bullet in list(arrows):
                  bullrect=pygame.Rect(arrow.get_rect())
                  bullrect.left=bullet[1]
                  bullrect.top=bullet[2]
                  if badrect.colliderect(bullrect): 
                      enemy.play()
                      acc[0]+=1
                      # index
                      # badguys.pop(0) if badguys else False
                      # False 
                      badguys.remove(badguy)
                      arrows.remove(bullet)
                      arrows.pop(index1)
                  index1+=1
            
    
              index+=1

          for badguy in badguys:
              screen.blit(badguyimg, badguy)

  
          font = pygame.font.Font(None, 24)
          time_remaining = 90000 - (pygame.time.get_ticks()-timestart)  # added
 # 60000
          survivedtext = font.render(str((gametime-pygame.time.get_ticks())//60000) + ":" + str((gametime-pygame.time.get_ticks())//1000%60).zfill(2), True, (255,255,255))
          # survivedtext = font.render(str((time_remaining/60000))+":"+str(time_remaining/1000%60).zfill(2), True, (255,255,255))
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
              # print(arrows)
              
          # Win/Lose check
          # win
          if pygame.time.get_ticks()>=gametime:
              game_over()
   
          if healthvalue<=0:
              game_over()
          if acc[1]!=0:
              accuracy=acc[0]*1.0/acc[1]*100
          else:
              accuracy=0
              # added
              pygame.font.init()
              font = pygame.font.SysFont("testing folder/font.ttf", 24)
              elapsedtime = pygame.time.get_ticks()-timestart/1000 
              game_over_message = " "
              if num_arrows <= 0:
                game_over_message = "You have run out of arrows!!!"
                game_over_message += "Score: "+str(accuracy)+ "%(Accuracy) * "+str(elapsedtime/1000)+ "(Time) =  " +str(int(accuracy*elapsedtime/1000))
                text = font.render(game_over_message, True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.centery = screen.get_rect().centerx
                textRect.centery = screen.get_rect().centery+24
                if exitcode == 0:
                  screen.blit(game_over, (0,0))
                else:
                  screen.blit(youwin, (0, 0))
                  screen.blit(text, textRect)
                  pygame.display.flip()
                  pygame.mixer.music.fadeout(1500)
                  pygame.time.delay(1500)
                global textx, texty, textx_size, texty_size
                global text2x, text2y, text2x_size, text2y_size
                bigfont = pygame.font.SysFont("testing folder/font.ttf", 80)
                text = bigfont.render('Play again', 13, (0, 255, 0))
                textx = width/2 - text.get_width()/2
                texty = width/4 - text.get_height()/2
                textx_size = text.get_width()
                texty_size = text.get_height()
                pygame.draw.rect(screen, (255, 255, 255), ((textx-5, texty-5), (textx_size+10, texty_size+110)))
                screen.blit(text,(width/2-text.get_width()/2, height()/4 -text.get_height()/2))
                text2 = bigfont.render('Exit', 13, (255,0,0))
                text2x = width/2-text2.get_width()/2
                text2y = height*3/4-text2.get_height()/2
                text2x_size = text2.get_width()
                text2y_size = text2.get_height()
                pygame.draw.rect(screen, (255, 255, 255), ((text2x-5, text2y-5), (text2x_size+10, text2y_size+10)))
                screen.blit(text2, (width/2-text2.get_width()/2, height*3/4-text2.get_height()/2))
                pygame.display.flip()
             

              '''while 1:
                for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                  elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x >= textx -5 and x <=textx + textx_size+5:
                      if y >= texty - 5 and y <= texty + texty_size+5:
                        break
                    if x >= text2x -5 and x <= text2x + text2x_size + 5:
                      if y >= text2y - 5 and y <= text2y + text2y_size + 5:
                        pygame.quit()
                        exit(0) ''' 





      
   #  if exitcode==0:
          # pygame.font.init()
          # font = pygame.font.Font(None, 24)
          # text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
          #textRect = text.get_rect()
          #textRect.centerx = screen.get_rect().centerx
          # textRect.centery = screen.get_rect().centery+24
          # screen.blit(gameover, (0,0))
           #screen.blit(text, textRect)
      # else:
          # pygame.font.init()
          # font = pygame.font.Font(None, 24)
          # text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
          # textRect = text.get_rect()
          #  textRect.centerx = screen.get_rect().centerx
          # textRect.centery = screen.get_rect().centery+24
          # screen.blit(youwin, (0,0))
          # screen.blit(text, textRect)
      # while 1:
         #  for event in pygame.event.get():
             #  if event.type == pygame.QUIT:
                  # running = False
                 #  pygame.quit()
                # add sys 
                  # sys.exit(0) 
    # pygame.display.flip() # 
    


    if menu_state == "about":
      if back_button.draw(screen):
        menu_state = "main"

    if menu_state == "settings":
      #if video_button.draw(screen):
        #print("Video Settings")
      #if audio_button.draw(screen):
        #print("Audio Settings")
      #if keys_button.draw(screen):
        #print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main" 
  else:
    draw_text("Press space button to pause", font, TEXT_COL, 140, 250)


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()