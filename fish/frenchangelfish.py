import pygame
import random
import time

class FrenchAngelFish:
    """The angel fish"""
    
    def __init__(self, screen):
        """Create an angel fish"""

        self.screen = screen
        
        # We have two images, one facing left and one facing right
        self.fish_left = pygame.image.load("fish/frenchangelfish-left.png").convert_alpha()
        self.fish_right = pygame.image.load("fish/frenchangelfish-right.png").convert_alpha()
        self.current_fish = self.fish_right

        # Figure out size of fish
        fishrect = self.current_fish.get_bounding_rect()
        self.width = fishrect.width
        self.height = fishrect.height
        
        # Start out in the middle bottom
        self.x = random.randint(200, 1000)
        screenrect = screen.get_bounding_rect()
        self.y = screenrect.height - fishrect.height

        # Start out moving a little to the right
        self.x_speed = random.randint(1, 3)
        self.y_speed = 0

        # Keep track of times for last direction and speed changes so fish moves more smoothly
        self.last_direction_change = time.time()
        self.last_x_speed_change = time.time()
        self.last_y_speed_change = time.time()
        self.last_slow_down = time.time()
        
    def move(self):
        """Move the fish in a way that looks right for the angel fish"""

        # Move the fish according to its speed and direction
        self.x += self.x_speed
        self.y += self.y_speed

        # Fish changes direction left to right once in a while, at most every 3 seconds
        if time.time() > self.last_direction_change + 3.0:
            
            r = random.randint(0, 100)
            
            # Don't change direction towards end of tank when close to it
            if self.x_speed > 0 and self.x < 300:
                r = 0
            elif self.x_speed < 0 and self.x > 900:
                r = 0
                
            # Don't change direction if going fast
            if abs(self.x_speed) > 4:
                r = 0
                
            if r == 1:
                
                # Change direction
                self.x_speed = -self.x_speed
                
                # Also lose a little speed with each turn
                if self.x_speed > 0:
                    self.x_speed -= 1
                elif self.x_speed < 0:
                    self.x_speed += 1
                    
                # Keep track of time we turned
                self.last_direction_change = time.time()
                
        # Fish speeds up periodically in X direction but at most every 3 seconds
        if time.time() > self.last_x_speed_change + 3.0:
            r = random.randint(0, 30)
            if r == 1:
                new_speed = random.randint(5, 9)
                if new_speed > abs(self.x_speed):
                    if self.x_speed < 0:
                        self.x_speed = -new_speed
                    else:
                        self.x_speed = new_speed
                    self.last_x_speed_change = time.time()

        # Fish drifts up and down periodically but changes direction at most once every 3 seconds
        if time.time() > self.last_y_speed_change + 3.0:
            r = random.randint(0, 100)
            if r == 1:
                self.y_speed = -1
                self.last_y_speed_change = time.time()
            elif r == 2:
                self.y_speed = 1
                self.last_y_speed_change = time.time()
            elif r == 3:
                self.y_speed = 0
                self.last_y_speed_change = time.time()
        
        # Don't go up or down unless going fairly fast
        if abs(self.x_speed) < 3:
            self.y_speed = 0
                
        # Fish loses momentum and slows down in X direction at rate of one unit of speed per second
        if time.time() > self.last_slow_down + 1.0:
            if self.x_speed < 0:
                self.x_speed += 1
            else:
                self.x_speed -= 1
            self.last_slow_down = time.time()
        
        # Bounce off the edges by reversing direction
        if self.x > 900 and self.x_speed > 0:
            self.x_speed = -self.x_speed
        elif self.x < 0 and self.x_speed < 0:
            self.x_speed = -self.x_speed
        if self.y > 300 and self.y_speed > 0:
            self.y_speed = -self.y_speed
        elif self.y < 0 and self.y_speed < 0:
            self.y_speed = -self.y_speed
        
        # Change to using correct fish image
        if self.x_speed > 0:
            self.current_fish = self.fish_right
        elif self.x_speed < 0:
            self.current_fish = self.fish_left
            
    def draw(self, screen):
        """Draw the angel fish in its current position"""
        screen.blit(self.current_fish, (self.x, self.y))
