from turtle import heading, width
import pygame
import sys

# canvas size
width = 600
height = 400

# make a canvas
screen = pygame.display.set_mode( (600,400))
# ((wid,hei))

# fill the canvas with some color
screen.fill("white")

# update the display or show to the computer screen
pygame.display.update()
while True :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      sys.exit()
  screen.fill("white")
  pygame.display.update()