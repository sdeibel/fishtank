# Initialize PyGame, which is the software that lets us easily create games
import pygame
pygame.init()
screen = pygame.display.set_mode([1200, 600])
myFont = pygame.font.SysFont("arial", 30)

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
   
# Create the fish.  The ones later in the list are draw later and thus
# look like they are closer than the earlier ones.
from fish.clownfish import ClownFish
from fish.suckerfish import SuckerFish
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
        fish.draw(screen)
        
    # Draw the silly text
    screen.blit(myFont.render("Hello Fishies!", 0, (255,255,200)), (20,20))

    # Copy everything to the screen
    pygame.display.update()
    
