import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fps = 30
fpsClock = pygame.time.Clock()

screenx = 800
screeny = 600

surface = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Hungry Knight Clone')

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

#camera
camrax = 0
camray = 0
CameraSlack = 100

GameOverMode = False




while True: # main game loop
    surface.fill(colours["green"])
    surface.blit(HungryKnight["HungerIcon"],(0,screeny-HungryKnight["HungerLevel"]))
    surface.blit(pygame.image.load("grass.png"),(300-camrax,300-camray))
    
    if HungryKnight["HungerInterval"] != fps/2:
        HungryKnight["HungerInterval"]+=1
    else:
        HungryKnight["HungerInterval"]=0
        HungryKnight["HungerLevel"]-=1
    if HungryKnight["HungerLevel"] == 0:
        GameOverMode = True
    playerx = HungryKnight["HKX"] + 25
    playery = HungryKnight["HKY"] + 25    
    if (camrax + screenx/2) - playerx > CameraSlack:
        camrax = playerx + (CameraSlack - (screenx/2))
    elif playerx - (camrax + screenx/2) > CameraSlack:
        camrax = playerx - (CameraSlack + (screenx/2))
    if (camray + screeny/2) - playery > CameraSlack:
        camray = playery + (CameraSlack - (screeny/2))
    elif playery - (camray + screeny/2) > CameraSlack:
        camray = playery - (CameraSlack + (screeny/2))
      
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
            surface.blit(HungryKnight["PlayerIcon"],(HungryKnight["HKX"]-camrax,HungryKnight["HKY"]-camray))
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
