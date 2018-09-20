'''
Created on 12/02/2018

@author: developer
'''
import pygame
import time
import random
from pkg_resources._vendor.pyparsing import White
from compiler.pyassem import Block

display_width  = 800 
display_height = 600 
green =(105, 255, 105 )
white = (255,255,255)
black = (0, 0, 0) 
red = (255, 0 , 0) #rgb
blue = (150, 180 , 255 ,255)
FPS = 30

block_size = 10

pygame.init() # init the surface 


        
# DEFINE FONT IN THE SCREEN
font = pygame.font.SysFont(None, 20)
def message_to_screen( msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit( screen_text, [display_height/ 2, display_width /2])



gameDisplay = pygame.display.set_mode((display_width, display_height))   # gameDisplay = surface

pygame.display.set_caption("Snake-game")


clock = pygame.time.Clock()
def game_loop():
    gameExit = False
    gameOver = False
    
    AppleX = random.randrange(0, display_width - block_size)
    AppleY = random.randrange(0, display_height - block_size)
  
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    
    while not gameExit:
        
        while gameOver == True:
           gameDisplay.fill(green)
           message_to_screen("end Of the game, press C to play again or Q to quit", white ) 
           pygame.display.update()
           
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       gameExit = True
                       gameOver = False
                   if event.key == pygame.K_c:
                       game_loop()
     
           
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = - block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size 
                    lead_y_change = 0
                   #if event.type == pygame.KEYDOWN:                                              
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size  
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size 
                    lead_x_change = 0
                    
    # bounderes
    
        if lead_x < 0 or lead_x >= 800 - 10 or lead_y < 0 or lead_y >= 600 - 10:
            gameOver = True
           
                
                
        clock.tick(FPS) 
        
    
        lead_x = lead_x + lead_x_change
        lead_y = lead_y + lead_y_change 
    #UPDATE
        gameDisplay.fill(blue)            # gameDisplay obj
    
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
        pygame.draw.rect(gameDisplay, green, [ AppleX , AppleY , block_size, block_size])
        
        pygame.display.update()   # Dislpay all content 
    message_to_screen(" you lose ", red)
    
 #   pygame.display.update()
    # end of the loop
 #   time.sleep(2)
    
    pygame.quit() # end of the init() method
    quit() # end of the programm
    
     # tHE SQUARE STOP TO RUN
game_loop()
    
    