from tkinter import BOTTOM
import pygame
from sys import exit

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f' {current_time}',False,"Black")
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time   
    

pygame.init()

SCREEN_WIDTH = 716
SCREEN_HIGHT = 404

screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HIGHT ))
pygame.display.set_caption('basic')
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0

bg_surf = pygame.image.load('assetes/bg.png')
ground_surf = pygame.image.load('assetes/ground.png')
enemy_surf = pygame.image.load('assetes/enemy.png')
player_surf =  pygame.image.load('assetes/player.png')

#score_surf = test_font.render('My game', False, 'White' )

player_gravity = 0

#create rectangle 
enemy_rect = enemy_surf.get_rect(midbottom=(600, 380))
player_rect = player_surf.get_rect(midbottom=(80,380))
#score_rect = score_surf.get_rect(center = (600, 50) )

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 370:
                    player_gravity = -25
        else: 
            #press space to restart the game 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 750 #to stop the collaps between the player and the enemy after the game ends
                start_time = int(pygame.time.get_ticks() / 1000)
        
        
                   
    if game_active:
        screen.blit(bg_surf,(0,0))
        screen.blit(ground_surf,(0,367))
        

        #pygame.draw.rect(display surface, color, rectangle, width , radus)
        #pygame.draw.rect(screen, 'Grey', score_rect)
        #pygame.draw.rect(screen, 'Grey', score_rect, 6, 10)
        #screen.blit(score_surf, score_rect)

        display_score()


        #moving the enemy using rect
        enemy_rect.x -= 5
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

        if player_rect.bottom >= 380:
            player_rect.bottom = 380

        screen.blit(player_surf, player_rect)

        #end the game
        if enemy_rect.colliderect(player_rect):
                game_active= False
        
    else:
            screen.fill("Red") #menu screen
 

    pygame.display.update()
    clock.tick(60)
