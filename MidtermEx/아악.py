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

def position (angle) :
  x = l*sin(angle) + x_center
  y = l*cos(angle) + y_center
  return(x,y)

def render (pos_xy) :
  screen.fill(white)
  pygame.draw.line(screen, black, (x_center, y_center), (pos_xy[0], pos_xy[1]), 2)
  pygame.draw.circle(screen, green, (pos_xy[0], pos_xy[1]), 10)
  pygame.draw.circle(screen, green, (x_center+20, y_center+20), 10)

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

l = 200 
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