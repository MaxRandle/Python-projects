#MAXWELL
import pygame, sys
from pygame.locals import *

screenWidth = 800
screenHeight = 600
FPS = 100
frame = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Brick Breaker")
pygame.init()

#platform class
class Platform:
    def __init__(self):
        self.w = 64
        self.h = 8
        self.pos = [screenWidth/2 - self.w/2, screenHeight - self.h]
        self.plat = Rect(self.pos[0], self.pos[1], self.w, self.h)

    def sketch(self):
        pygame.draw.rect(frame, (255, 255, 255), self.plat, 0)

#ball class
class Ball:
    def __init__(self):
        self.pos = [screenWidth/2, screenHeight/2]
        self.r = 6
        self.vel = [0, 0]
        self.g = 1

    def sketch(self):
        pygame.draw.circle(frame, (255, 255, 255), (int(self.pos[0]), int(self.pos[1])), self.r, 0)

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[1] += self.g

    def collision(self, plat):
        if (self.pos[1]+self.r) >= plat.pos[1]:
            return True
        elif (self.pos[1] <= 0):
            return True
        else:
            return False
        
#main loop
def main():

    platform = Platform()
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        frame.fill((0, 0, 0))
        
        ball.move()
        if ball.collision(platform) == True:
            ball.vel[1] = -1 * ball.vel[1]
            
        ball.sketch()
        platform.sketch()
        
        pygame.display.update()
        clock.tick(FPS)

main()


















