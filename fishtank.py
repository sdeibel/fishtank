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
   
# Create the fish.  The ones later in the list are drawn later and thus
# look like they are closer than the earlier ones.
from fish.clownfish import ClownFish
from fish.suckerfish import SuckerFish
from fish.frenchangelfish import FrenchAngelFish
all_fish = [ClownFish(screen), ClownFish(screen), FrenchAngelFish(screen)]
for i in range(0, 10):
    all_fish.append(ClownFish(screen))
all_fish.append(SuckerFish(screen))

# Loop forever until the user quits, moving and drawing the fish
clock = pygame.time.Clock() 
while True:
    
    # Slow down the loop so that we go through it 30 times per second, which means we show
    # 30 frames per second (FPS).  This is also about how many FPS most movies use.
    tick_time = clock.tick(30)
    
    # Set the window title with some status information 
    pygame.display.set_caption("Fishtank. FPS: %.2f FISH: %i" % (clock.get_fps(), len(all_fish)))

    # Check if quitting
    if IsQuitting():
        break

    # Move each fish
    for fish in all_fish:
        fish.move()
        
    # Draw the background image, each fish, and our silly text in that order (things
    # draw last end up in front)
    screen.blit(background, (0,0))
    for fish in all_fish:
        fish.draw(screen)
    screen.blit(myFont.render("Hello Fishies!", 0, (255,255,200)), (20,20))

    # Copy everything to the screen
    pygame.display.update()
    
