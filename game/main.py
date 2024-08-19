import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot


def draw_text(surface, text, size, x, y, bold=False):
    font_name = pygame.font.match_font('arial', bold)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'white')
    text_rectangle = text_surface.get_rect()
    text_rectangle.midleft = (x, y)
    surface.blit(text_surface, text_rectangle)


def main():
    pygame.init()

    # Define groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable, )
    Shoot.containers = (shots, drawable, updatable)

    # Setting up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    pygame_clock = pygame.time.Clock()
    pygame.display.set_caption('Asteroids!')

    # Objects used to play the game
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_filed = AsteroidField() # noqa

    # Keep track of score and asteroids destroyed
    score = 0
    asteroids_destroyed = 0
    new_life_counter = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                player.lives -= 1
                if player.lives <= 0:
                    print('Game Over')
                    return False
                asteroid.split()

            for shot in shots:
                if asteroid.collide(shot):
                    score += 100 - asteroid.radius
                    asteroids_destroyed += 1
                    new_life_counter += 1
                    shot.kill()
                    asteroid.split()

        # Determine if we should increase the number of lives
        if new_life_counter >= 100:
            # We'll limit to only 5 max lives
            if not player.lives >= 5:
                player.lives += 1

            new_life_counter = 0

        screen.fill(color='black')
        for item in drawable:
            item.draw(screen)
        draw_text(screen,
                  f'Score: {score}',
                  25, 50, 25, True)
        draw_text(screen,
                  f'Asteroids Destroyed: {asteroids_destroyed}',
                  15, 50, 50)
        draw_text(screen,
                  f'Lives left: {player.lives}',
                  15, SCREEN_WIDTH - 150, 25, True)
        pygame.display.flip()
        dt = pygame_clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
