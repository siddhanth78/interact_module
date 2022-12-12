import pygame
from pygame.locals import *
import random


class Player():

    xpos = 200
    ypos = 475
        
        

class Bullet():

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
            
    def getX(self):
        return self.x
            
    def getY(self):
        return self.y
        

class Enemy():

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
            
    def getX(self):
        return self.x
            
    def getY(self):
        return self.y
        
    

pygame.init()

velocity = 8
mass = 1

running = True
jump = False
shoot = False

clock = pygame.time.Clock()

ammo = []
    
for i in range(10):
    ammo.append(Bullet(Player.xpos, Player.ypos))

screen = pygame.display.set_mode((500, 500))

font = pygame.font.Font(None, 32)
text = font.render(f"Ammo : {len(ammo)}", True, (255, 255, 255), (0, 0, 0))

target = Enemy(255, 0)
targetStatus = True

while running:
    
    clock.tick(60)

    screen.fill((0, 0, 0))
    
    gunXPos = Player.xpos - 10
    gunYPos = Player.ypos - 5
    
    pygame.draw.rect(screen, (0, 0, 255), (Player.xpos, Player.ypos, 25, 25))
    pygame.draw.rect(screen, (192, 192, 192), (gunXPos, gunYPos, 10, 28))
    
    if targetStatus == True:
        pygame.draw.rect(screen, (255, 0, 0), (target.getX(), target.getY(), 25, 25))
        
    if shoot == True:
        pygame.draw.circle(screen, (255, 255, 0), (ammo[-1].getX(), ammo[-1].getY()), 3)
        if (ammo[-1].getX() + 6 > target.getX() and ammo[-1].getX() < target.getX() + 25 and ammo[-1].getY() + 6 > target.getY() and ammo[-1].getY() < target.getY() + 25):
            targetStatus = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        Player.xpos -= 5
    elif keys[pygame.K_RIGHT]:
        Player.xpos += 5
    
    if shoot == False:
        if keys[pygame.K_SPACE] and len(ammo) > 0:
            text = font.render(f"Ammo : {len(ammo) - 1}", True, (255, 255, 255), (0, 0, 0))
            ammo[-1].setX(gunXPos + 5)
            ammo[-1].setY(gunYPos)
            shoot = True
            
    if shoot == True:
        ammo[-1].setY(ammo[-1].getY() - 10)
        if ammo[-1].getY() < 0:
            ammo[-1].setY(-10)
            usedBullet = ammo.pop(-1)
            del usedBullet
            shoot = False
    
    '''if jump == False:
        if keys[pygame.K_SPACE]:
            jump = True
        
    if jump == True:
        force = 0.5 * mass * (velocity**2)
        Player.ypos -= force
        velocity -= 1
        if velocity < 0:
            mass = -1
        if velocity == -9:
            jump = False
            velocity = 8
            mass = 1'''
            
    screen.blit(text, (380, 10))
    
    pygame.display.update()