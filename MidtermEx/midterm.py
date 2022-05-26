from fileinput import filename
from itertools import count
from tkinter import Y
from turtle import Screen
import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv
from pygame import mixer
import matplotlib.pyplot as plt
pygame.init()

def position (angle1,angle2) :
  x1 = l1*sin(angle1) + x_center
  y1 = l1*cos(angle1) + y_center

  x2 = x1 + l2*sin(angle2)
  y2 = y1 + l2*cos(angle2)
  return(x1,y1), (x2,y2)

def position1 (an1) :
  x1 = l1*sin(0.0) + x_center
  y1 = l1*cos(0.0) + y_center

  x2 = x1 + l2*sin(an1)
  y2 = y1 + l2*cos(an1)
  return(x1,y1), (x2,y2)

def render (pos_xy1, pos_xy2) :
  screen.fill(white)
  pygame.draw.line(screen, black, (x_center, y_center), (pos_xy1[0], pos_xy1[1]), 2)
  pygame.draw.circle(screen, green, (pos_xy1[0], pos_xy1[1]), 10)
  pygame.draw.line(screen, black, (pos_xy1[0], pos_xy1[1]), (pos_xy2[0], pos_xy2[1]), 2)
  pygame.draw.circle(screen, green, (pos_xy2[0], pos_xy2[1]), 10)

def render1 (pos1, pos2) :
  screen.fill(white)
  pygame.draw.line(screen, black, (x_center, y_center), (pos1[0], pos1[1]), 2)
  pygame.draw.circle(screen, green, (pos1[0], pos1[1]), 10)
  pygame.draw.line(screen, black, (pos1[0], pos1[1]), (pos2[0], pos2[1]), 2)
  pygame.draw.circle(screen, green, (pos2[0], pos2[1]), 10)

def G (t,y) :
  F[0] = -g*sin(y[1]) - 1*cos(2*pi*0.45*t) #extra force
  F[1] = y[0]
  return inv_L.dot(F)

def G_1 (t,y) :
  F[0] = 0
  F[1] = y[0]
  return inv_L.dot(F)

def G1 (t,y1) :
  F[0] = -g*sin(y1[1])+1.0*sin(y1[1]) #damping
  F[1] = y1[0]
  return inv_L.dot(F)

def RK4 (t, y, delta_t):
  k1 = G(t,y)
  k2 = G(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G(t + 0.5*delta_t, y + 0.5*delta_t * k3)
  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

def RK4_2 (t, y, delta_t):
  k1 = G_1(t,y)
  k2 = G_1(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G_1(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G_1(t + 0.5*delta_t, y + 0.5*delta_t * k3)
  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

def RK4_1 (t, y, delta_t):
  k1 = G1(t,y)
  k2 = G1(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G1(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G1(t + 0.5*delta_t, y + 0.5*delta_t * k3)
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

l1 = 100
l2 = 100
a = 0.0 

x_center = width * 0.5
y_center = height * 0.5

m1 = 0.5
g = 9.8 
ll = 1.0 
t = 0.0
delta_t = 0.01
y = np.array([0.0, 0.0]) 
y1 = np.array([0.0, 1.0])
L = np.array([ [ll, 0.0],
              [0.0, 1.0]]) 

F = np.array([0.0, 0.0])
inv_L = inv(L) 

count = 0 

# F 그래프
# time = np.arange(0, 60, delta_t)
# FF = []
# YY = []
# ZZ = []
# for t in time :
#   y = y + delta_t * RK4(t, y, delta_t)
#   FF.append(F[0])
#   YY.append(y[1])
# plt.grid(True)
# plt.plot(time, FF, 'r', time, YY, 'b')
# plt.show()

while True :
  count +=1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
   
  xy1, xy2 = position(y[1],y[1])

   
  render(xy1, xy2)

  t += delta_t
  y = y + delta_t * RK4(t, y, delta_t)

  if t>20 :
      xy1, xy2 = position(y[1],y[1])
      render(xy1, xy2)
      t += delta_t
      y = y + delta_t * RK4_2(t, y, delta_t)

  if t>45 :
      xy3, xy4 = position1(y1[1])
      render1(xy3, xy4)
      t += delta_t
      y1 = y1 + delta_t * RK4_1(t, y1, delta_t)


  clock.tick(100)
  pygame.display.update()