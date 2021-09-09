import pygame, sys, time, random
from pygame.locals import *

pygame.init()

fps = 30
fpsClock = pygame.time.Clock()

screenx = 800
screeny = 600

grassQuantity = 800
BerryQuantity = 14
SBerryQuantity = 2

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
    "MoveRight" : False,
    "Boost":False,
    "SpeedInterval":0
    }

#camera
camrax = 0
camray = 0
CameraSlack = 100

GameOverMode = False

GrassCollection=[]
BerryCollection=[]
SBerryCollection=[]

def getRandomOffCam(camerax, cameray, screenx, screeny,objwidth,objheight):
    cameraRect = pygame.Rect(camerax, cameray, screenx, screeny)
    while True:
        x = random.randint(camerax - screenx, camerax+2*screenx)
        y = random.randint(cameray - screeny, cameray+2*screeny)

        objRect = pygame.Rect(x,y,objwidth,objheight)
        if not objRect.colliderect(cameraRect):
            return x,y
        
def outsideactive(camerax, cameray, obj, screenx,screeny):
    leftBound = camerax - screenx
    topBound = cameray - screeny
    boundsRect = pygame.Rect(leftBound,topBound, screenx*3, screeny*3)
    objRect = pygame.Rect(obj.x,obj.y,obj.width, obj.height)
    return not boundsRect.colliderect(objRect)

def RefilHunger(player,quantity):
    player["HungerLevel"]+= quantity
    if player["HungerLevel"] > 50:
        player["HungerLevel"] = 50
    return player["HungerLevel"]

class GrassObj:
    def __init__(self,camrax, camray, screenx, screeny):
        self.image = pygame.image.load("grass.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x , self.y = getRandomOffCam(camrax, camray, screenx, screeny, self.width,self.height)
        rect = pygame.Rect(self.x,self.y,self.width,self.height)

class BerryObj:
    def __init__(self,camrax, camray, screenx, screeny):
        self.image = pygame.image.load("Berry.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x , self.y = getRandomOffCam(camrax, camray, screenx, screeny, self.width,self.height)
        self.rectObj = self.image.get_rect(topleft = (self.x,self.y))
        
class SBerryObj:
    def __init__(self,camrax, camray, screenx, screeny):
        self.image = pygame.image.load("SpeedBerry.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x , self.y = getRandomOffCam(camrax, camray, screenx, screeny, self.width,self.height)
        self.rectObj = self.image.get_rect(topleft = (self.x,self.y))
        
for i in range(100):
    GrassCollection.append("temp")
    GrassCollection[i] = GrassObj(camrax, camray, screenx, screeny)
    GrassCollection[i].x = random.randint(0,screenx)
    GrassCollection[i].y = random.randint(0,screeny)

for i in range(3):
    BerryCollection.append("temp")
    BerryCollection[i] = BerryObj(camrax, camray, screenx, screeny)
    BerryCollection[i].x = random.randint(0,screenx)
    BerryCollection[i].y = random.randint(0,screeny)
    BerryCollection[i].rectObj = pygame.Rect(BerryCollection[i].x,BerryCollection[i].y,BerryCollection[i].width,BerryCollection[i].height)

for i in range(1):
    SBerryCollection.append("temp")
    SBerryCollection[i] = SBerryObj(camrax, camray, screenx, screeny)
    SBerryCollection[i].x = random.randint(0,screenx)
    SBerryCollection[i].y = random.randint(0,screeny)
    SBerryCollection[i].rectObj = pygame.Rect(SBerryCollection[i].x,SBerryCollection[i].y,SBerryCollection[i].width,SBerryCollection[i].height)
    
while True: # main game loop
    surface.fill(colours["green"])
    
    #grass
    while len(GrassCollection)<grassQuantity:
        GrassCollection.append("temp")
        GrassCollection[len(GrassCollection)-1] = GrassObj(camrax, camray, screenx, screeny)
        
    for i in range(len(GrassCollection)-1):
        surface.blit(GrassCollection[i].image,(GrassCollection[i].x-camrax,GrassCollection[i].y-camray))

    #berry
    while len(BerryCollection)<BerryQuantity:
        BerryCollection.append("temp")
        BerryCollection[len(BerryCollection)-1] = BerryObj(camrax, camray, screenx, screeny)

    for i in range(len(BerryCollection)-1):
        surface.blit(BerryCollection[i].image,(BerryCollection[i].x-camrax,BerryCollection[i].y-camray))

    #Speed Berry
    while len(SBerryCollection)<SBerryQuantity:
        SBerryCollection.append("temp")
        SBerryCollection[len(SBerryCollection)-1] = SBerryObj(camrax, camray, screenx, screeny)

    for i in range(len(SBerryCollection)-1):
        surface.blit(SBerryCollection[i].image,(SBerryCollection[i].x-camrax,SBerryCollection[i].y-camray))
        
    if HungryKnight["HungerInterval"] != fps/2:
        HungryKnight["HungerInterval"]+=1
        
    else:
        HungryKnight["HungerInterval"]=0
        HungryKnight["HungerLevel"]-=1
        
    if HungryKnight["SpeedInterval"] != fps*10 and HungryKnight["Boost"] == True:
        HungryKnight["SpeedInterval"]+=1
        
    else:
        HungryKnight["SpeedInterval"]=0
        Boost = False
        HungryKnight["MoveRate"] = 5
        
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
            elif event.key is (K_h):
                HungryKnight["HungerLevel"] = RefilHunger(HungryKnight,10)

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
                
    for i in range(len(GrassCollection)-1,-1,-1):
        if outsideactive(camrax, camray, GrassCollection[i], screenx,screeny):
            del GrassCollection[i]
            
    for i in range(len(BerryCollection)-1,-1,-1):
        if outsideactive(camrax, camray, BerryCollection[i], screenx,screeny):
            del BerryCollection[i]
        
    for i in range(len(BerryCollection)-1,-1,-1):
       if ( BerryCollection[i].rectObj).colliderect(HungryKnight["PlayerIcon"].get_rect(topleft =(HungryKnight["HKX"],HungryKnight["HKY"]))):
            del BerryCollection[i]
            RefilHunger(HungryKnight,10)

    for i in range(len(SBerryCollection)-1,-1,-1):
       if ( SBerryCollection[i].rectObj).colliderect(HungryKnight["PlayerIcon"].get_rect(topleft =(HungryKnight["HKX"],HungryKnight["HKY"]))):
            del SBerryCollection[i]
            HungryKnight["MoveRate"] = 10
            HungryKnight["Boost"] = True
            HungryKnight["HungerInterval"]=0
            
    surface.blit(HungryKnight["HungerIcon"],(0,screeny-HungryKnight["HungerLevel"]))
    fpsClock.tick(fps)
    pygame.display.update()
