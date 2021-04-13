#Importing Important Modules
import pygame
import random

#intialize the pygame
pygame.init()

#Created Game Window
screen = pygame.display.set_mode((800,600))

#Background
backgorund = pygame.image.load('/home/mrj/Documents/Python/Pygame/SpaceInvader/space.png')

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
enemyX = 0
enemyY = 480

enemyX_change = 10
enemyY_change = 30

#Bulle
bulletImg = pygame.image.load('/home/mrj/Documents/Python/Pygame/SpaceInvader/bullet.png')
bulletX = random.randint(0, 800)
bulletY = random.randint(50, 150)

bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg,(x ,y))

def enemy(x, y):
    screen.blit(enemyImg,(x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10)) 


#Main Game Loop
running = True
while running:

    #Background colour
    screen.fill((0, 0, 0))

    #background Image
    screen.blit(backgorund, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Keystroke left or right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -17
        if event.key == pygame.K_RIGHT:
            playerX_change = 17
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0


    #Backgorund colour
    screen.fill((2, 0, 9))

    #Checking Boundries Player
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736


    #Enemy Movement
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 10
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -10
        enemyY += enemyY_change
    
    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    
    
    pygame.display.update()
