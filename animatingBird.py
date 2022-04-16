from tkinter import BOTTOM
import pygame
from sys import exit
from random import randint

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f' {current_time}',False,"Black")
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time   

def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5

			if obstacle_rect.bottom == 380: screen.blit(cactus_surf,obstacle_rect)
			else: screen.blit(fly_surf,obstacle_rect)

		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

		return obstacle_list
	else: return []

def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 350:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_run):
            player_index = 0
        player_surf = player_run[int(player_index)]

    return player_surf

    

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



#player
player_stand =  pygame.image.load('assetes/DinoStart.png').convert_alpha()

player_run1 =  pygame.image.load('assetes/DinoRun1.png').convert_alpha()
player_run2 =  pygame.image.load('assetes/DinoRun2.png').convert_alpha()
player_run = [player_run1, player_run2]
player_index = 0
player_jump = pygame.image.load('assetes/DinoJump.png').convert_alpha()

player_surf = player_run[player_index]
player_rect = player_surf.get_rect(midbottom=(80,380))
player_gravity = 0

#obstacles
cactus_surf = pygame.image.load('assetes/cactus.png').convert_alpha()
obstacle_rect_list = []

fly_frame1 = pygame.image.load('assetes/Bird1.png').convert_alpha()
fly_frame2 = pygame.image.load('assetes/Bird2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

# Intro screen
reset_surf =  pygame.image.load('assetes/reset.png').convert_alpha()
reset_rect = reset_surf.get_rect(center=(358, 202))

game_name = test_font.render('chrome dino',False,"Black")
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,"Black")
game_message_rect = game_message.get_rect(center = (400,330))

clock = pygame.time.Clock()

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)


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
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(cactus_surf.get_rect(bottomright = (randint(900,1100),380)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),285)))
            			
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: 
                    fly_frame_index = 1
                else: 
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index] 


    if game_active:
        screen.blit(bg_surf,(0,0))
        screen.blit(ground_surf,(0,367))
        
        score = display_score()


        #player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 380:
            player_rect.bottom = 380

        player_animation()
        screen.blit(player_surf, player_rect)

        #Obstacle movement
        obstacle_rect_list= obstacle_movement(obstacle_rect_list)

        #end the game
        game_active = collisions(player_rect,obstacle_rect_list)


        
    else:#menu screen
            obstacle_rect_list.clear()
            player_gravity = 0
            screen.fill("Grey") 
            
            score_message = test_font.render(f'Your score : {score} ',False,'Black')
            score_message_rect = score_message.get_rect(center = (400,330))
            screen.blit(game_name,game_name_rect)

            if score == 0: 
                screen.blit(player_stand, (358, 180))
                screen.blit(game_message,game_message_rect)
            else: 
                screen.blit(reset_surf,reset_rect)
                screen.blit(score_message,score_message_rect)
 

    pygame.display.update()
    clock.tick(60)

