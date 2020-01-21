import pygame
import random
pygame.init()

display_width   = 1280
display_height  =  960

black   = (  0,  0,  0)
white   = (255,255,255)
red     = (255,  0,  0)
green   = (  0,255,  0)
blue    = (  0,  0,225)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Neuro-Evolution")
clock = pygame.time.Clock()

plant_sprite = pygame.image.load("plant.png")
herbivore_sprite = pygame.image.load("herbivore.png")
carnivore_sprite = pygame.image.load("carnivore.png")

def position():
    x = random.randint(0, display_width)
    y = random.randint(0, display_height)
    return (x, y)

def spawn_plant():
    gameDisplay.blit(plant_sprite, position())

def spawn_herbivore():
    gameDisplay.blit(herbivore_sprite, position())

def spawn_carnivore():
    gameDisplay.blit(carnivore_sprite, position())

def run():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.fill(white)
        spawn_plant()
        spawn_herbivore()
        spawn_carnivore()
        pygame.display.update()
        clock.tick(30)
        




run()
pygame.quit()
quit()












"""
        for n in range(0,16):
            if n%1 == 0:
                spawn_plant()
            if n%4 == 0:
                spawn_herbivore()
            if n%8 == 0:
                spawn_carnivore()






"""
