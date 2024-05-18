import pygame
from Background import Background

class Bird(pygame.sprite.Sprite):
    scale = 2

    loadBird = pygame.image.load("Bird.png")
    birdSize = pygame.transform.scale_by(loadBird, (scale, scale))

    width = loadBird.get_height() * scale
    height = loadBird.get_height() * scale
    xpos = 100
    ypos = Background.height/2 - width
    score = 0

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, userInput):
        
        # Gravity
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.vel == 0:
            self.flap = False
        if self.rect.y < Background.height - self.width:
            self.rect.y += int(self.vel)

        # Detect click
        if pygame.mouse.get_pressed()[0] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
        if self.alive == False:
            self.vel = 7