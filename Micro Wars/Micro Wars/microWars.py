import pygame
import random
import math

pygame.init()

displayWidth   = 800
displayHeight  = 600
CenterScreen = ((displayWidth)/2, (displayHeight)/2)

cell_width  = 32
cell_height = 32

black   = (  0,  0,  0)
white   = (255,255,255)
red     = (255,  0,  0)
green   = (  0,255,  0)
blue    = (  0,  0,225)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Micro Wars!")
clock = pygame.time.Clock()

#game inputs/parameters:
#controls:
up      = pygame.K_w
down    = pygame.K_s
left    = pygame.K_a
right   = pygame.K_d

#cell sprites:
cellSprite_Stationary     = pygame.image.load("cell_stationary.png")  #0
cellSprite_Up             = pygame.image.load("cell_up.png")          #1
cellSprite_Down           = pygame.image.load("cell_down.png")        #2
cellSprite_Left           = pygame.image.load("cell_left.png")        #3
cellSprite_Right          = pygame.image.load("cell_right.png")       #4
cellSprite_UpLeft         = pygame.image.load("cell_upleft.png")      #5
cellSprite_UpRight        = pygame.image.load("cell_upright.png")     #6
cellSprite_DownLeft       = pygame.image.load("cell_downleft.png")    #7
cellSprite_DownRight      = pygame.image.load("cell_downright.png")   #8

#cell class
class Cell:
    def __init__(self, x = centerScreen[0] - cellWidth/2, y = centerScreen[1] - cellHeight/2):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.direction = 0
        self.speed = 8
        self.hp = 64
        self.DNA = 0

        
    #getters
    def getPos(self):
        return pos
    
    def getDirection(self):
        return direction

    def getSpeed(self):
        return speed

    def getHP(self):
        return hp

    def getDNA(self):
        return DNA
        





