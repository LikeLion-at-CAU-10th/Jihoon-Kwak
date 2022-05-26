from fileinput import filename
from itertools import count
from turtle import Screen
import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv
from pygame import mixer
import matplotlib.pyplot as plt
pygame.init()

def point (angle1, angle2) :
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
  F[0] = -m2 * l2 * y[1] * y[1] * sin(y[2]-y[3]) - (m1+m2)*g*sin(y[2])
  F[1] = l1 * y[0] * y[0] * sin(y[2]- y[3]) - g * sin(y[3])
  F[2] = y[0]
  F[3] = y[1]

  L = np.array([
    [(m1+m2)*l1, m2*cos(y[2]-y[3]), 0, 0],
    [l1 * cos(y[2]-y[3]), l2, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
  ])
  inv_L = inv(L)
  return inv_L.dot(F)

def RK4 (t, y, delta_t):
  k1 = G(t,y)
  k2 = G(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G(t + 0.5*delta_t, y + 0.5*delta_t * k3)
  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

width = 1000
height = 800

screen = pygame.display.set_mode( (width, height) )

white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')

screen.fill(white)

pygame.display.update()

clock = pygame.time.Clock()

m1 = 2.0
m2 = 0.0
l1 = 1.0
l2 = 1.5
g = 9.8

l_pixel = 100

x_center = width * 0.5
y_center = height * 0.5

t = 0.0
delta_t = 0.01
y = np.array([0.0, 0.0, 1.0, 0.0]) 
F = np.array([0.0, 0.0, 0.0, 0.0])



count = 0 

FF=[]
time = np.arange(0, 200, delta_t)

# for t in time :
#   FF.append(F[3])

plt.grid(True)
plt.plot(time, FF, 'r')
plt.show()

while True :
  count +=1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
   
  xy1, xy2 = point(y[2], y[3])

   
  render(xy1, xy2)

  t += delta_t
  y = y + delta_t * RK4(t, y, delta_t)

  clock.tick(100)
  pygame.display.update()