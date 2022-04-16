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

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

bg_surf = pygame.image.load('assetes/bg.png').convert_alpha()
ground_surf = pygame.image.load('assetes/ground.png').convert_alpha()
enemy_surf = pygame.image.load('assetes/enemy.png').convert_alpha()
player_surf =  pygame.image.load('assetes/player.png').convert_alpha()

reset_surf =  pygame.image.load('assetes/reset.png').convert_alpha()
reset_rect = reset_surf.get_rect(center=(358, 202))

player_gravity = 0

#create rectangle 
enemy_rect = enemy_surf.get_rect(midbottom=(600, 380))
player_rect = player_surf.get_rect(midbottom=(80,380))

# Intro screen
game_name = test_font.render('chrome dino',False,"Black")
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,"Black")
game_message_rect = game_message.get_rect(center = (400,330))

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
        
        score = display_score()


        #moving the enemy using rect
        enemy_rect.x -= 5
        if enemy_rect.right <= 0:
            enemy_rect.left= 800

        screen.blit(enemy_surf,enemy_rect)

      
       
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
        #menu screen
            screen.fill("Grey") 
            
            score_message = test_font.render(f'Your score : {score} ',False,'Black')
            score_message_rect = score_message.get_rect(center = (400,330))
            screen.blit(game_name,game_name_rect)

            if score == 0: 
                screen.blit(player_surf, (358, 202))
                screen.blit(game_message,game_message_rect)
            else: 
                screen.blit(reset_surf,reset_rect)
                screen.blit(score_message,score_message_rect)
 

    pygame.display.update()
    clock.tick(60)
