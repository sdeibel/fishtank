import pygame
import random
import time

class SuckerFish:
    
    def __init__(self):
        """Create a clown fish"""
        
        # We have four images depending on direction
        self.fish_left_up = pygame.image.load("fish/sucker-fish-left-up.png").convert_alpha()
        self.fish_right_up = pygame.image.load("fish/sucker-fish-right-up.png").convert_alpha()
        self.fish_left_down = pygame.image.load("fish/sucker-fish-left-down.png").convert_alpha()
        self.fish_right_down = pygame.image.load("fish/sucker-fish-right-down.png").convert_alpha()
        self.current_fish = self.fish_right_up

        # Start out at left bottom
        self.x = random.randint(100, 1000)
        self.y = 420

        # Start out moving up and to right
        self.x_speed = 1
        self.y_speed = -1
        
        # Fish jiggles left to right
        self.jiggle = 0
        self.jiggle_incr = 1
        
    def move(self):
        """Move the fish in a way that looks right for the clown fish"""

        # Move the fish according to its speed and direction
        self.x += self.x_speed
        self.y += self.y_speed

        # Fish jiggles left to right as it goes
        self.jiggle += self.jiggle_incr
        if self.jiggle > 2 or self.jiggle < -2:
            self.jiggle_incr = -self.jiggle_incr
        
        # Bounce off the edges by reversing direction
        if self.x > 1050 and self.x_speed > 0:
            self.x_speed = -self.x_speed
        elif self.x < 0 and self.x_speed < 0:
            self.x_speed = -self.x_speed
        if self.y > 420 and self.y_speed > 0:
            self.y_speed = -self.y_speed
        elif self.y < 0 and self.y_speed < 0:
            self.y_speed = -self.y_speed
        
        # Change to using correct fish image
        if self.x_speed > 0:
            if self.y_speed > 0:
                self.current_fish = self.fish_right_down
            else:
                self.current_fish = self.fish_right_up
        elif self.x_speed < 0:
            if self.y_speed > 0:
                self.current_fish = self.fish_left_down
            else:
                self.current_fish = self.fish_left_up
            
    def draw(self, screen):
        """Draw the clown fish in its current position"""
        screen.blit(self.current_fish, (self.x + self.jiggle, self.y))
 