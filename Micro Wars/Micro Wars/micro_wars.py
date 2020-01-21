import pygame
import random
import math

pygame.init()

display_width   = 800
display_height  = 600

cell_width  = 32
cell_height = 32

black   = (  0,  0,  0)
white   = (255,255,255)
red     = (255,  0,  0)
green   = (  0,255,  0)
blue    = (  0,  0,225)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Micro Wars!")
clock = pygame.time.Clock()

#game inputs/parameters:
#controls:
up      = pygame.K_w
down    = pygame.K_s
left    = pygame.K_a
right   = pygame.K_d
#variables:
starting_location = ((display_width - cell_width)/2, (display_height - cell_height)/2)
starting_hp = 64
speed       =  8
dna_points  =  0

#cell sprites:
cell_stationary     = pygame.image.load("cell_stationary.png")  #0
cell_up             = pygame.image.load("cell_up.png")          #1
cell_down           = pygame.image.load("cell_down.png")        #2
cell_left           = pygame.image.load("cell_left.png")        #3
cell_right          = pygame.image.load("cell_right.png")       #4
cell_upleft         = pygame.image.load("cell_upleft.png")      #5
cell_upright        = pygame.image.load("cell_upright.png")     #6
cell_downleft       = pygame.image.load("cell_downleft.png")    #7
cell_downright      = pygame.image.load("cell_downright.png")   #8

#loads the correct image for a given movement direction:
def displayCell(x, y, direction):
    if direction == 0:
        gameDisplay.blit(cell_stationary, (x,y))
    if direction == 1:
        gameDisplay.blit(cell_up, (x,y))
    if direction == 2:
        gameDisplay.blit(cell_down, (x,y))
    if direction == 3:
        gameDisplay.blit(cell_left, (x,y))
    if direction == 4:
        gameDisplay.blit(cell_right, (x,y))
    if direction == 5:
        gameDisplay.blit(cell_upleft, (x,y))
    if direction == 6:
        gameDisplay.blit(cell_upright, (x,y))
    if direction == 7:
        gameDisplay.blit(cell_downleft, (x,y))
    if direction == 8:
        gameDisplay.blit(cell_downright, (x,y))

#changes the location of the cell for a given direction:
def moveCell(direction):
    if direction == 0:  #stationary
        x_change = 0
        y_change = 0
    if direction == 1:  #up
        x_change = 0
        y_change = -1 * speed
    if direction == 2:  #down
        x_change = 0
        y_change = speed
    if direction == 3:  #left
        x_change = -1 * speed
        y_change = 0
    if direction == 4:  #right
        x_change = speed
        y_change = 0
    if direction == 5:  #upleft
        x_change = -1 * speed / math.sqrt(2)
        y_change = -1 * speed / math.sqrt(2)
    if direction == 6:  #upright
        x_change = speed / math.sqrt(2)
        y_change = -1 * speed / math.sqrt(2)
    if direction == 7:  #downleft
        x_change = -1 * speed / math.sqrt(2)
        y_change = speed / math.sqrt(2)
    if direction == 8:  #downright
        x_change = speed / math.sqrt(2)
        y_change = speed / math.sqrt(2)
    
    return (x_change, y_change)

def game_loop():
    (x,y) =  starting_location
    (x_change, y_change) = (0, 0)
    
    gameExit = False
    while not gameExit:
        direction = 0
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
                
            #handles directional key presses:
            if event.type == pygame.KEYDOWN:
                if event.key == up:
                    direction = moveCell(1)
                if event.key == down:
                    direction = moveCell(2)
                if event.key == left:
                    direction = moveCell(3)
                if event.key == right:
                    direction = moveCell(4)
                if event.key == up and event.key == left:
                    direction = moveCell(5)
                if event.key == up and event.key == right:
                    direction = moveCell(6)
                if event.key == down and event.key == left:
                    direction = moveCell(7)
                if event.key == down and event.key == right:
                    direction = moveCell(8)
            
        x += x_change
        y += y_change
        gameDisplay.fill(white)
        cell(x, y, direction)

        pygame.display.update()
        clock.tick(30)




game_loop()
pygame.quit()
quit()




    
