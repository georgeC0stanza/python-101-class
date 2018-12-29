import pygame # for drawing to the screen
#import pdb #-- used for debugging with this method call pdb.set_trace()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1300, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --- global variables ---
#win conditions
win = False
objective_complete = False

#players postion (yeah i know this should be an object...)
player_position = [0] * 10
x = 70
y = 50
dx = 0
dy = 0
z = 0
dz = 0

#mario's image
player_image_size = 50
player_image_full = pygame.image.load("game-sprites\mario.png").convert()
player_image = pygame.transform.scale(player_image_full, (player_image_size, player_image_size))

#egg's image (pica was the placeholder for the egg in the alpha, need to refactor)
pica_size = 50
pica_image_full = pygame.image.load("game-sprites\egg.gif").convert()
pica_image = pygame.transform.scale(pica_image_full, (pica_size, pica_size))

pica_x = 160
pica_y = 340

#--- detects walls
def wall_collisions(x,y,dx,dy):
    if (x < 20):
        dx += 10
    if (x > 1250):
        dx -= 10
    if (y < 20):
        dy += 10
    if (y > 680):
        dy -= 10

    if (x < 1150 and (y < 150 and y > 130)):
        dy -= 20

    if (x > 520 and (y < 330 and y > 300)):
        dy -= 20
        
    if (x > 520 and (y < 510 and y > 530)):
        dy -= 10


    x += dx
    y += dy
    return [x, y]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                dx = -10
            elif event.key == pygame.K_RIGHT:
                dx = 10
            elif event.key == pygame.K_UP:
                dy = -10
            elif event.key == pygame.K_DOWN:
                dy = 10
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset dx/dy back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dz = 5
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dz = -5
                
 
    # --- Game logic should go here ---

    # --- mario's "jump"
    if player_image_size < 100:
        player_image_size += dz

    elif player_image_size > 50:
        player_image_size -= dz
    if player_image_size < 50:
        player_image_size = 50
    if player_image_size > 100:
        player_image_size = 99
    player_image = pygame.transform.scale(player_image_full, (player_image_size, player_image_size))

    # -- detect walls
    xy = wall_collisions(x,y,dx,dy)
    x = xy[0]
    y = xy[1]

    #-- did we meet the win condition?
    if (x < pica_x + 25 and x > pica_x - 25) and (y < pica_y + 25 and y > pica_y - 25):
        objective_complete = True
        pica_image = pygame.image.load("game-sprites\yoshi.jpg").convert()
        player_image_full = pygame.image.load("game-sprites\marioyoshi.jpg").convert()
    if (objective_complete == True and x > 1190 and y > 650):
        win = True
        
    # --- display ----

    screen.fill(BLACK)
    if win is False:
        screen.blit(pygame.image.load("game-sprites\maze.png").convert(), [1,1])
        screen.blit(player_image, [x,y])
        screen.blit(pica_image, [pica_x, pica_y])
    if win is True:
        screen.fill(BLACK)
        screen.blit(pygame.image.load("game-sprites\win.png").convert(), [1,1])    
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
