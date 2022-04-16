import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((716, 404))
pygame.display.set_caption('basic')

bg_surface = pygame.image.load('assetes/bg.png')
ground_surface = pygame.image.load('assetes/ground.png')
enemy_surface = pygame.image.load('assetes/enemy.png')

enemy_x_pos = 600

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,350))

    #moving the enemy 
    enemy_x_pos -= 3
    
    if enemy_x_pos <= -100:
        enemy_x_pos= 800

    screen.blit(enemy_surface,(enemy_x_pos,275))
    
    pygame.display.update()
    clock.tick(60)
