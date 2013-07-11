# Import the libraries we'll need to write the game
import time
import random
import pygame

# Initialize PyGame, which is the software that lets us easily create games
pygame.init()
screen = pygame.display.set_mode([1200, 600])
myFont = pygame.font.SysFont("arial", 30)
random.seed(time.time())

# Load the background image
background = pygame.image.load("aquarium-background.jpg").convert()

def IsQuitting():
    """Check if user has asked to quit"""
    
    for event in pygame.event.get():
        
        # Window was closed
        if event.type == pygame.QUIT:
            return True
        
        # User pressed the Esc key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
            
    return False

class ClownFish:
    """The clown fish"""
    
    def __init__(self):
        """Create a clown fish"""
        
        # We have two images, one facing left and one facing right
        self.fish_left = pygame.image.load("fish/clown-fish-left.png").convert_alpha()
        self.fish_right = pygame.image.load("fish/clown-fish-right.png").convert_alpha()
        self.current_fish = self.fish_right

        # Start out in the middle bottom
        self.x = random.randint(200, 1000)
        self.y = 500

        # Start out moving a little to the right
        self.x_speed = random.randint(1, 3)
        self.y_speed = 0

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
            
    def draw(self):
        """Draw the clown fish in its current position"""
        screen.blit(self.current_fish, (self.x, self.y))
        
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
            
    def draw(self):
        """Draw the clown fish in its current position"""
        screen.blit(self.current_fish, (self.x + self.jiggle, self.y))
    
# Create the fish.  The ones later in the list are draw later and thus
# look like they are closer than the earlier ones.
all_fish = [ClownFish(), ClownFish(), SuckerFish()]

# Loop forever until the user quits, moving and drawing the fish
clock = pygame.time.Clock() 
while True:
    
    # Slow down the loop so that we display 60 frames per second (this is like a movie)
    tick_time = clock.tick(30)
    
    # Set the window title with some status information
    pygame.display.set_caption("Fishtank. FPS: %.2f FISH: %i" % (clock.get_fps(), len(all_fish)))

    # Check if quitting
    if IsQuitting():
        break

    # Move the fish
    for fish in all_fish:
        fish.move()
        
    # Draw the background image
    screen.blit(background, (0,0))
    
    # Draw the fish
    for fish in all_fish:
        fish.draw()
        
    # Draw the silly text
    screen.blit(myFont.render("Hello Fishies!", 0, (255,255,200)), (20,20))

    # Copy everything to the screen
    pygame.display.update()
    
