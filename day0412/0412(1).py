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

# bkg = pygame.mixer.Sound("bensound-creativeminds.mp3")
# bkg.play(-1)

#from pprint import pprint

def position (angle) :
  #update : position
  x = l*sin(angle) + x_center
  y = l*cos(angle) + y_center
  return(x,y) #return as a pair

#rendering the object in the screen

def render (pos_xy) :
  screen.fill(white)
  pygame.draw.line(screen, black, (x_center, y_center), (pos_xy[0], pos_xy[1]), 2)
  pygame.draw.circle(screen, green, (pos_xy[0], pos_xy[1]), 10)

#slope(G) function
def G (t,y) :
  F[0] = -g*sin(y[1])
  F[1] = y[0]
  return inv_L.dot(F)

# RK4 method
def RK4 (t, y, delta_t):
  k1 = G(t,y)
  k2 = G(t + 0.5*delta_t, y + 0.5*delta_t * k1)
  k3 = G(t + 0.5*delta_t, y + 0.5*delta_t * k2)
  k4 = G(t + 0.5*delta_t, y + 0.5*delta_t * k3)
  return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

#canvas
width = 600
height = 600

#screen 600x400
screen = pygame.display.set_mode( (width, height) )

#built-in colors
white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')

#color the screen
screen.fill(white)

#update
pygame.display.update()

#for changing the frame counts per second
clock = pygame.time.Clock()

l = 200 #length of the pendulum in pixel
a = 0.0 #amgle of pendulum

x_center = width * 0.5
y_center = height * 0.5

#block from RK4 simple pendulum
########################################
g = 9.8 #gravity
ll = 1.0 #length of pendulum in meters
t = 0.0
delta_t = 0.01
y = np.array([0.0, 1.0]) #velocity, angle
L = np.array([ [ll, 0.0],
              [0.0, 1.0]]) # 2x2matrix
F = np.array([0.0, 0.0])
inv_L = inv(L) #matrix inversion
########################################

count = 0 #frame counter
#infinite loop
while True : #60 frames per second
  count +=1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
   #update
  xy = position(y[1])

   #render
  render(xy)

  #block from RK4 for simple pendulum
  ########################################
  t += delta_t
  y = y + delta_t * RK4(t, y, delta_t)
  ##########################################
  clock.tick(100) #run one hundred frames per second
  pygame.display.update() #every single frame I update

  # filename = "example_pendulum_%0.4d.png" % (count)
  # pygame.image.save( screen, filename) #save as many images