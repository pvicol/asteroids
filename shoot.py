from circleshape import CircleShape
from constants import *
import pygame


class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', radius=self.radius, width=2, center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt
