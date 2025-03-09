import pygame
import sys

# Define constants based on your Tkinter modifications
GRID_WIDTH = 10
GRID_HEIGHT = 10
TILE_SIZE = 30
GAP = 5
CANVAS_SIZE_X = GRID_WIDTH * TILE_SIZE + GAP * GRID_WIDTH
CANVAS_SIZE_Y = GRID_HEIGHT * TILE_SIZE + GAP * GRID_HEIGHT
BACKGROUND_COLOR = (100, 100, 100)  # Green
TILE_COLOR = (0, 0, 0)          # Black

# Initialize Pygame
pygame.init()

# Create the screen with the modified size
screen = pygame.display.set_mode((CANVAS_SIZE_X, CANVAS_SIZE_Y))
pygame.display.set_caption("10x10 Tile Grid")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the grid using the new constants
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x = col * (TILE_SIZE + GAP) + GAP
            y = row * (TILE_SIZE + GAP) + GAP
            pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
