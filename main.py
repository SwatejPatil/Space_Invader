#Importing Important Modules
import pygame

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

def player():
    screen.blit(playerImg,(playerX, playerY))
#Main Game Loop
running = True
while running:
    #Backgorund colour
    screen.fill((25, 0, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Backgorund colour
    screen.fill((25, 0, 25))

    player()
    pygame.display.update()
