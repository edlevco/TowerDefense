import pygame
import game_state

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

game = game_state.Game()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock for frame rate control
clock = pygame.time.Clock()

# # Game loop
def __main__():
    while game.game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_on = False

        # Fill screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Entry point
if __name__ == "__main__":
    print("run")
    __main__()

# Quit pygame
pygame.quit()
