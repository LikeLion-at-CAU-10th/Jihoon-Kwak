from fileinput import filename
from itertools import count
from turtle import Screen
import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv
from pygame import mixer
from pyparsing import White
pygame.init()

def point (angle1, angle2) :
  x1 = 100*l1 * sin(angle1) + x_center
  y1 = 100*l1 * cos(angle1) + y_center

  x2 = 100*l2 * sin(angle2)
  y2 = 100*l2 * cos(angle2)

  return (x1, y1), (x2, y2)

def render (posxy1, posxy2) :
  screen.fill(White)
  pygame.draw.line(screen, black, (x_center, y_center), (posxy1[0], posxy1[1]), 2)
  pygame.draw.circle(screen, green, (posxy1[0], posxy1[1]), 10)
  pygame.draw.line(screen, black, (posxy1[0], posxy1[1]), (posxy2[0], posxy2[1]), 2)
  pygame.draw.circle(screen, green, (posxy2[0], posxy2[1]), 10)

def G (t,y) :
  F[0] = -m2 * l2 * y[1] * y[1] * sin(y[2] - y[3]) - (m1 + m2)*g*sin(y[2])
  F[1] = l1 * y[0] *y[0] * sin(y[2] - y[3]) -g * sin(y[3])
  