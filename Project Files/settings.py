# Game options/settings.
TITLE = "Avoid Them All!"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheetimg.png"
SPRITESHEET2 = "can.png"
CLOUDSPRITE = "cloudsprite.png"

# Player Properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 22

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 3
PLATFORM_LAYER = 2
POW_LAYER = 2
MOB_LAYER = 3
CLOUD_LAYER = 1

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
				 (WIDTH - 500, HEIGHT * 3 / 4),
				 (450, HEIGHT - 500),
				 (230, 200),
				 (175,50)]

# Starting Clouds
CLOUDS_LIST = [(300, HEIGHT - 200),
			   (WIDTH - 360, HEIGHT * 3 / 4),
			   (200, HEIGHT - 450)]

# Define Color.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
CLOUDBLUE = (50, 139, 158)
CLOUDBLUE2 = (54, 145, 161)
BGCOLOR = SKYBLUE