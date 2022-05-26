# 1분에 한바퀴 도는 시계
import pygame
import sys
from math import *

width = 600
height = 400
w_center = width * 0.5
h_center = height * 0.5
lenght = 100
angle = 0.0
clock = pygame.time.Clock()
count = 1
screen = pygame.display.set_mode( (width, height) )
white = pygame.Color("white")
black = pygame.Color("black")
screen.fill("white")

pygame.display.update()
while True :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      sys.exit()

  x = lenght * sin(angle) + w_center
  y = lenght * cos(angle) + h_center

  angle += 0.104

  count += 1  

 
  screen.fill("white")
  pygame.draw.line(screen, black, (w_center, h_center), (x,y), 2)
  pygame.draw.circle(screen, black, (x, y), 10)
  pygame.display.update()

  clock.tick(1)
  pygame.display.update()