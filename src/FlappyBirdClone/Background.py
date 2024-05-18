class Background:
  import pygame

  width = 500
  height = 500
  xpos = width/2
  ypos = height/2

  # Set the surface

  screen = pygame.display.set_mode((width, height))

  # Initial load

  loadStart = pygame.image.load("SKStartScreen.png")
  loadStarted = pygame.image.load("SKScreenStarted.png")

  # Resize the initial load

  screenSize = pygame.transform.scale(loadStart, (width, height))
  startedSize = pygame.transform.scale(loadStarted, (width, height))