import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((716, 404))
pygame.display.set_caption('basic')
test_font = pygame.font.Font(None, 50)

bg_surf = pygame.image.load('assetes/bg.png')
ground_surf = pygame.image.load('assetes/ground.png')
enemy_surf = pygame.image.load('assetes/enemy.png')
player_surf =  pygame.image.load('assetes/player.png')
score_surf = test_font.render('My game', False, 'White' )

player_gravity = 0

#create rectangle 
enemy_rect = enemy_surf.get_rect(topleft=(600, 270))
player_rect = player_surf.get_rect(topleft=(80,200))
score_rect = score_surf.get_rect(center = (600, 50) )

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 370:
                player_gravity = -20

        
    screen.blit(bg_surf,(0,0))
    screen.blit(ground_surf,(0,350))
    

    #pygame.draw.rect(display surface, color, rectangle, width , radus)
    pygame.draw.rect(screen, 'Grey', score_rect)
    pygame.draw.rect(screen, 'Grey', score_rect, 6, 10)
    screen.blit(score_surf, score_rect)


    #moving the enemy using rect
    enemy_rect.x -= 3
    if enemy_rect.right <= 0:
        enemy_rect.left= 800

    screen.blit(enemy_surf,enemy_rect)

    #keyboard input
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')
    '''

    #player
    player_gravity += 1
    player_rect.y += player_gravity

    if player_rect.bottom >= 370:
        player_rect.bottom = 370

    screen.blit(player_surf, player_rect)

 

    pygame.display.update()
    clock.tick(60)
