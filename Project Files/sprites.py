# Sprite Classes for avoid
import pygame as pg
from settings import *
from random import choice, randrange
vec = pg.math.Vector2

class Spritesheet:

	# Utility class for loading and parsing spritesheets
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert()

	def get_image(self, x, y, width, height):
		#grab image out of larger sheet.
		image = pg.Surface((width, height))
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		#Commented out next line due to image being perfect at original size.
		#image = pg.transform.scale(image, (width // 2, height // 2))
		return image

class Player(pg.sprite.Sprite):

	def __init__(self, game):
		self._layer = PLAYER_LAYER
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.walking = False
		self.jumping = False
		self.current_frame = 0
		self.last_update = 0
		self.load_images()
		self.image = self.standing_frames[0]
		self.rect = self.image.get_rect()
		self.rect.center = (40, HEIGHT - 100)
		self.pos = vec(40, HEIGHT - 100)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def load_images(self):
		self.standing_frames = [self.game.spritesheet.get_image(357, 231, 55, 79),
								self.game.spritesheet.get_image(357, 231, 55, 79)]
		for frame in self.standing_frames:
			frame.set_colorkey(BLACK)
		self.walk_frames_r = [self.game.spritesheet.get_image(134, 199, 53, 78),
							  self.game.spritesheet.get_image(113, 279, 53, 78),
							  self.game.spritesheet.get_image(190, 232, 53, 78),
							  self.game.spritesheet.get_image(246, 232, 53, 78),
							  self.game.spritesheet.get_image(302, 232, 53, 78)]
		for frame in self.walk_frames_r:
			frame.set_colorkey(BLACK)
		self.walk_frames_l = []
		for frame in self.walk_frames_r:
			frame.set_colorkey(BLACK)
			self.walk_frames_l.append(pg.transform.flip(frame, True, False))

		self.jump_frame = self.game.spritesheet.get_image(56, 244, 55, 79)
		self.jump_frame.set_colorkey(BLACK)

	def update(self):
		self.animate()
		self.acc = vec(0, PLAYER_GRAV)
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC

		# Apply Friction
		self.acc.x += self.vel.x * PLAYER_FRICTION
		# Equations of Motion
		self.vel += self.acc
		if abs(self.vel.x) < 0.1:
			self.vel.x = 0
		self.pos += self.vel + 0.5 * self.acc
		# Wrap around edges of screen
		if self.pos.x > WIDTH + self.rect.width / 2:
			self.pos.x = 0 - self.rect.width / 2
		if self.pos.x < 0 - self.rect.width / 2:
			self.pos.x = WIDTH + self.rect.width / 2

		# Gather final position
		self.rect.midbottom = self.pos

	def animate(self):
		now = pg.time.get_ticks()
		
		# Check if character is moving.
		if self.vel.x != 0:
			self.walking = True
		else:
			self.walking = False

		# Animate character when walking.
		if self.walking:
			if now - self.last_update > 100:
				self.last_update = now
				self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
				#bottom = self.rect.bottom
				if self.vel.x > 0:
					self.image = self.walk_frames_r[self.current_frame]
				else:
					self.image = self.walk_frames_l[self.current_frame]
				#self.rect = self.image.get_rect()
				#self.rect.bottom = bottom

		# This is the code to animate the idle character.
		if not self.jumping and not self.walking:
			if now - self.last_update > 350:
				self.last_update = now
				self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
				#bottom = self.rect.bottom
				self.image = self.standing_frames[self.current_frame]
				#self.rect = self.image.get_rect()
				#self.rect.bottom = bottom 

		self.mask = pg.mask.from_surface(self.image)

	def jump(self):
		# Jump only if standing on something
		self.rect.x += 2
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 2
		if hits and not self.jumping:
			self.game.jump_sound.play()
			self.jumping = True
			self.vel.y = -PLAYER_JUMP

class Platform(pg.sprite.Sprite):

	def __init__(self, game, x, y):
		self._layer = PLATFORM_LAYER
		self.groups = game.all_sprites, game.platforms
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game

		images = [self.game.spritesheet.get_image(6, 4, 222, 47),
				 self.game.spritesheet.get_image(3, 203, 121, 35)]
		self.image = choice(images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		if randrange(100) < POW_SPAWN_PCT:
			Pow(self.game, self)

class Clouds(pg.sprite.Sprite):

	def __init__(self, game, x, y):
		self._layer = CLOUD_LAYER
		self.groups = game.all_sprites, game.clouds
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game

		clouds = [self.game.cloudsprite.get_image(0, 0, 900,  600), 
				  self.game.cloudsprite.get_image(0, 601, 900,  600),
				  self.game.cloudsprite.get_image(901, 0, 900,  600)]

		self.image = choice(clouds)
		self.image = pg.transform.scale(self.image, (900 // 2, 600 // 2))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Pow(pg.sprite.Sprite):

	def __init__(self, game, plat):
		self._layer = POW_LAYER
		self.groups = game.all_sprites, game.powerups
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.plat = plat
		self.type = choice(['boost'])
		self.image = self.game.spritesheet2.get_image(0, 0, 18, 34)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = self.plat.rect.centerx
		self.rect.bottom = self.plat.rect.top - 5

	def update(self):
		self.rect.bottom = self.plat.rect.top - 5
		if not self.game.platforms.has(self.plat):
			self.kill()

class Mob(pg.sprite.Sprite):	

	def __init__(self, game):
		self._layer = MOB_LAYER
		self.groups = game.all_sprites, game.mobs
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image_up = self.game.spritesheet.get_image(208, 165, 97, 49)
		self.image_up.set_colorkey(BLACK)
		self.image_mid = self.game.spritesheet.get_image(309, 85, 97, 56)
		self.image_mid.set_colorkey(BLACK)
		self.image_down = self.game.spritesheet.get_image(208, 75, 97, 60)
		self.image_down.set_colorkey(BLACK)
		self.image = self.image_up
		self.rect = self.image.get_rect()
		self.rect.centerx = choice([-100, WIDTH + 100])
		self.dx = 0
		self.vx = randrange(1, 4)
		if self.rect.centerx > WIDTH:
			self.vx *= -1
			self.dx = 1
		else:
			self.dx = 0
		self.rect.y = randrange(HEIGHT / 2)
		self.vy = 0
		self.dy = 0.5

	def update(self):
		self.rect.x += self.vx
		self.vy += self.dy

		if self.vy > 3 or self.vy < -3:
			self.dy *= -1

		center = self.rect.center

		if self.dx == 0:
			if self.dy < 0 and self.vy < 1.5:
				self.image = self.image_mid
			elif self.dy < 0 and self.vy > 1.5: 
				self.image = self.image_up
			else:
				self.image = self.image_down
		else:
			if self.dy < 0 and self.vy < 1.5:
				self.image = pg.transform.flip(self.image_mid, True, False)
			elif self.dy < 0 and self.vy > 1.5: 
				self.image = pg.transform.flip(self.image_up, True, False)
			else:
				self.image = pg.transform.flip(self.image_down, True, False)

		self.mask = pg.mask.from_surface(self.image)

		self.rect = self.image.get_rect()
		self.rect.center = center
		self.rect.y += self.vy
		if self.rect.left > WIDTH + 100 or self.rect.right < -100:
			self.kill()