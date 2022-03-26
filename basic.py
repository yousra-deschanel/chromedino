import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((716, 404))
pygame.display.set_caption('basic')

bg_surface = pygame.image.load('assetes/bg.png')
ground_surface = pygame.image.load('assetes/ground.png')
enemy_surface = pygame.image.load('assetes/enemy.png')


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    

   
    pygame.display.update()
    clock.tick(60)
