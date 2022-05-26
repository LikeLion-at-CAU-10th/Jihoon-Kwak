from fileinput import filename
from webbrowser import BackgroundBrowser
import pygame
import sys
from math import *

def point (angle) :
  x = lenght * sin(angle) + w_center
  y = lenght * cos(angle) + h_center
  return (x,y) # return as a pair of numbers or tuple

def render (xy) :
  screen.fill("white")
  # somthing interesting here
  pygame.draw.line(screen, black, (w_center, h_center), (xy[0],xy[1]), 2)
  pygame.draw.circle(screen, black, (xy[0], xy[1]), 10)
  pygame.display.update()


# pygame.init()

# background = pygame.mixer.sound("bensound-creativeminds.mp3")
# background.play(-1)

# canvas size
width = 600
height = 400

# center position
w_center = width * 0.5
h_center = height * 0.5

# lenght of the line
lenght = 100

# angle
angle = 0.0 #initial angle

# clock for screen
clock = pygame.time.Clock()

# counter
count = 1

# make a canvas
screen = pygame.display.set_mode( (width, height) )
# ((wid,hei))

# predefined colors
white = pygame.Color("white")
black = pygame.Color("black")

# fill the canvas with some color
screen.fill("white")

# update the display or show to the computer screen
pygame.display.update()
while True :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      sys.exit()

  # update the position of the circle
  xy = point(angle)

  angle += 0.01 # add 1 radian every screen

  count += 1 # update the count 

  # randering
  render(xy)

  clock.tick(100) #runs 1 screen per second
  pygame.display.update()

  # filename = "images/pendulum_%04.png" % (count)
  # pygame.image.save( screen, filename)