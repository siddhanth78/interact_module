import pygame
from pygame.locals import *
import random

fps = 15
running = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()

class Player():

    def __init__(self, player_x, player_y, player_state, player_vel):
        self.player_x = player_x
        self.player_y = player_y
        self.player_state = player_state
        self.player_vel = player_vel
        
    def getX(self):
        return self.player_x
        
    def getY(self):
        return self.player_y
        
    def setX(self, new_x):
        self.player_x = new_x
        
    def setY(self, new_y):
        self.player_y = new_y
        
    def setState(self, new_state):
        self.player_state = new_state
        
    def getState(self):
        return self.player_state
        
    def setVelocity(self, new_vel):
        self.player_vel = new_vel
        
    def getVelocity(self):
        return self.player_vel
        
    def wrapPlayer(self, maze_dim):
        #right
        if self.player_x+1 > maze_dim:
            self.player_x = 0
            
        #left
        elif self.player_x-1 < 0:
            self.player_x = maze_dim
        
        #down
        elif self.player_y+1 > maze_dim:
            self.player_y = 0
            
        #up
        elif self.player_y-1 < 0:
            self.player_y = maze_dim
            
def getTileColor(tile):
    if tile == 0:
        return (255, 255, 255)
    elif tile == 1:
        return (211, 211, 211)
    elif tile == 2:
        return (0, 255, 0)
    
        
        
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        
maze_dim = 19
        

player = Player(18, 18, 'up', 1)
        

while running:

    clock.tick(fps)
    
    screen.fill((0, 0, 0))
    
    tiles = []

    y = 0
    for row in maze:
        x = 0
        for tile in row:
            tiles.append((pygame.Rect(x, y, 25, 25), tile))
            x += 25
        y += 25
    
    for tile in tiles:
        color = getTileColor(tile[1])
        pygame.draw.rect(screen, color, tile[0])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.setState('up')
            if event.key == pygame.K_DOWN:
                player.setState('down')
            if event.key == pygame.K_LEFT:
                player.setState('left')
            if event.key == pygame.K_RIGHT:
                player.setState('right')
            if event.key == pygame.K_ESCAPE:
                running = False
    
    row = player.getY()
    col = player.getX()
    
    maze[row][col] = 0
    
    flag = 0
    
    if player.getState() == 'up':
        if row-1 < 0:
            flag = 1
        elif maze[row-1][col] == 1:
            pass
        else:
            row -= 1
    elif player.getState() == 'down':
        if row+1 > maze_dim:
            flag = 1
        elif maze[row+1][col] == 1:
            pass
        else:
            row += 1
    elif player.getState() == 'left':
        if col-1 < 0:
            flag = 1
        elif maze[row][col-1] == 1:
            pass
        else:
            col -= 1
    elif player.getState() == 'right':
        if col+1 > maze_dim:
            flag = 1
        elif maze[row][col+1] == 1:
            pass
        else:
            col += 1
    
    if flag == 1:
        player.wrapPlayer(maze_dim)
        row = player.getY()
        col = player.getX()
        
    player.setY(row)
    player.setX(col)
         
    maze[row][col] = 2
    
    pygame.display.update()
        