import pygame
import random
import time

class ClownFish:
    """The clown fish"""
    
    def __init__(self, screen):
        """Create a clown fish"""

        self.screen = screen
        
        # We have two images, one facing left and one facing right
        self.fish_left = pygame.image.load("fish/clown-fish-left.png").convert_alpha()
        self.fish_right = pygame.image.load("fish/clown-fish-right.png").convert_alpha()
        self.current_fish = self.fish_right

        # Start out in the middle bottom
        self.x = random.randint(200, 1000)
        self.y = 500
        self.z = 1.0

        # Start out moving a little to the right
        self.x_speed = random.randint(1, 3)
        self.y_speed = 0
        self.z_speed = 0

        # Keep track of times for last direction and speed changes so fish moves more smoothly
        self.last_direction_change = time.time()
        self.last_x_speed_change = time.time()
        self.last_y_speed_change = time.time()
        self.last_slow_down = time.time()
        
    def move(self):
        """Move the fish in a way that looks right for the clown fish"""

        # Move the fish according to its speed and direction
        self.x += self.x_speed
        self.y += self.y_speed
        self.z += self.z_speed
        
        if self.z > 2.0:
            self.z = 2.0
            self.z_speed = 0
        elif self.z < 0.0:
            self.z = 0.0
            self.z_speed = 0

        # Fish changes direction left to right once in a while, at most every 3 seconds
        if time.time() > self.last_direction_change + 3.0:
            
            r = random.randint(0, 100)
            
            # Don't change direction towards end of tank when close to it
            if self.x_speed > 0 and self.x < 200:
                r = 0
            elif self.x_speed < 0 and self.x > 1000:
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
                
        # Fish loses momentum and slows down in X direction at rate of one unit of speed per second
        if time.time() > self.last_slow_down + 1.0:
            if self.x_speed < 0:
                self.x_speed += 1
            else:
                self.x_speed -= 1
            self.last_slow_down = time.time()
            
        r = random.randint(0, 100)
        if r == 1:
            self.z_speed += 0.01
        elif r == 2:
            self.z_speed -= 0.01
        
        # Bounce off the edges by reversing direction
        if self.x > 1050 and self.x_speed > 0:
            self.x_speed = -self.x_speed
        elif self.x < 0 and self.x_speed < 0:
            self.x_speed = -self.x_speed
        if self.y > 400 and self.y_speed > 0:
            self.y_speed = -self.y_speed
        elif self.y < 0 and self.y_speed < 0:
            self.y_speed = -self.y_speed
        
        # Change to using correct fish image
        if self.x_speed > 0:
            self.current_fish = self.fish_right
        elif self.x_speed < 0:
            self.current_fish = self.fish_left
            
    def draw(self, screen):
        """Draw the clown fish in its current position"""
        w, h = self.current_fish.get_size()
        w = int((w * 0.10) * self.z + w)
        h = int((h * 0.10) * self.z + h)
        fish = pygame.transform.scale(self.current_fish, (w, h))
        screen.blit(fish, (self.x, self.y))
