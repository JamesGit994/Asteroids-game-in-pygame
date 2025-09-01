import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullets import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_space = AsteroidField()
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)


# game loop starts
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        delte_time = fps.tick(60)
        dt = delte_time / 1000
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_detection(asteroid):
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
