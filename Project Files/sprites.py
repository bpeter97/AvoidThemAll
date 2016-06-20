# Sprite Classes for avoid
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Spritesheet:
	# Utility class for loading and parsing spritesheets
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert()

	def get_image(self, x, y, width, height):
		#grab image out of larger sheet.
		image = pg.Surface((width, height))
		image.blit(self.spritesheet, (0,0), (x, y, width, height))
		#if images too small, comment out next line or readjust.
		image = pg.transform.scale(image, (width // 2, height // 2))
		return image

class Player(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.walking = False
		self.jumping = False
		self.current_frame = 0
		self.last_update = 0
		self.load_images()
		self.image = self.standing_frames[0]
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(WIDTH / 2, HEIGHT / 2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def load_images(self):
		self.standing_frames = [self.game.spritesheet.get_image(357, 231, 55, 79),
								self.game.spritesheet.get_image(357, 231, 55, 79)]
		for frame in self.standing_frames:
			frame.set_colorkey(BLACK)
		self.walk_frames_r = [self.game.spritesheet.get_image(133, 198, 55, 79),
							  self.game.spritesheet.get_image(112, 278, 55, 79),
							  self.game.spritesheet.get_image(189, 231, 55, 79),
							  self.game.spritesheet.get_image(245, 231, 55, 79),
							  self.game.spritesheet.get_image(301, 231, 55, 79)]
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
		self.pos += self.vel + 0.5 * self.acc
		# Wrap around edges of screen
		if self.pos.x > WIDTH:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = WIDTH

		# Gather final position
		self.rect.midbottom = self.pos

	def animate(self):

		now = pg.time.get_ticks()
		if not self.jumping and not self.walking:
			if now - self.last_update > 350:
				self.last_update = now
				self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
				bottom = self.rect.bottom
				self.image = self.standing_frames[self.current_frame]
				self.rect = self.image.get_rect()
				self.rect.bottom = bottom

	def jump(self):
		# Jump only if standing on something
		self.rect.x += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 1
		if hits:
			self.vel.y = -PLAYER_JUMP

class Platform(pg.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w, h))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y