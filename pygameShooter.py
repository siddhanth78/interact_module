import pygame
from pygame.locals import *
import random
from math import degrees, atan2

class Player():

    xpos = 200
    ypos = 475
    
class Bullet():

    xpos = 0
    ypos = 0
    endx = None
    endy = None
    flag = 0
    damage = 10
    
class Enemy():
    
    xpos = 100
    ypos = 100
    health = 100
    flag = 1
    
class FirePower():

    xpos = 200
    ypos = 200
    flag = 1
    damage_increase = 5

pygame.init()

velocity = 8
mass = 1

running = True
jump = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

scale = (25, 25)
powscale = (35, 25)

player_img_org = pygame.image.load(r'C:\Users\siddh\OneDrive\Desktop\Coding\assets\test.png').convert_alpha()
player_img_org = pygame.transform.scale(player_img_org, scale)

crosshair = pygame.image.load(r'C:\Users\siddh\OneDrive\Desktop\Coding\assets\crosshair.png').convert_alpha()

pygame.mouse.set_visible(False)

bullets = []

enemy = Enemy()
enemy_img = pygame.Surface((25, 25))
enemy_rect = enemy_img.get_rect(center = (enemy.xpos, enemy.ypos))

powerup = FirePower()

powerup_img = pygame.image.load(r'C:\Users\siddh\OneDrive\Desktop\Coding\assets\powerup.png').convert_alpha()
powerup_img = pygame.transform.scale(powerup_img, powscale)
powerup_rect = powerup_img.get_rect(center = (FirePower.xpos, FirePower.ypos))

def rotateImg(screen, player_img, player_rect, x, y, angle):
    player_img_copy = pygame.transform.rotate(player_img, angle)
    player_rect_copy = player_img_copy.get_rect(center = player_img.get_rect(center = (x, y)).center)
    screen.blit(player_img_copy, player_rect_copy)
    return player_img_copy
    
def shoot(bullets,x, y, ex, ey):
    bullet = Bullet()
    bullet.xpos = x
    bullet.ypos = y
    bullet.endx = ex
    bullet.endy = ey
    bullet.flag = 1
    bullets.append(bullet)
    return bullets

while running:
    
    clock.tick(60)

    screen.fill((0, 255, 0))
    
    player_rect_org = player_img_org.get_rect(center = (Player.xpos, Player.ypos))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            bullets = shoot(bullets, Player.xpos, Player.ypos, mouse_x, mouse_y)

    x_ = mouse_x - Player.xpos
    y_ = mouse_y - Player.ypos
    angle = degrees(-atan2(y_, x_))
    player_img = rotateImg(screen, player_img_org, player_rect_org, Player.xpos, Player.ypos, angle)  
    player_rect = player_img.get_rect(center = (Player.xpos, Player.ypos))
    
    crosshair_rect = crosshair.get_rect(center = (mouse_x, mouse_y))
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        Player.xpos -= 5
        if Player.xpos == -25:
            Player.xpos = 500
    elif keys[pygame.K_d]:
        Player.xpos += 5
        if Player.xpos == 500:
            Player.xpos = -25
    elif keys[pygame.K_w]:
        Player.ypos -= 5
        if Player.ypos == -25:
            Player.ypos = 500
    elif keys[pygame.K_s]:
        Player.ypos += 5
        if Player.ypos == 500:
            Player.ypos = -25
    
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
            
    if Player.xpos+15 > powerup.xpos and Player.xpos < powerup.xpos+10 and Player.ypos+15 > powerup.ypos and Player.ypos < powerup.ypos+15:
        if powerup.flag == 1:
            Bullet.damage += powerup.damage_increase
        powerup.flag = 0
    
    for i in range(len(bullets)):
        bullet_surf = pygame.Surface((10, 10))
        bullet_surf.fill((255, 255, 0))
        bullet_rect = bullet_surf.get_rect(center = (bullets[i].xpos, bullets[i].ypos))
        if bullets[i].xpos < bullets[i].endx:
            bullets[i].xpos += 10
        if bullets[i].xpos > bullets[i].endx:
            bullets[i].xpos -= 10
        if bullets[i].ypos < bullets[i].endy:
            bullets[i].ypos += 10
        if bullets[i].ypos > bullets[i].endy:
            bullets[i].ypos -= 10
            
        if bullets[i].xpos+10 > bullets[i].endx and bullets[i].xpos < bullets[i].endx+10 and bullets[i].ypos+10 > bullets[i].endy and bullets[i].ypos < bullets[i].endy+10:
            bullets[i].flag = 0
        if bullets[i].xpos+15 > enemy.xpos and bullets[i].xpos < enemy.xpos+15 and bullets[i].ypos+15 > enemy.ypos and bullets[i].ypos < enemy.ypos+15:
            enemy.health -= bullets[i].damage
            bullets[i].flag = 0
        else:
            screen.blit(bullet_surf, bullet_rect)

    bullets = list(filter(lambda b: (b.flag == 1), bullets))
    
    if enemy.health <= 0:
        enemy.flag = 0
    
    if enemy.flag == 1:
        screen.blit(enemy_img, enemy_rect)
        
    screen.blit(player_img, player_rect)
    
    if powerup.flag == 1:
        screen.blit(powerup_img, powerup_rect)
        
    screen.blit(crosshair, crosshair_rect)
    pygame.display.update()