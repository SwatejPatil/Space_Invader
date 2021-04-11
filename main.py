#Importing Important Modules
import pygame
import random

#intialize the pygame
pygame.init()

#Created Game Window
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('/home/mrj/Documents/Python/Pygame/SpaceInvader/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('/home/mrj/Documents/Python/Pygame/SpaceInvader/001-jet.png')
playerX = 370
playerY = 480

playerX_change = 0

#Enemy
enemyImg = pygame.image.load('/home/mrj/Documents/Python/Pygame/SpaceInvader/alien.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)

enemyX_change = 0

def player(x, y):
    screen.blit(playerImg,(x ,y))

def enemy(x, y):
    screen.blit(enemyImg,(x, y))


#Main Game Loop
running = True
while running:
    #Backgorund colour
    screen.fill((25, 0, 25))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Keystroke left or right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -1
        if event.key == pygame.K_RIGHT:
            playerX_change = 1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0


    #Backgorund colour
    screen.fill((2, 0, 9))

    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736




    player(playerX, playerY)
    enemy(enemyX, enemyY)

    
    
    pygame.display.update()
