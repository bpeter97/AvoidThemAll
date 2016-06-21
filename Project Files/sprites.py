# Sprite Classes for avoid
import pygame as pg
from settings import *
from random import choice
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
		#image = pg.transform.scale(image, (width // 2, height // 2))
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
		pg.sprite.Sprite.__init__(self)
		self.game = game
		images = [self.game.spritesheet.get_image(6, 4, 222, 47),
				 self.game.spritesheet.get_image(3, 203, 121, 35)]
		self.image = choice(images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y