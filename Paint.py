import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

# Brush settings
brush_size = 5
brush_down = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            brush_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            brush_down = False
        elif event.type == pygame.MOUSEMOTION:
            if brush_down:
                pygame.draw.circle(screen, current_color, event.pos, brush_size)

    pygame.display.update()
