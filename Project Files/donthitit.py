"""
* @Program Name: 	Avoid Them All!
* @Author: 			Brian Peter
* @Description: 	This is a game in which you are supposed to avoid as many cars as possible! Build your score and maintain the highest record!
* @Version: 		0.01
* @Side Note: 		This is the first game I have ever written.
"""

import pygame, time, random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color = (53, 115, 255)

#Image demensions
moto_width = 45 #FIXME needs to be adjusted.
veh_width = 42

#Load the images
motoImg = pygame.image.load('moto.png')
roadImg = pygame.image.load('road.png')
grassImg = pygame.image.load('grass.png')
stripeImg = pygame.image.load('roadstripes.png')
ambImg = pygame.image.load('Ambulance.png')
audiImg = pygame.image.load('Audi.png')
copImg = pygame.image.load('Police.png')
viperImg = pygame.image.load('Black_viper.png')

#Set up the actual window
screenDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Avoid Them All!')
clock = pygame.time.Clock()

moto = Images(motoImg,(display_width * 0.45),(display_height * 0.8),screenDisplay)
grass = Images(grassImg,0,0,screenDisplay)
grass2 = Images(grassImg,0,-600,screenDisplay)
road = Images(roadImg,0,0,screenDisplay)
stripe = Images(stripeImg,0,0,screenDisplay)
stripe2 = Images(stripeImg,0,-600,screenDisplay)

"""
* @Type/Name:		Vehicle Class
* @Description:		This class is to call repetetive "enemy vehicles"
"""

class Vehicle(object):

	def __init__(self, vehW, vehH, vehImg, surface, vehSpd):
		self.vehicle_w = vehW
		self.vehicle_h = vehH
		self.vehicle_speed = vehSpd
		self.vehicle_img = vehImg
		self.vehicle_y = random.randrange(0 - 600 + self.vehicle_h, 0 - self.vehicle_h)
		self.vehicle_x = random.randrange(139,660 - self.vehicle_w)
		self.screenDisplay = surface

	def veh_move(self):
		self.vehicle_y += self.vehicle_speed
		self.screenDisplay.blit(self.vehicle_img, (self.vehicle_x, self.vehicle_y))

	def update(self):
		self.screenDisplay.blit(self.vehicle_img, (self.vehicle_x, self.vehicle_y))

"""
* @Type/Name:		ImagePlacement Class
* @Description:		This class is to load images and move them if required.
"""

class Images(object):

	def __init__(self, imgVar, x1, y1, surface):
		self.name = imgVar
		self.x = x1
		self.y = y1
		self.screen = surface

	def draw(self):
		self.screen.blit(self.name,(self.x,self.y))

	def bgMove(self):
		self.y += 10

	def motoMove(self,key):
		self.keyPress = key
		if self.keyPress = "keyLeft":
			self.x += -5

		if self.keyPress = "keyRight":
			self.x += 5

	def stopMove(self,key):
		self.x = 0

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black)
	screenDisplay.blit(text, (0,0))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115) #freesansbold.ttf
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	screenDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('You crashed!')

'''
def game_intro():

	intro = True

	staticList1 = [grass, stripe]
	staticList2 = [grass2, stripe2]

	imageDraw = [grass, grass2, road, stripe, stripe2, moto]

	for img in imageDraw:
		img.draw()

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		for statics in staticList1:
			if statics.statics_y < display_height:
				statics.bgMove()
			if statics.statics_y > display_height:
				statics.statics_y = 0
				statics.bgMove()

		for statics2 in staticList2:
			if statics2.statics2_y < display_height:
				statics2.bgMove()
			if statics2.statics2_y > display_height:
				statics2.statics2_y = -600
				statics2.bgMove()

		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects("You Can't Touch This!", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		screenDisplay.blit(TextSurf, TextRect)
		pygame.display.update()
		clock.tick(15)
'''

def game_loop():

	vehicleSpeed = random.randrange(2,8)
	vehicleW = 42
	vehicleH = 109
	dodged = 0

# = This is to set that we haven't crashed yet.
	gameExit = False

# = Defining different variables used within the game loop.
	staticList1 = [grass, stripe]
	staticList2 = [grass2, stripe2]

	imageDraw = [grass, grass2, road, stripe, stripe2, moto]

	vehList = [ambImg, audiImg, copImg, viperImg]
	vehicleList = [Vehicle(vehicleW, vehicleH, random.choice(vehList), screenDisplay, random.randrange(2,8)) for x in range(4)]

# = Beginning of the loop.
	while not gameExit:

# ===== Started with event handling.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					keyPress = "keyLeft"
					moto.motoMove(keyPress)
				elif event.key == pygame.K_RIGHT:
					keyPress = "keyRight"
					moto.motoMove(keyPress)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					moto.stopMove()

# ===== Draw the images and move them!
		for img in imageDraw:
			img.draw()

		for statics in staticList1:
			if statics.statics_y < display_height:
				statics.bgMove()
			if statics.statics_y > display_height:
				statics.statics_y = 0
				statics.bgMove()

		for statics2 in staticList2:
			if statics2.statics2_y < display_height:
				statics2.bgMove()
			if statics2.statics2_y > display_height:
				statics2.statics2_y = -600
				statics2.bgMove()

		for vehicle in vehicleList:
			if vehicle.vehicle_y < display_height:
				vehicle.veh_move()
			if vehicle.vehicle_y > display_height:
				vehicle.vehicle_y = random.randrange(0 - 600 + vehicle.vehicle_h, 0 - vehicle.vehicle_h)
				vehicle.vehicle_x = random.randrange(139,660 - vehicle.vehicle_w)
				vehicle.veh_move()
				dodged += 1

# ========= This still needs testing, continuing to hit vehicles accross the X axis when they are not visible on screen.
			if moto.y < vehicle.vehicle_y + vehicle.vehicle_h:
				if moto.x > vehicle.vehicle_x and moto.x < vehicle.vehicle_x + vehicle.vehicle_w or moto.x + moto_width > vehicle.vehicle_x and moto.x + moto_width < vehicle.vehicle_x + vehicle.vehicle_w:
					print('vehicle x crossover')
					print("you hit the other vicle X")
					crash()

# ===== Draw scores.
		things_dodged(dodged)

# ===== This makes it so you can't drive on the grass!
		if moto.x > display_width - 139 - moto_width or moto.x < 139:
			crash()

# ===== Update the vehicles locations.
		for vehicle in vehicleList:
			vehicle.update()

# ===== This updates the display.
		pygame.display.update()

# ===== This sets the frames per second.
		clock.tick(60)

# RUN THE PROGRAM!
#game_intro()
game_loop()

#You must exit pygames before quitting python.
pygame.quit()
quit()
