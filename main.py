# Get rid of the annoying pygame message for cleaner console
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import all python files & pygame
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init() # initialize Pygame
    
    # Variables

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set up display
    clock = pygame.time.Clock() # Ensure steady frame rate
    running = True # Main loop condition
    dt = 0 # delta time
    
    # Create the player instance
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x, y)
    asteroidfield = AsteroidField()
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        for a in asteroids:
            check = a.check_collision(player)
            if check == True:
                print("Game over!")
                return
        for a in asteroids:
            for s in shots:
                check = s.check_collision(a)
                if check == True:
                    a.split()
                    s.kill()

        dt = clock.tick(60) / 1000
        
    

# make sure the file is only called when run directly
if __name__ == "__main__":
    main()