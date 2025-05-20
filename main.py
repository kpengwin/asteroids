# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import Player
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    Player.containers = (drawable, updateable)
    p = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        # get delta time in seconds
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)
        screen.fill(color="black")
        for d in drawable:
            d.draw(screen=screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
