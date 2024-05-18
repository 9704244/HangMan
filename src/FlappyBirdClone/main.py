# Made by Symon Kim with Pygame

import pygame
import random

from FlappyBird import Bird
from Background import Background
from Pipe import Pipe
from sys import exit

pygame.init()

# Initial variables
loadScreen = Background.screenSize
running = True
initial = True
initBird = True
isAlive = True
pipeTimer = 0
birdTimer = 0
clock = pygame.time.Clock()
xBird, yBird = Bird.xpos, Bird.ypos
userInput = pygame.key.get_pressed()
birdPos = (Bird.xpos, Bird.ypos)
font = pygame.font.SysFont('Segoe', 26)

# Make groups
pipes = pygame.sprite.Group()
bird = pygame.sprite.GroupSingle()
# Add bird

bird.add(Bird(xBird, yBird, Bird.birdSize))

# Collisions
while running == True:

    # Collision Detection
    pipeCollision = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
    if pipeCollision:
        bird.sprite.alive = False
    # load background
    Background.screen.blit(loadScreen, (0, 0))

    # Add to pipes
    if pipeTimer <= 0:
        xTop, xBottom = Background.width + Pipe.width, Background.width + Pipe.width
        yTop = random.randrange(-500, -320)
        yBottom = yTop + Pipe.height + 120
        pipes.add(Pipe(xTop, yTop, Pipe.pipeSizeTop, 'top'))
        pipes.add(Pipe(xBottom, yBottom, Pipe.pipeSizeBottom, 'bottom'))
        pipeTimer = 190
    pipeTimer -= 1

    # Update
    if bird.sprite.alive == True and loadScreen == Background.startedSize:
        pipes.update()
    if loadScreen == Background.startedSize:
        bird.update(userInput)
    if initBird == True:
        xBird += 10
        initBird = False
    #Draw
    pipes.draw(Background.screen)
    bird.draw(Background.screen)

    #Score
    scoreText = font.render('score: ' + str(Bird.score), True, (255, 255, 255))
    Background.screen.blit(scoreText, (20, 20))

    # Check to delete pipe
    clock.tick(60)
    pygame.display.update()

        # Enter Game
    if initial == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                loadScreen = Background.startedSize
                initial = False

    # Object Detection

    # Exit Code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
exit()

