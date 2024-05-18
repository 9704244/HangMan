
import pygame
from Background import Background
from FlappyBird import Bird
import random
class Pipe(pygame.sprite.Sprite):
    scored = False

    width = 162
    height = 600
    xpos = Background.width + width
    ypos = Background.height - height/2

    loadPipeTop = pygame.image.load("SKPipeTop.png")
    loadPipeBottom = pygame.image.load("SKPipeBottom.png")
    
    pipeSizeTop = pygame.transform.scale(loadPipeTop, (width, height))
    pipeSizeBottom = pygame.transform.scale(loadPipeBottom, (width, height))

    hTop = pipeSizeTop.get_height()
    hBot = pipeSizeBottom.get_height()

    # Constructor which sets x, y, and image variables to be assigned
    def __init__(self, x, y, image, pipeType):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, = x,y
        self.pipeType = pipeType
    def update(self):
        self.rect.x -= 2 # speed
        if self.rect.x <= -Background.width:
            self.kill()
        if Bird.xpos + Bird.width/2 > self.rect.topright[0] and self.scored == False and self.pipeType == 'bottom':
            Bird.score += 1
            self.scored = True