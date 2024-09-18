import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    (numpass, numfail) = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyclock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # This is weird - why not just define it in the class?
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # game logic
        for thing in updatable:
            thing.update(dt)
        for roid in asteroids:
            if roid.collision(player):
                print("Game over!")
                sys.exit()
        
        # redisplay all
        screen.fill(0, None, 0)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        dt = pyclock.tick(60) / 1000   # 60 fps, each tick is 1/60th of a second


if __name__ == "__main__":
    main()
