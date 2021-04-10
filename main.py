import pygame

#intialize the pygame
pygame.init()

#Created Game Window
screen = pygame.display.set_mode((800,600))

#Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
