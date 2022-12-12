import pygame
from pygame.locals import *
import random


class Square(pygame.sprite.Sprite):
 
    def __init__(self, color):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        
class Player():

    xpos = 500/2
    ypos = 375
    
class Enemy():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getEnemyXPos(self):
        return self.x
        
    def getEnemyYPos(self):
        return self.y
        
def setPositions(mode):
    if(mode == 'v'):
        x = random.randint(0, 475)
        y = random.randint(0, 10)
    elif(mode == 'h'):
        x = random.randint(0, 10)
        y = random.randint(0, 375)
    return x, y

pygame.init()
 
screen = pygame.display.set_mode((500, 400))
player = Square((0, 200, 255))

enemy1 = Square((238, 75, 43))
enemy2 = Square((238, 75, 43))
enemy3 = Square((238, 75, 43))
enemy4 = Square((238, 75, 43))
enemy5 = Square((238, 75, 43))

enemies = []

for i in range(5):
    enemies.append(Enemy(random.randint(0, 475), random.randint(0, 10)))
    
enemy1_xpos = enemies[0].getEnemyXPos()
enemy2_xpos = enemies[1].getEnemyXPos()
enemy3_xpos = enemies[2].getEnemyXPos()
enemy4_xpos = enemies[3].getEnemyXPos()
enemy5_xpos = enemies[4].getEnemyXPos()

enemy1_ypos = enemies[0].getEnemyYPos()
enemy2_ypos = enemies[1].getEnemyYPos()
enemy3_ypos = enemies[2].getEnemyYPos()
enemy4_ypos = enemies[3].getEnemyYPos()
enemy5_ypos = enemies[4].getEnemyYPos()

enemy1_mode = 'v'
enemy2_mode = 'v'
enemy3_mode = 'v'
enemy4_mode = 'v'
enemy5_mode = 'v'

clock = pygame.time.Clock()

running = True

modes = ['v', 'h']

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        Player.xpos -= 5
    elif keys[pygame.K_RIGHT]:
        Player.xpos += 5
    elif keys[pygame.K_UP]:
        Player.ypos -= 5
    elif keys[pygame.K_DOWN]:
        Player.ypos += 5
        
    if enemy1_mode == 'v':
        enemy1_ypos += 3
    elif enemy1_mode == 'h':
        enemy1_xpos += 3

    if enemy2_mode == 'v':
        enemy2_ypos += 3
    elif enemy2_mode == 'h':
        enemy2_xpos += 3
        
    if enemy3_mode == 'v':
        enemy3_ypos += 3
    elif enemy3_mode == 'h':
        enemy3_xpos += 3
        
    if enemy4_mode == 'v':
        enemy4_ypos += 3
    elif enemy4_mode == 'h':
        enemy4_xpos += 3
        
    if enemy5_mode == 'v':
        enemy5_ypos += 3
    elif enemy5_mode == 'h':
        enemy5_xpos += 3
    
    if(Player.xpos + 25 > enemy1_xpos and Player.xpos < enemy1_xpos + 25 and Player.ypos + 25 > enemy1_ypos and Player.ypos < enemy1_ypos + 25):
        print("YOU LOSE!")
        running = False
        
    if(Player.xpos + 25 > enemy2_xpos and Player.xpos < enemy2_xpos + 25 and Player.ypos + 25 > enemy2_ypos and Player.ypos < enemy2_ypos + 25):
        print("YOU LOSE!")
        running = False
        
    if(Player.xpos + 25 > enemy3_xpos and Player.xpos < enemy3_xpos + 25 and Player.ypos + 25 > enemy3_ypos and Player.ypos < enemy3_ypos + 25):
        print("YOU LOSE!")
        running = False
        
    if(Player.xpos + 25 > enemy4_xpos and Player.xpos < enemy4_xpos + 25 and Player.ypos + 25 > enemy4_ypos and Player.ypos < enemy4_ypos + 25):
        print("YOU LOSE!")
        running = False
        
    if(Player.xpos + 25 > enemy5_xpos and Player.xpos < enemy5_xpos + 25 and Player.ypos + 25 > enemy5_ypos and Player.ypos < enemy5_ypos + 25):
        print("YOU LOSE!")
        running = False

    #Mode 'v' -- Vertical

    if enemy1_ypos >= 395 and enemy1_mode == 'v':
        enemy1_mode = random.choice(modes)
        enemy1_xpos, enemy1_ypos = setPositions(enemy1_mode)
    
    if enemy2_ypos >= 395 and enemy2_mode == 'v':
        enemy2_mode = random.choice(modes)
        enemy2_xpos, enemy2_ypos = setPositions(enemy2_mode)
        
    if enemy3_ypos >= 395 and enemy3_mode == 'v':
        enemy3_mode = random.choice(modes)
        enemy1_xpos, enemy1_ypos = setPositions(enemy3_mode)
        
    if enemy4_ypos >= 395 and enemy4_mode == 'v':
        enemy4_mode = random.choice(modes)
        enemy4_xpos, enemy4_ypos = setPositions(enemy4_mode)
        
    if enemy5_ypos >= 395 and enemy5_mode == 'v':
        enemy5_mode = random.choice(modes)
        enemy5_xpos, enemy5_ypos = setPositions(enemy5_mode)
    
    #Mode 'h' -- Horizontal
    
    if enemy1_xpos >= 495 and enemy1_mode == 'h':
        enemy1_mode = random.choice(modes)
        enemy1_xpos, enemy1_ypos = setPositions(enemy1_mode)
    
    if enemy2_xpos >= 495 and enemy2_mode == 'h':
        enemy2_mode = random.choice(modes)
        enemy2_xpos, enemy2_ypos = setPositions(enemy2_mode)
        
    if enemy3_xpos >= 495 and enemy3_mode == 'h':
        enemy3_mode = random.choice(modes)
        enemy3_xpos, enemy3_ypos = setPositions(enemy3_mode)
        
    if enemy4_xpos >= 495 and enemy4_mode == 'h':
        enemy4_mode = random.choice(modes)
        enemy4_xpos, enemy4_ypos = setPositions(enemy4_mode)
        
    if enemy5_xpos >= 495 and enemy5_mode == 'h':
        enemy5_mode = random.choice(modes)
        enemy5_xpos, enemy5_ypos = setPositions(enemy5_mode)
    
    screen.fill((0,0,0))
    screen.blit(player.surf, (Player.xpos, Player.ypos))
    
    screen.blit(enemy1.surf, (enemy1_xpos, enemy1_ypos))
    screen.blit(enemy2.surf, (enemy2_xpos, enemy2_ypos))
    screen.blit(enemy3.surf, (enemy3_xpos, enemy3_ypos))
    screen.blit(enemy4.surf, (enemy4_xpos, enemy4_ypos))
    screen.blit(enemy5.surf, (enemy5_xpos, enemy5_ypos))

    pygame.display.update()
    
    clock.tick(60)