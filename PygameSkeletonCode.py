#MAXWELL
import pygame, sys
from pygame.locals import *

screenWidth = 800
screenHeight = 600
FPS = 100
frame = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("")
pygame.init()

def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)

main()
