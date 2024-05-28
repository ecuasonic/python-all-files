"""
On my honor, I will abstain from all deceit. I
will neither give nor receive unacknowledged aid
in my academic work nor will I permit such action
by any member of this community. I will respect
the persons and property of the community, and will
not condone the discourteous or dishonest treatment
of these by my peers.
Braxton Wannamaker
November 3rd, 2021
This program is 
"""

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #initialize game and great scam object
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.setmode((ai_settings.screen,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in
    bullets=Group()
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        #Redraw the screen during each passs through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the most recently drawn screen visible
        pygame.display.flip()
run_game()
