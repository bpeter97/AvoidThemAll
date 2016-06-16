# Pygame template - skeleton for a new pygame project.
import pygame, random

WIDTH = 800
HEIGHT = 600
FPS = 30

# Define colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid Them All!")
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
	# Keep this running at the right speed.
	clock.tick(FPS)

	# Process Input (events)
	for event in pygame.event.get():
		# Check for closing the game.
		if event.type == pygame.QUIT:
			running = False

	# Update Section

	# Draw / Render Section
	screen.fill(BLACK)

	# Always do this last. *After drawing everything, flip the display.*
	pygame.display.flip()

pygame.quit()