from fileinput import filename
from itertools import count
from turtle import Screen
import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv
from pygame import mixer
pygame.init()

def position (angle1) :
  x1 = 100*l1*sin(angle1) + x_center
  y1 = 100*l1*cos(angle1) + y_center

  x2 = x1 + 100*l2*sin(angle1)
  y2 = y1 + 100*l2*cos(angle1)
  return(x1,y1), (x2,y2)

def render (xy1, xy2) :
  screen.fill(white)
  pygame.draw.line(screen, black, (x_center, y_center), (xy1[0], xy1[1]), 2)
  pygame.draw.circle(screen, green, (xy1[0], xy1[1]), 10)
  pygame.draw.line(screen, black, (xy1[0], xy1[1]), (xy2[0], xy2[1]), 2)
  pygame.draw.circle(screen, green, (xy2[0], xy2[1]), 10)

def G (t,y) :
  F[0] = -g*sin(y[1])
  F[1] = y[0]
  return inv_L.dot(F)

def RK4 (t, y, delta_t):
  k1 = G(t,y)
  k2 = G(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G(t + 0.5*delta_t, y + 0.5*delta_t * k3)
  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

width = 600
height = 600

screen = pygame.display.set_mode( (width, height) )

white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')

screen.fill(white)

pygame.display.update()

clock = pygame.time.Clock()

l1 = 200 
l2 = 100
a = 0.0 

x_center = width * 0.5
y_center = height * 0.5

g = 9.8 
ll = 1.0 
t = 0.0
delta_t = 0.01
y = np.array([0.0, 1.0]) 
L = np.array([ [ll, 0.0],
              [0.0, 1.0]]) 
F = np.array([0.0, 0.0])
inv_L = inv(L) 

count = 0 

while True :
  count +=1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
   
  xy = position(y[1])

   
  render(xy)

  t += delta_t
  y = y + delta_t * RK4(t, y, delta_t)

  clock.tick(100)
  pygame.display.update()