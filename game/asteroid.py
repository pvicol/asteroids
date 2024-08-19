from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
                screen,
                'white',
                radius=self.radius,
                width=2,
                center=self.position
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate new random angle/trajectory
        random_angle = random.uniform(20, 50)

        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create new asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set the velocity for the new asteroids
        asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
