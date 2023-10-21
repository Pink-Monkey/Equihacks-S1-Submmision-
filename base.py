
import pygame
import math
import random

pizza_position = [960, 540]

pygame.init()




#define screen sixe
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Equihacks S1 Submission")



#define colours
BG = (255, 255, 255)
BLACK = (0, 0, 0)

pizza_original = pygame.image.load('img/pizzacursor.png')

run = True

speed = 2
pizza_speed = 0

DEFAULT_IMAGE_SIZE = (80, 80)
DEFAULT_Cookie_SIZE = (15, 15)
 
# Scale the image to your needed sixe
pizza_original = pygame.transform.scale(pizza_original, DEFAULT_IMAGE_SIZE)




bullet = pygame.image.load('img/cookie-removebg-preview.png').convert_alpha()
bullet = pygame.transform.scale(bullet, DEFAULT_Cookie_SIZE)
bullet_list = []

#game loop

angle = 0

def bullet_create(angle):
  bullet_rect = bullet.get_rect(center = (pizza_position[0],pizza_position[1]))
  bullet_list.append([bullet, bullet_rect, angle])

  """Assign a position and an image to the bullet"""
  """Add to a list of bullets"""

def bullet_render():
  for bullet in bullet_list:
    screen.blit(bullet[0], bullet[1])
  """Go through the list of bullets and render each bullet"""
  pass

def pizza_move(angle, x_dist, y_dist):
  if math.sqrt(x_dist**2 + y_dist**2) > 10:
    pizza_position[0] -= math.cos(angle) * pizza_speed
    pizza_position[1] += math.sin(angle) * pizza_speed

def bullet_move():
  for bullet in bullet_list:
    bullet[1] = bullet[1].move(speed * math.cos(bullet[2]) , -1* speed * math.sin(bullet[2]))


while run:


  #update background
  screen.fill(BLACK)
  #get mouse position
  pos = pygame.mouse.get_pos()

  x_dist = pos[0] - pizza_position[0]
  y_dist = -(pos[1] - pizza_position[1])#-ve because pygame y coordinates increase down the screen
  angle = math.degrees(math.atan2(y_dist, x_dist))
  bullet_angle = math.atan2(y_dist, x_dist)

  
  #rotate pizza
  pizza = pygame.transform.rotate(pizza_original, angle - 90)
  pizza_rect = pizza.get_rect(center = (pizza_position[0], pizza_position[1]))

  pizza_move(bullet_angle, x_dist, y_dist)
 

  #draw image
  screen.blit(pizza, pizza_rect)

  bullet_move()
  bullet_render()
  
  
  
  #update display
  pygame.display.flip()

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
         bullet_create(bullet_angle)
      if event.key == pygame.K_UP:
        pizza_speed -= 1
      if event.key == pygame.K_DOWN:
        if pizza_speed + 3 < 0:
          pizza_speed += 2

  

    

  

pygame.quit()