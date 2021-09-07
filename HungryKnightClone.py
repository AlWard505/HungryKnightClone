import pygame, sys, time
from pygame.locals import *

pygame.init()

fps = 30
fpsClock = pygame.time.Clock()

screenx = 800
screeny = 600
surface = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('PyGameIntro')

colours = {#    R   G   B
    "white" : (255,255,255),
    "red"   : (255,  0,  0),
    "green" : (  0,255,  0)
    }

#character varibles
HungryKnight ={
    "PlayerIcon": pygame.image.load("HK.png"),
    "HungerIcon": pygame.image.load("Hunger.png"),
    "HungerLevel": 50,
    "HungerInterval":0,
    "HKX":400,
    "HKY":300,
    "MoveRate" : 5,
    "MoveDown" : False,
    "MoveUp" : False,
    "MoveLeft" : False,
    "MoveRight" : False
    }

GameOverMode = False



while True: # main game loop
    surface.fill(colours["green"])
    surface.blit(HungryKnight["PlayerIcon"],(HungryKnight["HKX"],HungryKnight["HKY"]))
    surface.blit(HungryKnight["HungerIcon"],(0,screeny-HungryKnight["HungerLevel"]))
    if HungryKnight["HungerInterval"] != fps/2:
        HungryKnight["HungerInterval"]+=1
    else:
        HungryKnight["HungerInterval"]=0
        HungryKnight["HungerLevel"]-=1
    if HungryKnight["HungerLevel"] == 0:
        GameOverMode = True
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key in (K_UP,K_w):
                HungryKnight["MoveDown"] = False
                HungryKnight["MoveUp"] = True
            elif event.key in (K_DOWN, K_s):
                HungryKnight["MoveUp"]= False
                HungryKnight["MoveDown"] = True
            elif event.key in (K_LEFT, K_a):
                HungryKnight["MoveRight"] = False
                HungryKnight["MoveLeft"] = True
            elif event.key in (K_RIGHT, K_d):
                HungryKnight["MoveLeft"] = False
                HungryKnight["MoveRight"] = True
               
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_a):
                HungryKnight["MoveLeft"] = False
            elif event.key in (K_RIGHT, K_d):
                HungryKnight["MoveRight"] = False
            elif event.key in (K_UP, K_w):
                HungryKnight["MoveUp"] = False
            elif event.key in (K_DOWN, K_s):
                HungryKnight["MoveDown"] = False

            elif event.key == K_ESCAPE:
                terminate()

    if not GameOverMode:
            if HungryKnight["MoveLeft"]:
                HungryKnight["HKX"] -= HungryKnight["MoveRate"]
            if HungryKnight["MoveUp"]:
                HungryKnight["HKY"] -= HungryKnight["MoveRate"]
            if HungryKnight["MoveRight"] == True:
                HungryKnight["HKX"] += HungryKnight["MoveRate"]
            if HungryKnight["MoveDown"]:
                HungryKnight["HKY"] += HungryKnight["MoveRate"]

    fpsClock.tick(fps)
    pygame.display.update()
