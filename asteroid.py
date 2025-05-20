from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    containers: tuple

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            new_angles = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for angle in new_angles: 
                _ = Asteroid(self.position.x, self.position.y, new_radius)
                _.velocity = angle * 1.2
