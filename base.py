
import pygame
import math
import random

pizza_position = [960, 540]

pygame.init()
score = 0
health = 3



#define screen sixe
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Equihacks S1 Submission")


#define colours
pygame.mouse.set_visible(False)
BG = (255, 255, 255)
BLACK = (0, 0, 0)

pizza_original = pygame.image.load('img/pizzacursor.png')
cursor_img = pygame.image.load('img/peppermint-removebg-preview.png')


asteroid_l1 = pygame.image.load('img/lemon-removebg-preview.png')
asteroid_l2 = pygame.image.load('img/redlemon-removebg-preview.png')
asteroid_list = []



run = True

speed = 4
asteroid_speed = 3
pizza_speed = 0

DEFAULT_IMAGE_SIZE = (80, 80)
DEFAULT_Cookie_SIZE = (15, 15)
DEAFULT_CURSOR_SIZE = (32, 32)
# Scale the image to your needed sixe
pizza_original = pygame.transform.scale(pizza_original, DEFAULT_IMAGE_SIZE)
cursor_img = pygame.transform.scale(cursor_img, DEAFULT_CURSOR_SIZE)

x = [10, 1910]
y = [10, 1070]


bullet = pygame.image.load('img/cookie-removebg-preview.png').convert_alpha()
bullet = pygame.transform.scale(bullet, DEFAULT_Cookie_SIZE)
bullet_list = []

#game loop

angle = 0

def asteroid_bullet_collision(score):
  for idb, bullet in enumerate(bullet_list): 
    for ida, asteroid in enumerate(asteroid_list):
      if bullet[1].colliderect(asteroid[1]) and asteroid[3] == asteroid_l1:
        score += 10

        bullet_list.pop(idb)
        asteroid_list.pop(ida)
        asteroid_create(30, 59, asteroid_l2) 
        asteroid_create(30, 59, asteroid_l2) 
      if bullet[1].colliderect(asteroid[1]) and asteroid[3] == asteroid_l2:
        score += 50
        bullet_list.pop(idb)
        asteroid_list.pop(ida)
  return score




def asteroid_create(low_size, high_size, costume_type):
  if random.random() < 0.05:
    location_x_asteroid=random.choice(x)
    location_y_asteroid=random.randrange(y[0], y[1])
    size_asteroid = random.randrange(low_size, high_size)
    DEAFULT_ASTEROID_SIZE = (size_asteroid, size_asteroid)
    x_dist = location_x_asteroid - pizza_position[0]
    y_dist = location_y_asteroid - pizza_position[1]
    asteroid_angle = math.degrees(math.atan2(y_dist, x_dist))
    asteroid = pygame.transform.scale(costume_type, DEAFULT_ASTEROID_SIZE)
    asteroid_rect = asteroid.get_rect(center = (random.choice(x), random.randrange(y[0], y[1])))  
    asteroid_list.append([asteroid, asteroid_rect, asteroid_angle + 180, costume_type])

def asteroid_render():
  for asteroid in asteroid_list:
    screen.blit(asteroid[0], asteroid[1])

def asteroid_move():
  for asteroid in asteroid_list:
    asteroid[1] = asteroid[1].move(asteroid_speed * math.cos(asteroid[2]) , -1* speed * math.sin(asteroid[2]))
 

def bullet_create(angle):
  bullet_rect = bullet.get_rect(center = (pizza_position[0],pizza_position[1]))
  bullet_list.append([bullet, bullet_rect, angle])

  """Assign a position and an image to the bullet"""
  """Add to a list of bullets"""

def bullet_render():
  for bullet in bullet_list:
    screen.blit(bullet[0], bullet[1])
  """Go through the list of bullets and render each bullet"""

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
  screen.blit(cursor_img, pos)

  
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

  asteroid_create(60, 100, asteroid_l1)
  asteroid_render()
  asteroid_move()
  
  score = asteroid_bullet_collision(score)
  
  #update display
  pygame.display.flip()

  #event handlerbullet
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

  print(score)

  

    

  

pygame.quit()