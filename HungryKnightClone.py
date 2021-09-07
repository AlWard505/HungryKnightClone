import pygame, sys
from pygame.locals import *

pygame.init()

fps = 30
fpsClock = pygame.time.Clock()

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PyGameIntro')

colours = {#    R   B   G
    "white" : (255,255,255),
    "red"   : (255,  0,  0)
    }

#character varibles
HungryKnight = pygame.image.load("HK.png")
HKX=400
HKY=300
MoveRate = 5
MoveDown = False
MoveUp = False
MoveLeft = False
MoveRight = False

GameOverMode = False



while True: # main game loop
    surface.fill(colours["red"])
    surface.blit(HungryKnight,(HKX,HKY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key in (K_UP,K_w):
                MoveDown = False
                MoveUp = True
            elif event.key in (K_DOWN, K_s):
                MoveUp= False
                MoveDown = True
            elif event.key in (K_LEFT, K_a):
                MoveRight = False
                MoveLeft = True
            elif event.key in (K_RIGHT, K_d):
                MoveLeft = False
                MoveRight = True
               
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_a):
                MoveLeft = False
            elif event.key in (K_RIGHT, K_d):
                MoveRight = False
            elif event.key in (K_UP, K_w):
                MoveUp = False
            elif event.key in (K_DOWN, K_s):
                MoveDown = False

            elif event.key == K_ESCAPE:
                terminate()

    if not GameOverMode:
            if MoveLeft:
                HKX -= MoveRate
            if MoveUp:
                HKY -= MoveRate
            if MoveRight == True:
                HKX += MoveRate
            if MoveDown:
                HKY += MoveRate
    fpsClock.tick(fps)
    pygame.display.update()
