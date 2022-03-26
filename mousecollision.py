import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((716, 404))
pygame.display.set_caption('basic')

bg_surface = pygame.image.load('assetes/bg.png')
ground_surface = pygame.image.load('assetes/ground.png')
enemy_surface = pygame.image.load('assetes/enemy.png')
player_surf =  pygame.image.load('assetes/player.png')

#create rectangle 
enemy_rect = enemy_surface.get_rect(topleft=(600, 270))
player_rect = player_surf.get_rect(topleft=(80,200))


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            print(event.pos) 

    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    screen.blit(player_surf, player_rect)

    #moving the enemy using rect
    enemy_rect.x -= 3
    if enemy_rect.right <= 0:
        enemy_rect.left= 800

    screen.blit(enemy_surface,enemy_rect)

    '''
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        #print(pygame.mouse.get_pressed()) 
        print("collision")
    '''

    pygame.display.update()
    clock.tick(60)
