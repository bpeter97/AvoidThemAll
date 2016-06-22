# Game options/settings.
TITLE = "Avoid Them All!"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheetimg.png"

# Player Properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
				 (WIDTH - 50, HEIGHT * 3 / 4),
				 (125, HEIGHT - 350),
				 (230, 200),
				 (175,100)]

# Define Color.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = SKYBLUE