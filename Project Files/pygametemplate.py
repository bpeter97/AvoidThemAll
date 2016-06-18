# Pygame template - skeleton for a new pygame project.
import pygame, random
from settings import *

"""

You are at 5:20 on https://www.youtube.com/watch?v=uWvb3QzA48c&index=18&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw


"""

# Initialize pygame and create window.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
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