
import pygame
from pygame.locals import *
import random
import time
import ctypes


# print(time.localtime()[3])

pygame.init()
w=ctypes.windll.user32.GetSystemMetrics(0)
h=ctypes.windll.user32.GetSystemMetrics(1)

screen=pygame.display.set_mode((w, h), pygame.FULLSCREEN)
pygame.display.set_caption("Snakes N Ladders")
pygame.display.update()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()
pygame.mixer.music.load('victory.mp3')
# pygame.mixer.music.play()


clock = pygame.time.Clock()

font_1              = pygame.font.Font("Notice Things.ttf", 30)
pos                 = ''
array_pos           = [(0, 0), (0, 0), (0, 0), (0, 0)]
array_taple         = [(0, 0), (0, 0), (0, 0), (0, 0)]
bg                  = pygame.image.load('bg.jpg')
icon                = pygame.image.load('logoAnjoman.png')
pygame.display.set_icon(icon)
img_map             = pygame.image.load('map.jpg')
img_victory         = pygame.image.load('victory.png')
img_victory         = pygame.transform.scale(img_victory, (500, 200))
img_False           = pygame.image.load('False.jpg')
img_False           = pygame.transform.scale(img_False, (320, 320))
img_True            = pygame.image.load('True.jpg')
img_speak           = pygame.image.load('speak.png')
img_dontspeak       = pygame.image.load('dontspeak.png')
mainDice            = pygame.image.load("Side1.png")
side1               = pygame.image.load("Side1.png")
side1               = pygame.transform.scale(side1, (50, 50))
side2               = pygame.image.load("Side2.png")
side2               = pygame.transform.scale(side2, (50, 50))
side3               = pygame.image.load("Side3.png")
side3               = pygame.transform.scale(side3, (50, 50))
side4               = pygame.image.load("Side4.png")
side4               = pygame.transform.scale(side4, (50, 50))
side5               = pygame.image.load("Side5.png")
side5               = pygame.transform.scale(side5, (50, 50))
side6               = pygame.image.load("Side6.png")
side6               = pygame.transform.scale(side6, (50, 50))

img_dota_blue       = pygame.image.load('blueround.png')
img_dota_blue       = pygame.transform.scale(img_dota_blue, (80, 80))
img_dota_red        = pygame.image.load('redround.png')
img_dota_red        = pygame.transform.scale(img_dota_red, (80, 80))
img_dota_green      = pygame.image.load('greenround.png')
img_dota_green      = pygame.transform.scale(img_dota_green, (80, 80))
img_dota_yellow     = pygame.image.load('yellowround.png')
img_dota_yellow     = pygame.transform.scale(img_dota_yellow, (80, 80))

img_forward1        = pygame.image.load('forward1.png')
img_forward3        = pygame.image.load('forward3.png')
img_forward4        = pygame.image.load('forward4.png')
img_forward5        = pygame.image.load('forward5.png')
img_forward6        = pygame.image.load('forward6.png')
img_endRaw          = pygame.image.load('EndRaw.png')
img_pos2first       = pygame.image.load('pos2first.png')
img_pos2next        = pygame.image.load('pos2next.png')

img_back2           = pygame.image.load('back2.png')
img_back3           = pygame.image.load('back3.png')
img_back4           = pygame.image.load('back4.png')
img_back5           = pygame.image.load('back5.png')
img_back6           = pygame.image.load('back6.png')
img_pos2last        = pygame.image.load('pos2last.png')
img_pos2previus     = pygame.image.load('pos2previus.png')
img_strtRaw         = pygame.image.load('strtRaw.png')

img_exit            = pygame.image.load('exit2.png')
img_exit            = pygame.transform.scale(img_exit, (165, 85))
img_start           = pygame.image.load('start2.png')
img_start           = pygame.transform.scale(img_start, (165, 85))
img_return          = pygame.image.load('return.png')
img_about_us        = pygame.image.load('aboutus2.png')
img_about_us        = pygame.transform.scale(img_about_us, (165, 85))
img_rolls           = pygame.image.load('rolls_button2.png')
img_rolls           = pygame.transform.scale(img_rolls, (165, 85))
img_1p              = pygame.image.load('1p.png')
img_2p              = pygame.image.load('2p.png')
img_2p              = pygame.transform.scale(img_2p, (200, 50))
img_3p              = pygame.image.load('3p.png')
img_3p              = pygame.transform.scale(img_3p, (200, 50))
img_4p              = pygame.image.load('4p.png')
img_4p              = pygame.transform.scale(img_4p, (200, 50))

img_blue            = pygame.image.load('blue.png')
img_blue            = pygame.transform.scale(img_blue, (140, 140))
img_red             = pygame.image.load('red.png')
img_red             = pygame.transform.scale(img_red, (140, 140))
img_green           = pygame.image.load('green.png')
img_green           = pygame.transform.scale(img_green, (140, 140))
img_yellow          = pygame.image.load('yellow.png')
img_yellow          = pygame.transform.scale(img_yellow, (140, 140))
credit_pic          = pygame.image.load('credit.png')
credit_pic          = pygame.transform.scale(credit_pic, (w-240, h-200))
rolls_pic           = pygame.image.load('rolls.png')
rolls_pic           = pygame.transform.scale(rolls_pic, (w-100, h-200))

blue_hit_right_1    = pygame.image.load('blue_hit_right_1.png')
blue_hit_right_1    = pygame.transform.scale(blue_hit_right_1, (50, 50))
blue_hit_right_2    = pygame.image.load('blue_hit_right_2.png')
blue_hit_right_2    = pygame.transform.scale(blue_hit_right_2, (50, 50))
blue_hit_left_1     = pygame.image.load('blue_hit_left_1.png')
blue_hit_left_1     = pygame.transform.scale(blue_hit_left_1, (50, 50))
blue_hit_left_2     = pygame.image.load('blue_hit_left_2.png')
blue_hit_left_2     = pygame.transform.scale(blue_hit_left_2, (50, 50))

hit_blue            = [blue_hit_right_1, blue_hit_right_2, blue_hit_left_1, blue_hit_left_2]

red_hit_right_1     = pygame.image.load('red_hit_right_1.png')
red_hit_right_1     = pygame.transform.scale(red_hit_right_1, (50, 50))
red_hit_right_2     = pygame.image.load('red_hit_right_2.png')
red_hit_right_2     = pygame.transform.scale(red_hit_right_2, (50, 50))
red_hit_left_1      = pygame.image.load('red_hit_left_1.png')
red_hit_left_1      = pygame.transform.scale(red_hit_left_1, (50, 50))
red_hit_left_2      = pygame.image.load('red_hit_left_2.png')
red_hit_left_2      = pygame.transform.scale(red_hit_left_2, (50, 50))

hit_red             = [red_hit_right_1, red_hit_right_2, red_hit_left_1, red_hit_left_2]

green_hit_right_1   = pygame.image.load('green_hit_right_1.png')
green_hit_right_1   = pygame.transform.scale(green_hit_right_1, (50, 50))
green_hit_right_2   = pygame.image.load('green_hit_right_2.png')
green_hit_right_2   = pygame.transform.scale(green_hit_right_2, (50, 50))
green_hit_left_1    = pygame.image.load('green_hit_left_1.png')
green_hit_left_1    = pygame.transform.scale(green_hit_left_1, (50, 50))
green_hit_left_2    = pygame.image.load('green_hit_left_2.png')
green_hit_left_2    = pygame.transform.scale(green_hit_left_2, (50, 50))

hit_green           = [green_hit_right_1, green_hit_right_2, green_hit_left_1, green_hit_left_2]

yellow_hit_right_1  = pygame.image.load('yellow_hit_right_1.png')
yellow_hit_right_1  = pygame.transform.scale(yellow_hit_right_1, (50, 50))
yellow_hit_right_2  = pygame.image.load('yellow_hit_right_2.png')
yellow_hit_right_2  = pygame.transform.scale(yellow_hit_right_2, (50, 50))
yellow_hit_left_1   = pygame.image.load('yellow_hit_left_1.png')
yellow_hit_left_1   = pygame.transform.scale(yellow_hit_left_1, (50, 50))
yellow_hit_left_2   = pygame.image.load('yellow_hit_left_2.png')
yellow_hit_left_2   = pygame.transform.scale(yellow_hit_left_2, (50, 50))

hit_yellow          = [yellow_hit_right_1, yellow_hit_right_2, yellow_hit_left_1, yellow_hit_left_2]

color_img           = [img_blue, img_red, img_green, img_yellow]
diceSides           = [side1, side2, side3, side4, side5, side6, 0]
diceSides_shans     = [side1, side2, side6, side3, side5, side6, side4, side5, side6, side1, side3, side6]
number_ask          = ['0.5', '1', '2', '3', '4', '5', '6', '4', '6']
function_ask        = ['*', '/', '+', '-']
num_ask             = [0.5, 1, 2, 3, 4, 5, 6, 4, 6]
a ,b                = (w-500)/2, (h-500)/2+450
u, z                = (w-500)/2-200, (h-500)/2+450
array_ask           = [(a+100, b), (a+350, b), (a+200, b-50), (a+100, b-100), (a+350, b-100), (a, b-150), (a+300, b-200), (a+100, b-250), (a+350, b-250), (a+50, b-300), (a+250, b-300), (a+300, b-350), (a+100, b-400), (a+350, b-400), (a+50, b-450), (a+300, b-450)]

blue_right_1        = pygame.image.load('blue_right_1.png')
blue_right_1        = pygame.transform.scale(blue_right_1, (45, 45))
blue_right_2        = pygame.image.load('blue_right_2.png')
blue_right_2        = pygame.transform.scale(blue_right_2, (45, 45))
blue_left_1         = pygame.image.load('blue_left_1.png')
blue_left_1         = pygame.transform.scale(blue_left_1, (45, 45))
blue_left_2         = pygame.image.load('blue_left_2.png')
blue_left_2         = pygame.transform.scale(blue_left_2, (45, 45))

red_right_1         = pygame.image.load('red_right_1.png')
red_right_1         = pygame.transform.scale(red_right_1, (45, 45))
red_right_2         = pygame.image.load('red_right_2.png')
red_right_2         = pygame.transform.scale(red_right_2, (45, 45))
red_left_1          = pygame.image.load('red_left_1.png')
red_left_1          = pygame.transform.scale(red_left_1, (45, 45))
red_left_2          = pygame.image.load('red_left_2.png')
red_left_2          = pygame.transform.scale(red_left_2, (45, 45))

green_right_1       = pygame.image.load('green_right_1.png')
green_right_1       = pygame.transform.scale(green_right_1, (45, 45))
green_right_2       = pygame.image.load('green_right_2.png')
green_right_2       = pygame.transform.scale(green_right_2, (45, 45))
green_left_1        = pygame.image.load('green_left_1.png')
green_left_1        = pygame.transform.scale(green_left_1, (45, 45))
green_left_2        = pygame.image.load('green_left_2.png')
green_left_2        = pygame.transform.scale(green_left_2, (45, 45))

yellow_right_1       = pygame.image.load('yellow_right_1.png')
yellow_right_1       = pygame.transform.scale(yellow_right_1, (45, 45))
yellow_right_2       = pygame.image.load('yellow_right_2.png')
yellow_right_2       = pygame.transform.scale(yellow_right_2, (45, 45))
yellow_left_1        = pygame.image.load('yellow_left_1.png')
yellow_left_1        = pygame.transform.scale(yellow_left_1, (45, 45))
yellow_left_2        = pygame.image.load('yellow_left_2.png')
yellow_left_2        = pygame.transform.scale(yellow_left_2, (45, 45))

img_tp_1             = pygame.image.load('teleport1.png')
img_tp_1             = pygame.transform.scale(img_tp_1, (50, 50))
img_tp_2             = pygame.image.load('teleport2.png')
img_tp_2             = pygame.transform.scale(img_tp_2, (50, 50))
img_tp_3             = pygame.image.load('teleport3.png')
img_tp_3             = pygame.transform.scale(img_tp_3, (50, 50))
img_tp_4             = pygame.image.load('teleport4.png')
img_tp_4             = pygame.transform.scale(img_tp_4, (50, 50))
img_tp_5             = pygame.image.load('teleport5.png')
img_tp_5             = pygame.transform.scale(img_tp_5, (50, 50))
img_tp_6             = pygame.image.load('teleport6.png')
img_tp_6             = pygame.transform.scale(img_tp_6, (50, 50))

images_tp            = [img_tp_1, img_tp_2, img_tp_3, img_tp_4, img_tp_5, img_tp_6, img_tp_1, img_tp_2, img_tp_3, img_tp_4, img_tp_5, img_tp_6]

walkRight_b          = [blue_right_1, blue_right_2] 
walkLeft_b           = [blue_left_1, blue_left_2]
walkRight_r          = [red_right_1, red_right_2] 
walkLeft_r           = [red_left_1, red_left_2]
walkRight_g          = [green_right_1, green_right_2]
walkLeft_g           = [green_left_1, green_left_2]
walkRight_y          = [yellow_right_1, yellow_right_2]
walkLeft_y           = [yellow_left_1, yellow_left_2]
array_tp             = [(a+200, b), (a+150, b-50), (a+300, b-50), (a+150, b-250), (a, b-100), (a+250, b-150), (a, b-200), (a+200 ,b-450), (a+400, b-300), (a+50, b-350)]
array_tp_True        = [False, False, False, False]
text_speak           = ['speak', 0]

class Voice():
	def __init__(self, src):
		self.counter = 0
		self.src     = src
		# self.sound   = pygame.mixer.music.load(self.src)
		self.sound   = pygame.mixer.Sound(self.src)
		self.volume  = 1

	def play_sound(self, number):
		self.counter = self.counter + 1
		# self.sound.play(number)
		self.sound.play(number)

	def puase(self):
		self.counter = self.counter - 1
		self.sound.stop()

	def unpause(self, number):
		self.counter = self.counter + 1
		self.sound.play(number)

	def change_volume(self, number):
		self.volume  = number
		self.sound.set_volume(self.volume)

voice_main           = Voice("main game muzki.wav")
voice_tas            = Voice("DiceRoll.wav")
voice_hit            = Voice("hit.wav")
voice_tp             = Voice("teleport.wav")
voice_question       = Voice("question.wav")
voice_True           = Voice("answer_true.wav")
voice_False          = Voice("answer_false.wav")
voice_button         = Voice("button.wav")
voice_victory        = Voice("button.wav")

class button(object):
	def __init__(self, screen, x, y, width, height, text_color, background_color, text, font):
		self.font             = font
		self.screen           = screen
		self.rect             = pygame.Rect(x,y,width,height)
		self.x                = x
		self.y                = y
		self.width            = width
		self.height           = height
		self.text             = text
		self.text_color       = text_color
		self.background_color = background_color
		self.angle            = 0

	def check(self):
		return self.rect.collidepoint(pygame.mouse.get_pos())

	def draw(self):
		pygame.draw.rect(self.screen, self.background_color,(self.rect),0)
		textobj  = self.font.render(self.text, True, self.text_color)
		textrect = textobj.get_rect(center=(self.x+self.width/2, self.y+self.height/2))
		self.screen.blit(textobj,textrect)
		pygame.draw.rect(self.screen, self.text_color, self.rect,3)

	def delete(self):
		del self

def speak(text):
	if text == 'speak':
		screen.blit(img_speak, (10, 20))
	elif text == 'dontspeak':
		screen.blit(img_dontspeak, (10, 20))

def menu() :
	# pygame.mixer.music.play()
	voice_main.change_volume(1)
	if voice_main.counter == 0 and text_speak[0] == 'speak':
		voice_main.play_sound(-1)
	a = 1
	pygame.display.flip()
	while True :
		screen.blit(bg , (0,0))
		speak(text_speak[0])
		screen.blit(img_exit, (((w-165)/2), (h/2)+100))
		screen.blit(img_start, (((w-165)/2), (h/2)-200))
		screen.blit(img_rolls, (((w-165)/2), (h/2)-100))
		screen.blit(img_about_us, (((w-165)/2), (h/2)))


		pygame.display.flip()
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				x,y = event.pos
				if x >= ((w-165)/2) and x <= ((w-165)/2)+165 and y >= (h/2)+100 and y <= (h/2)+186:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					pygame.quit()
					quit()

				elif x >= ((w-165)/2)  and x <= ((w-165)/2)+165  and y >= (h/2)-100 and y <= (h/2)-15:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					rolls()

				elif x >= ((w-165)/2) and x <= ((w-165)/2)+165 and y >= (h/2) and y <= (h/2)+85:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					Credit()

				elif x>10 and x<62 and y>20 and y<72 :
					if text_speak[0] == 'speak':
						# pygame.mixer.music.pause()
						voice_main.puase()
						text_speak[0] = 'dontspeak'
					elif text_speak[0] == 'dontspeak':
						# pygame.mixer.music.unpause()
						voice_main.unpause(-1)
						text_speak[0] = 'speak'

				elif x >= ((w-165)/2) and x <= ((w-165)/2)+165 and y >= (h/2)-200 and y <= (h/2)-115:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					start_game()

			# if event.type == pygame.MOUSEBUTTONDOWN :
			# 	x,y = event.pos
			# 	if x >= ((w-165)/2)-82  and x <= ((w-165)/2)+82  and y >= (h/2)-100 and y <= (h/2)-15:
			# 		if text_speak[0] == 'speak':
			# 			voice_button.play_sound(0)
			# 		Credit()

			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	x, y = event.pos
			# 	if x >= ((w-165)/2)-82 and x <= ((w-165)/2)+82 and y >= (h/2) and y <= (h/2)+85:
			# 		if text_speak[0] == 'speak':
			# 			voice_button.play_sound(0)
			# 		rolls()

			# if event.type == pygame.MOUSEBUTTONDOWN :
			# 	x,y = event.pos 
			# 	if x>10 and x<62 and y>20 and y<72 :
			# 		if text_speak[0] == 'speak':
			# 			# pygame.mixer.music.pause()
			# 			voice_main.puase()
			# 			text_speak[0] = 'dontspeak'
			# 		elif text_speak[0] == 'dontspeak':
			# 			# pygame.mixer.music.unpause()
			# 			voice_main.unpause(-1)
			# 			text_speak[0] = 'speak'
			# if event.type == pygame.MOUSEBUTTONDOWN :
			# 	x, y = event.pos
			# 	if x >= (w/2)-100 and x <= (w/2)+200 and y >= (h/2)-200 and y <= (h/2):
			# 		if text_speak[0] == 'speak':
			# 			voice_button.play_sound(0)
			# 		start_game()
	pygame.display.update()

def rolls():
	screen.blit(bg, (0, 0))
	screen.blit(rolls_pic, (50, 90))
	pygame.display.flip()
	while True:
		screen.blit(img_return, (int((w-165)/2), h-110))
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				if x >= int((w-165)/2) and x <= int((w-165)/2)+165 and y >= h-110 and y <= h-23:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					menu()
		pygame.display.update()

def Credit():
	# back_button =  button(screen, (w/2)-100, 650, 200, 75, (67, 181, 18), (40, 40, 40), "Back", font_1)
	screen.blit(bg, (0, 0))
	screen.blit(credit_pic,(120, 90))
	pygame.display.flip()
	credit = True 
	while credit :
		screen.blit(img_return, (int((w-165)/2), h-110))
		# back_button.draw()
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE :
					Quit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				x,y = event.pos 
				if x >= int((w-165)/2) and x <= int((w-165)/2)+165 and y >= h-110 and y <= h-23:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					menu()
		pygame.display.update()	

def start_game():
	screen.blit(bg , (0, 0))
	pygame.display.flip()
	while True:
		# screen.blit(img_1p, ((w/2)-85 , 100))
		screen.blit(bg, (0, 0))
		speak(text_speak[0])
		screen.blit(img_2p, ((w-200)/2 , (h/2)-100))
		screen.blit(img_3p, ((w-200)/2 , h/2))
		screen.blit(img_4p, ((w-200)/2 , (h/2)+100))
		screen.blit(img_return, ((w-165)/2 , h-150))


		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE :
					Quit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				i, j = event.pos
				if i>=(w-200)/2 and i<=(w-200)/2+200 and j>=(h/2)-100 and j<=(h/2)-50:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					game(2, a-50, b, a-50, b, a-50, b, a-50, b, 0, 0, 0, 0, 0, True, 0, False, False, False, False, True, array_pos)
				elif i>=(w-200)/2 and i<=(w-200)/2+200 and j>=(h/2) and j<= (h/2)+50:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					game(3, a-50, b, a-50, b, a-50, b, a-50, b, 0, 0, 0, 0, 0, True, 0, False, False, False, False, True, array_pos)
				elif i>=(w-200)/2 and i<=(w-200)/2+200 and j>=(h/2)+100 and j<=(h/2)+150:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					game(4, a-50, b, a-50, b, a-50, b, a-50, b, 0, 0, 0, 0, 0, True, 0, False, False, False, False, True, array_pos)
				# elif i>=(w/2)-85 and i<=(w/2)+85 and j>=400 and j<=446:
				# 	game(4, a-50, b, a-50, b, a-50, b, a-50, b, 0, 0, 0, 0, 0, True, 0, False, False, False, False, True, array_pos)
				elif i>= ((w-165)/2) and i<= ((w-165)/2)+165 and j>=h-150 and j<=h-65:
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					menu()
				elif i>10 and i<62 and j>20 and j<72 :
					if text_speak[0] == 'speak':
						# pygame.mixer.music.pause()
						voice_main.puase()
						text_speak[0] = 'dontspeak'
					elif text_speak[0] == 'dontspeak':
						# pygame.mixer.music.unpause()
						voice_main.unpause(-1)
						text_speak[0] = 'speak'
		pygame.display.update()

def created():
	txt = ''
	img = pygame.image.load('bg.jpg')
	screen.blit(img, (0, 0))
	pygame.display.flip()
	back_button = button(screen, w-250, h-100, 200, 50, (255, 0, 0), (255, 255, 255), "BACK", font_1)
	while True:
		back_button.draw()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.check():
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					# print('hoy')
					txt = 'back'
					break
	if txt == 'back':
		menu()
	pygame.display.update()

def main():
	screen.fill((255, 255, 0))
	pos = 'menu'
	while True:
		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN and pos == "menu":
				print('yes')
				if quit_button.check():
					pygame.quit();
					quit()
		pygame.display.update()

def move_goti(x, y, a, b, img, number):
	array_left  = [b, b+100, b+200, b+300, b+400]
	array_right = [b+50, b+150, b+250, b+350, b+450]
	if y in array_right:
		if x == a+450:
			screen.blit(img, (x, y+50))
			move_goti(x, y+50, a, b, img, number-1)
		else:
			screen.blit(img, (x, y+50))
			move_goti(x+50, y, a, b, img, number-1)

def rollTheDice() :
	a, b = (w-500)/2-200, (h-500)/2+450
	for i in range(1, 75):
		randomDiceSide = random.randint(0, 5)
		screen.blit(diceSides[randomDiceSide] , (a, b-100)) 
		pygame.time.delay(20)
		pygame.display.update()	 #animation e charkhidane tass
	finalSide = randomDiceSide + 1
	diceSides[6] = randomDiceSide
	return finalSide

def do_dice():
	run =True
	notRolled = True
	while run :
		clock.tick(30)	 #fps e bazi (ziad bodanesh mohem nis ta felan hamninjori gozashtam ke yadam bashe)
		if notRolled == True :	#bara avlin bar ke tas narikhte
			screen.blit(mainDice,(0,0))
			notRolled = False
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN :
				x, y = event.pos
				if mainDice.get_rect().collidepoint(x,y) :
					pygame.mixer.music.play()
					rollTheDice()
					pygame.time.delay(150)
		break

		pygame.display.update()	

def taple(taple_1, taple_2):
	array_right   = [b, b-100, b-200, b-300, b-400]
	array_left    = [b-50, b-150, b-250, b-350, b-450]
	if taple_1[1] < taple_2[1]:
		return True
	elif taple_1[1] == taple_2[1]:
		if taple_1[1] in array_right:
			if taple_1[0] > taple_2[0]:
				return True
			else:
				return False
		elif taple_1[1] in array_left:
			if taple_1[0] < taple_2[0]:
				return True
			else:
				return False

	else:
		return False

def tartib(array, number):
	array_right   = [b, b-100, b-200, b-300, b-400]
	array_left    = [b-50, b-150, b-250, b-350, b-450]
	array_a       = [a, a+50, a+100, a+150, a+200, a+250, a+300, a+350, a+400, a+450]
	arr           = [[], []]
	for i in range(len(array)):
		if array[i][0] in array_a:
			if i != number:
				if taple(array[i], array[number]):
					if len(arr[0]) == 0:
						arr[0].append(i)
					elif len(arr[0]) == 1:
						if taple(array[arr[0][0]], array[i]):
							arr[0].append(i)
						else:
							arr[0].append(arr[0][0])
							arr[0][0] = i
					elif len(arr[0]) == 2:
						if taple(array[arr[0][1]], array[i]):
							arr[0].append(i)
						else:
							arr[0].append(arr[0][1])
							arr[0][1] = i

						if taple(array[arr[0][1]], array[arr[0][0]]):
							normal    = arr[0][0]
							arr[0][0] = arr[0][1]
							arr[0][1] = normal
				else:
					if len(arr[1]) == 0:
						arr[1].append(i)
					elif len(arr[1]) == 1:
						if taple(array[arr[1][0]], array[i]):
							arr[1].append(arr[1][0])
							arr[1][0] = i
						else:
							arr[1].append(i)
					elif len(arr[1]) == 2:
						if taple(array[arr[1][1]], array[i]):
							arr[1].append(arr[1][1])
							arr[1][1] = i
						else:
							arr[1].append(i)

						if taple(array[arr[1][0]], array[arr[1][1]]):
							normal    = arr[1][0]
							arr[1][0] = arr[1][1]
							arr[1][1] = normal
	return arr

def rolle(number, n):
	array_right   = [b, b-100, b-200, b-300, b-400]
	array_left    = [b-50, b-150, b-250, b-350, b-450]
	arr   = []
	e     = []
	array = tartib(array_pos, number)
	if n == 1:
		if array_pos[number] == (a+50, b-450):
			arr.append(0)
			arr.append(e)
			print(arr)
			return arr

		if len(array[0]) == 1:
			e.append(array[0][0])
			arr.append(1)
		elif len(array[0]) >= 2:
			e.append(array[0][0])
			arr.append(1)
			e.append(array[0][len(array[0])-1])
			arr.append(2)

		if (array_pos[number][1] in array_right and array_pos[number][0] <= a+250) or (array_pos[number][1] in array_left and array_pos[number][0] >= a+250):
			arr.append(3)
		arr.append(4)
		arr.append(e)
		print(arr)
		return arr

	elif n == 2:
		if array_pos[number] == (a+100, b):
			arr.append(0)
			arr.append(e)
			print(arr)
			return arr

		if len(array[1]) == 1:
			e.append(array[1][0])
			arr.append(1)
		elif len(array[1]) >= 2:
			e.append(array[1][0])
			arr.append(1)
			e.append(array[1][len(array[1])-1])
			arr.append(2)

		if (array_pos[number][1] in array_right and array_pos[number][0] <= a+250) or (array_pos[number][1] in array_left and array_pos[number][0] >= a+250):
			arr.append(3)
		arr.append(4)
		arr.append(e)
		print(arr)
		return arr

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

class Ask():
	def __init__(self):
		# self.t      = ''
		# self.answer = 0
		self.number_ask     = ['0.5', '1', '2', '3', '4', '5', '6', '4', '6']
		self.function_ask   = ['*', '/', '+', '-']
		self.num_ask        = [0.5, 1, 2, 3, 4, 5, 6, 4, 6]

		
	def run(self):
		self.t      = ''
		self.answer = 0
		i      = random.randint(1, 2)
		int_1  = random.randint(0, 8)
		int_2  = random.randint(0, 8)
		int_3  = random.randint(0, 8)
		func_1 = random.randint(0, 3)
		func_2 = random.randint(0, 3)
		x      = self.num_ask[int_1]
		y      = self.num_ask[int_2]
		z      = self.num_ask[int_3]
		# answer = 0
		# x = random.randint(0, 9)
		# y = random.randint(0, 5)
		if i == 1:
			# print('1111111111111111111')
			self.t = self.number_ask[int_1] + self.function_ask[func_1] + self.number_ask[int_2]
			# print(self.t)
			if self.function_ask[func_1] == '*':
				self.answer = x * y
			elif self.function_ask[func_1] == '/':
				self.answer = x / y
			elif self.function_ask[func_1] == '+':
				self.answer = x + y
			elif self.function_ask[func_1] == '-':
				self.answer = x - y
			# print(self.answer)
		elif i == 2:
			# print('222222222222222')
			self.t = self.number_ask[int_1] + self.function_ask[func_1] + self.number_ask[int_2] + self.function_ask[func_2] + self.number_ask[int_3]
			# print(self.t)
			if self.function_ask[func_1] == '-':
				if self.function_ask[func_2] == '-':
					self.answer = x - y - z
				elif self.function_ask[func_2] == '+':
					self.answer = x - y + z
				elif self.function_ask[func_2] == '*':
					self.answer = x - y * z
				elif self.function_ask[func_2] == '/':
					self.answer =  x - y / z
			elif self.function_ask[func_1] == '+':
				if self.function_ask[func_2] == '-':
					self.answer = x + y - z
				elif self.function_ask[func_2] == '+':
					self.answer = x + y + z
				elif self.function_ask[func_2] == '*':
					self.answer = x + y * z
				elif self.function_ask[func_2] == '/':
					self.answer = x + y / z
			elif self.function_ask[func_1] == '/':
				if self.function_ask[func_2] == '-':
					self.answer = x / y - z
				elif self.function_ask[func_2] == '+':
					self.answer = x / y + z
				elif self.function_ask[func_2] == '*':
					self.answer = x / y * z
				elif self.function_ask[func_2] == '/':
					self.answer = x / y / z
			elif self.function_ask[func_1] == '*':
				if self.function_ask[func_2] == '-':
					self.answer = x * y - z
				elif self.function_ask[func_2] == '+':
					self.answer = x * y + z
				elif self.function_ask[func_2] == '*':
					self.answer = x * y * z
				elif self.function_ask[func_2] == '/':
					self.answer = x * y / z
	
def asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, color_name):
	if text_speak[0] == 'speak':
		voice_question.play_sound(0)
	voice_main.change_volume(0.0)
	# 	voice_quesion.play_sound(0)
	array_right   = [b, b-100, b-200, b-300, b-400]
	array_left    = [b-50, b-150, b-250, b-350, b-450]
	ask     = Ask()
	ask.run()
	t       = ask.t
	answer  = ask.answer
	numberr = random.randint(3, 6)
	# if numberr == 3:
	# 	numberrr = ' 3 khane be jelo beraid ...'
	# elif numberr == 4:
	# 	numberrr = ' 4 khane be jelo beraid ...'
	# elif numberr == 5:
	# 	numberrr = ' 5 khane be jelo beraid ...'
	# elif numberr == 6:
	# 	numberrr = ' 6 khane be jelo beraid ...'
	if '.' in str(answer):
		answer = truncate(answer, 2)
	array   = [(w/2)-250, (w/2)-130, (w/2)-10, (w/2)+110]
	arr     = []
	n       = 3
	text    = ''
	while len(arr) != 4:
		e = random.randint(0, n)
		arr.append(array[e])
		array = array[:e] + array[e+1:]
		n = n - 1
	screen.blit(bg, (0, 0))
	pygame.display.flip()
	# time.sleep(1)
	i      = random.randint(0, 2)
	if i == 0 or answer == 0:
		answer_1 = answer-1
		if '.' in str(answer_1):
			answer_1 = truncate(answer_1, 2)
		answer_2 = answer+1
		if '.' in str(answer_2):
			answer_2 = truncate(answer_2, 2)
		answer_3 = answer+2
		if '.' in str(answer_3):
			answer_3 = truncate(answer_3, 2)
	elif i == 1:
		answer_1 = answer/2
		if '.' in str(answer_1):
			answer_1 = truncate(answer_1, 2)
		answer_2 = answer*2
		if '.' in str(answer_2):
			answer_2 = truncate(answer_2, 2)
		answer_3 = answer*3
		if '.' in str(answer_3):
			answer_3 = truncate(answer_3, 2)
	elif i == 2:
		answer_1 = answer-0.5
		if '.' in str(answer_1):
			answer_1 = truncate(answer_1, 2)
		answer_2 = answer-2
		if '.' in str(answer_2):
			answer_2 = truncate(answer_2, 2)
		answer_3 = answer+0.5
		if '.' in str(answer_3):
			answer_3 = truncate(answer_3, 2)
			
	show_text = button(screen, (w/2)-250, (h/2)-50, 500, 100, (255, 255, 255), (255, 0, 0), t, font_1)
	test_1    = button(screen, arr[0], (h/2)+75, 100, 50, (255, 255, 255), (255, 100, 0), str(answer), font_1)
	test_2    = button(screen, arr[1], (h/2)+75, 100, 50, (255, 255, 255), (255, 100, 0), str(answer_1), font_1)
	test_3    = button(screen, arr[2], (h/2)+75, 100, 50, (255, 255, 255), (255, 100, 0), str(answer_2), font_1)
	test_4    = button(screen, arr[3], (h/2)+75, 100, 50, (255, 255, 255), (255, 100, 0), str(answer_3), font_1)
	timer_but = button(screen, (w/2)+350, (h/2)-50, 50, 50, (0, 0, 0), (255, 100, 0), str(5), font_1)
	timer     = 0
	timee     = time.localtime()[5]
	timerr    = 1
	while True:
		if text != '':
			break
		show_text.draw()
		test_1.draw()
		test_2.draw()
		test_3.draw()
		test_4.draw()
		timer_but.draw()
		now = time.localtime()[5]
		if now > timee:
			timer_but.delete()
			timerr    = now-timee
			timer_but = button(screen, (w/2)+350, (h/2)-50, 50, 50, (0, 0, 0), (255, 100, 0), str(6-timerr if (timerr<6) else 0), font_1)
			timer_but.draw()
		elif now < timee:
			timer_but.delete()
			timerr    = 60+now-timee
			timer_but = button(screen, (w/2)+350, (h/2)-50, 50, 50, (0, 0, 0), (255, 100, 0), str(6-timerr if (timerr<6) else 0), font_1)
			timer_but.draw()
		if timerr >= 6:
			text = 'timerr'
			break

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if test_1.check():
					text = 'test_1'
					break

				elif test_2.check() or test_3.check() or test_4.check():
					text = 'other'
					break
		pygame.display.update()
	# voice_quesion.puase()
	dic_color = {'blue':0, 'red':1, 'green':2, 'yellow':3}
	if text == 'timerr' or text == 'other':
		if text_speak[0] == 'speak':
			voice_False.play_sound(0)
		# if numberr == 3:
		# 	numberrr = ' 3 khane be agab beraid ...'
		# elif numberr == 4:
		# 	numberrr = ' 4 khane be agab beraid ...'
		# elif numberr == 5:
		# 	numberrr = ' 5 khane be agab beraid ...'
		# elif numberr == 6:
		# 	numberrr = ' 6 khane be agab beraid ...'
		arr     = rolle(dic_color[color_name], 2)
		arr_num = arr[random.randint(0, len(arr)-2)]
		if arr_num == 0:
			image_load = img_back2
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' 2 khane be agab beravid ...', font_1)
		elif arr_num == 1:
			image_load = img_pos2last
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' jaye khod ra ba nafare akhar avaz konid ...', font_1)
		elif arr_num == 2:
			image_load = img_pos2previus
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' jaye khod ra ba nafare gabli avaz konid ...', font_1)
		elif arr_num == 3:
			image_load = img_strtRaw
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' be abteda radifi ke dar an garar darid beravid ...', font_1)
		elif arr_num == 4:
			if numberr == 3:
				image_load = img_back3
			elif numberr == 4:
				image_load = img_back4
			elif numberr == 5:
				image_load = img_back5
			elif numberr == 6:
				image_load = img_back6
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), numberrr, font_1)
	if text == 'test_1':
		if text_speak[0] == 'speak':
			voice_True.play_sound(0)
		# if numberr == 3:
		# 	numberrr = ' 3 khane be jelo beraid ...'
		# elif numberr == 4:
		# 	numberrr = ' 4 khane be jelo beraid ...'
		# elif numberr == 5:
		# 	numberrr = ' 5 khane be jelo beraid ...'
		# elif numberr == 6:
		# 	numberrr = ' 6 khane be jelo beraid ...'
		arr     = rolle(dic_color[color_name], 1)
		arr_num = arr[random.randint(0, len(arr)-2)]
		if arr_num == 0:
			image_load = img_forward1
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' 1 khane be jelo beravid ...', font_1)
		elif arr_num == 1:
			image_load = img_pos2first
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' jaye khod ra ba nafare aval avaz konid ...', font_1)
		elif arr_num == 2:
			image_load = img_pos2next
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' jaye khod ra ba nafare badi avaz konid ...', font_1)
		elif arr_num == 3:
			image_load = img_endRaw
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), ' be entehaie radifi ke dar an garar darid beravid ...', font_1)
		elif arr_num == 4:
			if numberr == 3:
				image_load = img_forward3
			elif numberr == 4:
				image_load = img_forward4
			elif numberr == 5:
				image_load = img_forward5
			elif numberr == 6:
				image_load = img_forward6
			# cart_but = button(screen, (w/2)-300, (h/2)+200, 600, 100, (255, 255, 255), (255, 0, 0), numberrr, font_1)

	timer     = 0
	timee     = time.localtime()[5]
	timerr    = 1
	screen.blit(bg, (0, 0))
	screen.blit(image_load, (((w-600)/2), h/2+150))
	pygame.display.flip()
	tt        = True
	while True:
		# cart_but.draw()
		if text == 'timerr' or text == 'other':
			screen.blit(img_False, (int((w-320)/2), int((h-360)/2)))
		elif text == 'test_1':
			screen.blit(img_True, (int((w-320)/2), int((h-360)/2)))
		now = time.localtime()[5]
		if now > timee:
			timerr    = now-timee
		elif now < timee:
			timerr    = 60+now-timee
		if timerr >= 3 and tt:
			# voice_quesion.pause()
			if text_speak[0] == 'speak':
				voice_question.puase()
			voice_main.change_volume(0.5)
			tt = False
			if text == 'timerr' or text == 'other':
				voice_False.puase()
				if arr_num == 0:
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu-2, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red-2, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green-2, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow-2, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
				elif arr_num == 1 or arr_num == 2:
					if arr_num == 1:
						n = arr[len(arr)-1][0]
					elif arr_num == 2:
						n = arr[len(arr)-1][1]
					if color_name == 'blue':
						print('blue')
						if n == 1:
							print('yes')
							game(num, x_r, y_r, x_b, y_b, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 2:
							print('yes')
							game(num, x_g, y_g, x_r, y_r, x_b, y_b, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_y, y_y, x_r, y_r, x_g, y_g, x_b, y_b, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('red')
						if n == 0:
							print('yes')
							game(num, x_r, y_r, x_b, y_b, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 2:
							print('yes')
							game(num, x_b, y_b, x_g, y_g, x_r, y_r, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_b, y_b, x_y, y_y, x_g, y_g, x_r, y_r, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('green')
						if n == 0:
							print('yes')
							game(num, x_g, y_g, x_r, y_r, x_b, y_b, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 1:
							print('yes')
							game(num, x_b, y_b, x_g, y_g, x_r, y_r, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_b, y_b, x_r, y_r, x_y, y_y, x_g, y_g, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yellow')
						if n == 0:
							print('yes')
							game(num, x_y, y_y, x_r, y_r, x_g, y_g, x_b, y_b, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						if n == 1:
							print('yes')
							game(num, x_b, y_b, x_y, y_y, x_g, y_g, x_r, y_r, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						if n == 2:
							print('yes')
							game(num, x_b, y_b, x_r, y_r, x_y, y_y, x_g, y_g, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)

				elif arr_num == 3:
					color = dic_color[color_name]
					if array_pos[color][1] in array_right:
						number_padash = int(int(array_pos[color][0]-a)/50)
					elif array_pos[color][1] in array_left:
						number_padash = int(int(a+450-array_pos[color][0])/50)
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu-number_padash, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red-number_padash, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green-number_padash, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow-number_padash, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)

				elif arr_num == 4:
					print(int(-numberr))
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, int(-numberr), number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, int(-numberr), number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, int(-numberr), number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, int(-numberr), number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)




			elif text == 'test_1':
				voice_True.puase()
				if arr_num == 0:
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu+1, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red+1, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green+1, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow+1, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
				
				elif arr_num == 1 or arr_num == 2:
					if arr_num == 1:
						n = arr[len(arr)-1][0]
					elif arr_num == 2:
						n = arr[len(arr)-1][1]
					if color_name == 'blue':
						if n == 1:
							print('yes')
							game(num, x_r, y_r, x_b, y_b, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 2:
							print('yes')
							game(num, x_g, y_g, x_r, y_r, x_b, y_b, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_y, y_y, x_r, y_r, x_g, y_g, x_b, y_b, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						if n == 0:
							print('yes')
							game(num, x_r, y_r, x_b, y_b, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 2:
							print('yes')
							game(num, x_b, y_b, x_g, y_g, x_r, y_r, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_b, y_b, x_y, y_y, x_g, y_g, x_r, y_r, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						if n == 0:
							print('yes')
							game(num, x_g, y_g, x_r, y_r, x_b, y_b, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 1:
							print('yes')
							game(num, x_b, y_b, x_g, y_g, x_r, y_r, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						elif n == 3:
							print('yes')
							game(num, x_b, y_b, x_r, y_r, x_y, y_y, x_g, y_g, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						if n == 0:
							print('yes')
							game(num, x_y, y_y, x_r, y_r, x_g, y_g, x_b, y_b, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						if n == 1:
							print('yes')
							game(num, x_b, y_b, x_y, y_y, x_g, y_g, x_r, y_r, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
						if n == 2:
							print('yes')
							game(num, x_b, y_b, x_r, y_r, x_y, y_y, x_g, y_g, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)

				elif arr_num == 3:
					color = dic_color[color_name]
					if array_pos[color][1] in array_right:
						number_padash = int(int(a+450-array_pos[color][0])/50)
					elif array_pos[color][1] in array_left:
						number_padash = int(int(array_pos[color][0]-a)/50)
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu+number_padash, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red+number_padash, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green+number_padash, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow+number_padash, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)

				elif arr_num == 4:
					if color_name == 'blue':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu+numberr, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'red':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red+numberr, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'green':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green+numberr, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
					elif color_name == 'yellow':
						print('yes')
						game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow+numberr, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, False, array_pos)
		pygame.display.update()

class player( ) :
    def __init__(self,x , y , width , height, screen):
        self.x         = x 
        self.y         = y 
        self.width     = width
        self.height    = height
        self.vel       = 5
        self.left      = False
        self.right     = False
        self.walkCount = 0
        self.standing  = True
        self.screen    = screen
    
    def draw(self) :
        if self.walkCount + 1 >= 27  :
            self.walkCount = 0
        if not(self.standing) :
            if self.left :
                self.screen.blit(walkLeft_b[self.walkCount // 3] , (self.x  , self.y))
                self.walkCount += 1
            elif self.right :
                self.screen.blit(walkRight_b[self.walkCount // 3] , (self.x , self.y ))
                self.walkCount += 1
        else :
            if self.right :
                self.screen.blit(walkRight_b[0] , (self.x ,self.y))
            else :
                self.screen.blit(walkLeft_b[0] , (self.x , self.y))

def animation(x, y, number, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, text):
	if text == 'blue':
		n = 0
	elif text == 'red':
		n = 1
	elif text == 'green':
		n = 2
	elif text == 'yellow':
		n = 3
	if x < a:
		x = a
		number = number - 1

	array_right   = [b, b-100, b-200, b-300, b-400]
	array_left    = [b-50, b-150, b-250, b-350, b-450]
	wc = 0
	while number >= 1:
		if y in array_right:
			if x == a+450:
				screen.blit(img_map, (a, b-450))
				y = y-50
				if n == 0:
					screen.blit(walkLeft_b[0], (x, y))
				elif n == 1:
					screen.blit(walkLeft_r[0], (x, y))
				elif n == 2:
					screen.blit(walkLeft_g[0], (x, y))
				elif n == 3:
					screen.blit(walkLeft_y[0], (x, y))
				if wc + 1 > 4:
					wc = 0
				for i in range(num):
					if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 2], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
					elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 2], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
					elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 2], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
					elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 2], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
				number = number - 1
				wc = wc + 1
			else:
				fasele = int((a+450 - x)/50)
				if fasele >= number:
					f = number*10
				elif fasele <= number:
					f = fasele*10
				# f      = int((a+450 - x_b)/5)
				walkCount = 0
				for i in range(f):
					screen.blit(img_map, (a, b-450))
					if wc + 1 > 4:
						wc = 0
					for i in range(num):
						if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
							if y_b in array_right:
								screen.blit(walkRight_b[wc // 2], (x_b, y_b))
							elif y_b in array_left:
								screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
						elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
							if y_r in array_right:
								screen.blit(walkRight_r[wc // 2], (x_r, y_r))
							elif y_r in array_left:
								screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
						elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
							if y_g in array_right:
								screen.blit(walkRight_g[wc // 2], (x_g, y_g))
							elif y_g in array_left:
								screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
						elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
							if y_y in array_right:
								screen.blit(walkRight_y[wc // 2], (x_y, y_y))
							elif y_y in array_left:
								screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
					if walkCount + 1 > 4:
						walkCount = 0
					x = x + 5
					if n == 0:
						screen.blit(walkRight_b[walkCount // 2], (x, y))
					elif n == 1:
						screen.blit(walkRight_r[walkCount // 2], (x, y))
					elif n == 2:
						screen.blit(walkRight_g[walkCount // 2], (x, y))
					elif n == 3:
						screen.blit(walkRight_y[walkCount // 2], (x, y))
					walkCount = walkCount + 1
					wc = wc + 1
					pygame.display.update()
					pygame.time.delay(50)
					if x + 5 > a+450:
						break
				number = number - fasele
				if number <= -1:
					number = 0
		elif y in array_left:
			if x == a:
				screen.blit(img_map, (a, b-450))
				if wc + 1 > 4:
					wc = 0
				y = y-50
				if n == 0:
					screen.blit(walkRight_b[0], (x, y))
				elif n == 1:
					screen.blit(walkRight_r[0], (x, y))
				elif n == 2:
					screen.blit(walkRight_g[0], (x, y))
				elif n == 3:
					screen.blit(walkRight_y[0], (x, y))
				for i in range(num):
					if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 2], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
					elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 2], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
					elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 2], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
					elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 2], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
				number = number - 1
				wc = wc + 1
			else:
				fasele = int((x - a)/50)
				if fasele >= number:
					f = number*10
				elif fasele < number:
					f = fasele*10
				walkCount = 0
				for i in range(f):
					screen.blit(img_map, (a, b-450))
					if wc + 1 > 4:
						wc = 0
					for i in range(num):
						if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
							if y_b in array_right:
								screen.blit(walkRight_b[wc // 2], (x_b, y_b))
							elif y_b in array_left:
								screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
						elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
							if y_r in array_right:
								screen.blit(walkRight_r[wc // 2], (x_r, y_r))
							elif y_r in array_left:
								screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
						elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
							if y_g in array_right:
								screen.blit(walkRight_g[wc // 2], (x_g, y_g))
							elif y_g in array_left:
								screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
						elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
							if y_y in array_right:
								screen.blit(walkRight_y[wc // 2], (x_y, y_y))
							elif y_y in array_left:
								screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
					if walkCount + 1 > 4:
						walkCount = 0
					wc = wc + 1
					x = x - 5
					if n == 0:
						screen.blit(walkLeft_b[walkCount // 2], (x, y))
					elif n == 1:
						screen.blit(walkLeft_r[walkCount // 2], (x, y))
					elif n == 2:
						screen.blit(walkLeft_g[walkCount // 2], (x, y))
					elif n == 3:
						screen.blit(walkLeft_y[walkCount // 2], (x, y))
					walkCount = walkCount + 1
					pygame.display.update()
					pygame.time.delay(50)
					if x - 5 < a:
						break
				number = number - fasele
				if number <= -1:
					number = 0
	while number <= -1:
		if y in array_right:
			if x == a:
				screen.blit(img_map, (a, b-450))
				if wc + 1 > 4:
					wc = 0
				for i in range(num):
					if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 2], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
					elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 2], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
					elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 2], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
					elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 2], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
				y = y+50
				wc = wc + 1
				if n == 0:
					screen.blit(walkRight_b[0], (x, y))
				elif n == 1:
					screen.blit(walkRight_r[0], (x, y))
				elif n == 2:
					screen.blit(walkRight_g[0], (x, y))
				elif n == 3:
					screen.blit(walkRight_y[0], (x, y))
				number = number + 1
			else:
				fasele = int((x - a)/50)
				if fasele >= number * -1:
					f = number * 10 * -1
				else:
					f = fasele * 10
				walkCount = 0
				for i in range(f):
					screen.blit(img_map, (a, b-450))
					if wc + 1 > 4:
						wc = 0
					for i in range(num):
						if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
							if y_b in array_right:
								screen.blit(walkRight_b[wc // 2], (x_b, y_b))
							elif y_b in array_left:
								screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
						elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
							if y_r in array_right:
								screen.blit(walkRight_r[wc // 2], (x_r, y_r))
							elif y_r in array_left:
								screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
						elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
							if y_g in array_right:
								screen.blit(walkRight_g[wc // 2], (x_g, y_g))
							elif y_g in array_left:
								screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
						elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
							if y_y in array_right:
								screen.blit(walkRight_y[wc // 2], (x_y, y_y))
							elif y_y in array_left:
								screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
					if walkCount + 1 > 4:
						walkCount = 0
					wc = wc + 1
					x = x - 5
					if n == 0:
						screen.blit(walkLeft_b[walkCount // 2], (x, y))
					elif n == 1:
						screen.blit(walkLeft_r[walkCount // 2], (x, y))
					elif n == 2:
						screen.blit(walkLeft_g[walkCount // 2], (x, y))
					elif n == 3:
						screen.blit(walkLeft_y[walkCount // 2], (x, y))
					walkCount = walkCount + 1
					pygame.display.update()
					pygame.time.delay(50)
					if x - 5 < a:
						break
				number = number + fasele
				if number >= 1:
					number = 0
		elif y in array_left:
			# print('y in left')
			if x == a+450:
				screen.blit(img_map, (a, b-450))
				if wc + 1 > 4:
					wc = 0
				for i in range(num):
					if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 2], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
					elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 2], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
					elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 2], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
					elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 2], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
				y = y+50
				if n == 0:
					screen.blit(walkLeft_b[0], (x, y))
				elif n == 1:
					screen.blit(walkLeft_r[0], (x, y))
				elif n == 2:
					screen.blit(walkLeft_g[0], (x, y))
				elif n == 3:
					screen.blit(walkLeft_y[0], (x, y))
				number = number + 1
				wc = wc + 1
			else:
				fasele = int((a+450 - x)/50)
				if fasele >= number:
					f = number*10
				elif fasele <= number:
					f = fasele*10
				# f      = int((a+450 - x_b)/5)
				# print(f)
				walkCount = 0
				for j in range(int(-f)):
					# print(x)
					screen.blit(img_map, (a, b-450))
					if wc + 1 > 4:
						wc = 0
					for i in range(num):
						if num-i == 1 and come_blue and (x_b != a-50) and text != 'blue':
							if y_b in array_right:
								screen.blit(walkRight_b[wc // 2], (x_b, y_b))
							elif y_b in array_left:
								screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
						elif num-i == 2 and come_red and (x_r != a-50) and text != 'red':
							if y_r in array_right:
								screen.blit(walkRight_r[wc // 2], (x_r, y_r))
							elif y_r in array_left:
								screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
						elif num-i == 3 and come_green  and (x_g != a-50) and text != 'green':
							if y_g in array_right:
								screen.blit(walkRight_g[wc // 2], (x_g, y_g))
							elif y_g in array_left:
								screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
						elif num-i == 4 and come_yellow and (x_y != a-50) and text != 'yellow':
							if y_y in array_right:
								screen.blit(walkRight_y[wc // 2], (x_y, y_y))
							elif y_y in array_left:
								screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
					if walkCount + 1 > 4:
						walkCount = 0
					wc = wc + 1
					x = x + 5
					if n == 0:
						screen.blit(walkRight_b[walkCount // 2], (x, y))
					elif n == 1:
						screen.blit(walkRight_r[walkCount // 2], (x, y))
					elif n == 2:
						screen.blit(walkRight_g[walkCount // 2], (x, y))
					elif n == 3:
						screen.blit(walkRight_y[walkCount // 2], (x, y))
					walkCount = walkCount + 1
					pygame.display.update()
					pygame.time.delay(50)
					# print(x)
					if x + 5 > a+450:
						break

				number = number + fasele
				if number >= 1:
					number = 0

	# print('nahayi',x)
	array_poss     = [x, y]
	return array_poss

def tp(x, y, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y):
	array_right    = [b, b-100, b-200, b-300, b-400]
	array_left     = [b-50, b-150, b-250, b-350, b-450]
	x_now = x
	y_now = y
	if x == x_b and y == y_b:
		text = 'blue'
	elif x == x_r and y == y_r:
		text = 'red'
	elif x == x_g and y == y_g:
		text = 'green'
	elif x == x_y and y == y_y:
		text = 'yellow'
	if (x, y) in array_tp:
		for i in range(len(array_tp)):
			if (x, y) == array_tp[i]:
				if i%2 == 0:
					(x, y) = array_tp[i+1]
					break
					# return (x, y)
				else:
					(x, y) = array_tp[i-1]
					break
					# return (x, y)
	if x_now != x or y_now != y:
		if text_speak[0] == 'speak':
			voice_tp.play_sound(0)
		# print('omad')
		walkCounter = 0
		for wc in range(60):
			screen.blit(img_map, (a, b-450))
			if walkCounter + 1 > 4:
				walkCounter = 0
			# time.sleep(0.02)
			if wc == 89:
				if text_speak[0] == 'speak':
					voice_tp.play_sound(0)
			if wc < 30:
				screen.blit(images_tp[wc // 5], (x_now, y_now))
			else:
				screen.blit(images_tp[(wc-30) // 5], (x, y))
			num = 4
			for i in range(num):
				if num-i == 1 and (x_b != a-50) and text != 'blue':
					if y_b in array_right:
						screen.blit(walkRight_b[walkCounter // 2], (x_b, y_b))
					elif y_b in array_left:
						screen.blit(walkLeft_b[walkCounter // 2], (x_b, y_b))
				elif num-i == 2 and (x_r != a-50) and text != 'red':
					if y_r in array_right:
						screen.blit(walkRight_r[walkCounter // 2], (x_r, y_r))
					elif y_r in array_left:
						screen.blit(walkLeft_r[walkCounter // 2], (x_r, y_r))
				elif num-i == 3 and (x_g != a-50) and text != 'green':
					if y_g in array_right:
						screen.blit(walkRight_g[walkCounter // 2], (x_g, y_g))
					elif y_g in array_left:
						screen.blit(walkLeft_g[walkCounter // 2], (x_g, y_g))
				elif num-i == 4 and (x_y != a-50) and text != 'yellow':
					if y_y in array_right:
						screen.blit(walkRight_y[walkCounter // 2], (x_y, y_y))
					elif y_y in array_left:
						screen.blit(walkLeft_y[walkCounter // 2], (x_y, y_y))
			walkCounter = walkCounter + 1
			pygame.display.update()
			pygame.time.delay(50)
	voice_tp.puase()
	return (x, y)

def hit(x, y, text, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, txt):
	if text_speak[0] == 'speak':
		voice_hit.play_sound(0)
	array_right    = [b, b-100, b-200, b-300, b-400]
	array_left     = [b-50, b-150, b-250, b-350, b-450]
	if y in array_right:
		wc = 0
		if text == 'blue':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_blue[wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'red':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_red[wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'green':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_green[wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'yellow':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_yellow[wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
	elif y in array_left:
		wc = 0
		if text == 'blue':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_blue[2 + wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'red':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_red[2 + wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'green':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_green[2 + wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
		elif text == 'yellow':
			for i in range(32):
				if wc >= 8:
					wc = 0
				# time.sleep(0.02)
				screen.blit(img_map, (a, b-450))
				for i in range(num):
					if num-i == 1 and text != 'blue' and txt != 'blue' and (x_b != a-50):
						if y_b in array_right:
							screen.blit(walkRight_b[wc // 4], (x_b, y_b))
						elif y_b in array_left:
							screen.blit(walkLeft_b[wc // 4], (x_b, y_b))
					elif num-i == 2 and text != 'red' and txt != 'red' and (x_r != a-50):
						if y_r in array_right:
							screen.blit(walkRight_r[wc // 4], (x_r, y_r))
						elif y_r in array_left:
							screen.blit(walkLeft_r[wc // 4], (x_r, y_r))
					elif num-i == 3 and text != 'green' and txt != 'green'  and (x_g != a-50):
						if y_g in array_right:
							screen.blit(walkRight_g[wc // 4], (x_g, y_g))
						elif y_g in array_left:
							screen.blit(walkLeft_g[wc // 4], (x_g, y_g))
					elif num-i == 4 and text != 'yellow' and txt != 'yellow' and (x_y != a-50):
						if y_y in array_right:
							screen.blit(walkRight_y[wc // 4], (x_y, y_y))
						elif y_y in array_left:
							screen.blit(walkLeft_y[wc // 4], (x_y, y_y))
				screen.blit(hit_yellow[2 + wc // 4], (x, y))
				wc = wc + 1
				pygame.time.delay(50)
				pygame.display.update()
	voice_hit.puase()

def game(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, ask, array_pos):
	# x_b, y_b      = x_bb, y_bb
	voice_main.change_volume(0.5)
	win            = False
	print('game started ...')
	# x_r, y_r      = x_rr, y_rr
	# x_g, y_g      = x_gg, y_gg
	# x_y, y_y      = x_yy, y_yy
	# number_belu   = 0
	# number_red    = 0
	# number_green  = 0
	# number_yellow = 0
	array_pos[0]   = (x_b, y_b)
	array_pos[1]   = (x_r, y_r)
	array_pos[2]   = (x_g, y_g)
	array_pos[3]   = (x_y, y_y)

	array_taple[0] = (x_b, y_b)
	array_taple[1] = (x_r, y_r)
	array_taple[2] = (x_g, y_g)
	array_taple[3] = (x_y, y_y)

	array_right    = [b, b-100, b-200, b-300, b-400]
	array_left     = [b-50, b-150, b-250, b-350, b-450]
	# player_blue   = player(x_b, y_b, 0, 0, screen)
	# player_red    = player(x_r, y_r, 0, 0, screen)
	# player_green  = player(x_g, y_g, 0, 0, screen)
	# player_yellow = (x_y, y_y, 0, 0, screen)
	walkCount      = 0
	right          = False
	left           = False
	vel            = 5
	tp_blue        = array_tp_True[0]
	tp_red         = array_tp_True[1]
	tp_green       = array_tp_True[2]
	tp_yellow      = array_tp_True[3]
	# taple_bluee   = taple_blue
	# taple_red     = taple_red
	# taple_greenn  = taple_green
	# taple_yelloww = taple_yellow
	# notRolled     = notRolledd
	# number        = numberr
	# color_num     = color_numm
	# come_blue     = come_bluee
	# come_red      = come_redd
	# come_green    = come_greenn
	# come_yellow   = come_yelloww
	# ask           = False

	screen.blit(bg, (0, 0))
	screen.blit(img_map, ((w-500)/2, (h-500)/2))
	if num == 4:
		for i in range(num):
			if i == 0:
				screen.blit(img_dota_blue, ((w-500)/2+60, (h-500)/2-80))
				screen.blit(blue_right_1, ((w-500)/2+60+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 1:
				screen.blit(img_dota_red, (((w-500)/2)+160, (h-500)/2-80))
				screen.blit(red_right_1, (((w-500)/2)+160+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 2:
				screen.blit(img_dota_green, (((w-500)/2)+260, (h-500)/2-80))
				screen.blit(green_right_1, (((w-500)/2)+260+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 3:
				screen.blit(img_dota_yellow, (((w-500)/2)+360, (h-500)/2-80))
				screen.blit(yellow_right_1, (((w-500)/2)+360+(80-45)/2, (h-500)/2-80+(80-45)/2))
	elif num == 3:
		for i in range(num):
			if i == 0:
				screen.blit(img_dota_blue, ((w-500)/2+110, (h-500)/2-80))
				screen.blit(blue_right_1, ((w-500)/2+110+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 1:
				screen.blit(img_dota_red, (((w-500)/2)+210, (h-500)/2-80))
				screen.blit(red_right_1, (((w-500)/2)+210+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 2:
				screen.blit(img_dota_green, (((w-500)/2)+310, (h-500)/2-80))
				screen.blit(green_right_1, (((w-500)/2)+310+(80-45)/2, (h-500)/2-80+(80-45)/2))
	elif num == 2:
		for i in range(num):
			if i == 0:
				screen.blit(img_dota_blue, ((w-500)/2+90, (h-500)/2-80))
				screen.blit(blue_right_1, ((w-500)/2+90+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif i == 1:
				screen.blit(img_dota_red, (((w-500)/2)+330, (h-500)/2-80))
				screen.blit(red_right_1, (((w-500)/2)+330+(80-45)/2, (h-500)/2-80+(80-45)/2))
	# screen.blit(img_bluegoti, (x_b, y_b))
	pygame.display.flip()
	walkCounter     = 0
	# back_button = button(screen, w-250, h-100, 200, 50, (255, 255, 255), (255, 0, 0), 'BACK', font_1)
	wc = 0
	while True:
		if walkCounter >= 2:
			walkCounter = 0
		if text_speak[1] == 1:
			screen.blit(bg, (0, 0))
			if num == 4:
				for i in range(num):
					if i == 0:
						screen.blit(img_dota_blue, ((w-500)/2+60, (h-500)/2-80))
						screen.blit(blue_right_1, ((w-500)/2+60+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 1:
						screen.blit(img_dota_red, (((w-500)/2)+160, (h-500)/2-80))
						screen.blit(red_right_1, (((w-500)/2)+160+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 2:
						screen.blit(img_dota_green, (((w-500)/2)+260, (h-500)/2-80))
						screen.blit(green_right_1, (((w-500)/2)+260+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 3:
						screen.blit(img_dota_yellow, (((w-500)/2)+360, (h-500)/2-80))
						screen.blit(yellow_right_1, (((w-500)/2)+360+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif num == 3:
				for i in range(num):
					if i == 0:
						screen.blit(img_dota_blue, ((w-500)/2+110, (h-500)/2-80))
						screen.blit(blue_right_1, ((w-500)/2+110+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 1:
						screen.blit(img_dota_red, (((w-500)/2)+210, (h-500)/2-80))
						screen.blit(red_right_1, (((w-500)/2)+210+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 2:
						screen.blit(img_dota_green, (((w-500)/2)+310, (h-500)/2-80))
						screen.blit(green_right_1, (((w-500)/2)+310+(80-45)/2, (h-500)/2-80+(80-45)/2))
			elif num == 2:
				for i in range(num):
					if i == 0:
						screen.blit(img_dota_blue, ((w-500)/2+90, (h-500)/2-80))
						screen.blit(blue_right_1, ((w-500)/2+90+(80-45)/2, (h-500)/2-80+(80-45)/2))
					elif i == 1:
						screen.blit(img_dota_red, (((w-500)/2)+330, (h-500)/2-80))
						screen.blit(red_right_1, (((w-500)/2)+330+(80-45)/2, (h-500)/2-80+(80-45)/2))
			text_speak[1] = 0
		speak(text_speak[0])
		# if notRolled:
		# screen.blit(diceSides[diceSides[6]], (a-200, b-100))
			# notRolled = False
		screen.blit(img_map, ((w-500)/2, (h-500)/2))
		# if win and text_speak[0] == 'speak':
		# 	voice_victory.change_volume(1)
		# elif win and text_speak[0] == 'dontspeak':
		# 	voice_victory.change_volume(0)
		# pygame.display.flip()
		if color_num == 0:
			screen.blit(img_blue, (w/2+300, h/2+110))
		elif color_num == 1:
			screen.blit(img_red, (w/2+300, h/2+110))
		elif color_num == 2:
			screen.blit(img_green, (w/2+300, h/2+110))
		elif color_num == 3:
			screen.blit(img_yellow, (w/2+300, h/2+110))
		screen.blit(diceSides[diceSides[6]] , (w/2+345, h/2+155))
		screen.blit(img_return, (w-250, h-100))
		# back_button.draw()
		# if ask:

		# if number_belu == 0 and come_blue and (x_b, y_b) in array_ask and (x_b, y_b) != array_taple[0]:
		# 	array_taple[0] = (x_b, y_b)
		# 	asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'blue')
		# elif number_red == 0 and come_red and (x_r, y_r) in array_ask and (x_r, y_r) != array_taple[1]:
		# 	array_taple[1] = (x_r, y_r)
		# 	asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'red')
		# elif  number_green == 0 and come_green and (x_g, y_g) in array_ask and (x_g, y_g) != array_taple[2]:
		# 	array_taple[2] = (x_g, y_g)
		# 	asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'green')
		# elif  number_yellow == 0 and come_yellow and (x_y, y_y) in array_ask and (x_y, y_y) != array_taple[3]:
		# 	array_taple[3] = (x_y, y_y)
		# 	asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'yellow')
		

		# array_taple[0] = (x_b, y_b)
		# array_taple[1] = (x_r, y_r)
		# array_taple[2] = (x_g, y_g)
		# array_taple[3] = (x_y, y_y)

		if number_belu >= 1:
			if y_b == b-450 and x_b-(number_belu*50) < a:
				if number_belu != 6:
					if color_num == num-1:
						color_num = 0
					else:
						color_num = 1
				number_belu = 0
			else:
				tp_blue = True
				color_num   = 0
				array_poss  = animation(x_b, y_b, number_belu, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'blue')
				number_belu = 0
				x_b         = array_poss[0]
				y_b         = array_poss[1]
				
				if number_belu == 0:
					if x_b==x_r and y_b==y_r:
						hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
						come_red   = False
						x_r        = a-50
						y_r        = b
					elif x_b==x_g and y_b==y_g:
						print('1')
						hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
						come_green   = False
						x_g          = a-50
						y_g          = b
					elif x_b==x_y and y_b==y_y:
						hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
						come_yellow   = False
						x_y           = a-50
						y_y           = b
					if diceSides[6] != 5:
						if color_num == num-1:
							color_num = 0
						else:
							color_num = 1

		if number_belu <= -1:
			tp_blue = True
			color_num = 0
			array_poss   = animation(x_b, y_b, number_belu, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'blue')
			number_belu = 0
			x_b         = array_poss[0]
			y_b         = array_poss[1]
			if number_belu == 0:
				if x_b==x_r and y_b==y_r:
					hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
					come_red   = False
					x_r        = a-50
					y_r        = b
				elif x_b==x_g and y_b==y_g:
					hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
					come_green   = False
					x_g          = a-50
					y_g          = b
				elif x_b==x_y and y_b==y_y:
					hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
					come_yellow   = False
					x_y           = a-50
					y_y           = b
				if diceSides[6] != 5:
					if color_num == num-1:
						color_num = 0
					else:
						color_num = 1

		if number_red >= 1:
			if y_r == b-450 and x_r-(number_red*50) < a:
				if number_red != 6:
					if color_num == num-1:
						color_num = 0
					else:
						color_num = 2
				number_red = 0
			else:
				tp_red = True
				color_num  = 1
				array_poss  = animation(x_r, y_r, number_red, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'red')
				number_red = 0
				x_r        = array_poss[0]
				y_r        = array_poss[1]
				if number_red == 0:
					if x_b==x_r and y_b==y_r:
						hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
						come_blue  = False
						x_b        = a-50
						y_b        = b
					elif x_r==x_g and y_r==y_g:
						print('2')
						hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
						come_green   = False
						x_g          = a-50
						y_g          = b
					elif x_r==x_y and y_r==y_y:
						hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
						come_yellow   = False
						x_y           = a-50
						y_y           = b
					if diceSides[6] != 5:
						if color_num == num-1:
							color_num = 0
						else:
							color_num = 2

		if number_red <= -1:
			tp_red = True
			color_num  = 1
			array_poss  = animation(x_r, y_r, number_red, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'red')
			number_red = 0
			x_r        = array_poss[0]
			y_r        = array_poss[1]
			if number_red == 0:
				if x_b==x_r and y_b==y_r:
					hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
					come_blue  = False
					x_b        = a-50
					y_b        = b
				elif x_r==x_g and y_r==y_g:
					hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
					come_green   = False
					x_g          = a-50
					y_g          = b
				elif x_r==x_y and y_r==y_y:
					hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
					come_yellow   = False
					x_y           = a-50
					y_y           = b
				if diceSides[6] != 5:
					if color_num == num-1:
						color_num = 0
					else:
						color_num = 2

		if number_green >= 1:
			if y_g == b-450 and x_g-(number_green*50) < a:
				if number_green != 6:
					if color_num == num-1:
						color_num = 0
					else:
						color_num =3
				number_green = 0
			else:
				tp_green = True
				color_num    = 2
				array_poss    = animation(x_g, y_g, number_green, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'green')
				number_green = 0
				x_g          = array_poss[0]
				y_g          = array_poss[1]
				if number_green == 0:
					if x_g==x_r and y_g==y_r:
						hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
						come_red   = False
						x_r        = a-50
						y_r        = b
					elif x_b==x_g and y_b==y_g:
						hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
						come_blue    = False
						x_b          = a-50
						y_b          = b
					elif x_g==x_y and y_g==y_y:
						hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
						come_yellow   = False
						x_y           = a-50
						y_y           = b
					if diceSides[6] != 5:
						if color_num == num-1:
							color_num = 0
						else:
							color_num = 3

		if number_green <= -1:
			tp_green = True
			color_num    = 2
			array_poss    = animation(x_g, y_g, number_green, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'green')
			number_green = 0
			x_g          = array_poss[0]
			y_g          = array_poss[1]
			if number_green == 0:
				if x_g==x_r and y_g==y_r:
					hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
					come_red   = False
					x_r        = a-50
					y_r        = b
				elif x_b==x_g and y_b==y_g:
					hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
					come_blue    = False
					x_b          = a-50
					y_b          = b
				elif x_g==x_y and y_g==y_y:
					hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
					come_yellow   = False
					x_y           = a-50
					y_y           = b
				if diceSides[6] != 5:
					if color_num == num-1:
						color_num = 0
					else:
						color_num = 3

		if number_yellow >= 1:
			if y_y == b-450 and x_y-(number_yellow*50) < a:
				if number_yellow != 6:
					color_num = 0
				number_yellow = 0
			else:
				tp_yellow = True
				color_num     = 3
				array_poss     = animation(x_y, y_y, number_yellow, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'yellow')
				number_yellow = 0
				x_y           = array_poss[0]
				y_y           = array_poss[1]
				print('x_y', x_y, ' , y_y', y_y, ' ,x_g', x_g, ', y_g', y_g)
				if number_yellow == 0:
					if x_y==x_r and y_y==y_r:
						hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
						come_red   = False
						x_r        = a-50
						y_r        = b
					elif x_y==x_g and y_y==y_g:
						print('3')
						hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
						come_green   = False
						x_g          = a-50
						y_g          = b
					elif x_b==x_y and y_b==y_y:
						hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
						come_blue     = False
						x_y           = a-50
						y_y           = b
					if diceSides[6] != 5:
						color_num = 0

		if number_yellow <= -1:
			tp_yellow = True
			color_num     = 3
			array_poss     = animation(x_y, y_y, number_yellow, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'yellow')
			number_yellow = 0
			x_y           = array_poss[0]
			y_y           = array_poss[1]
			if number_yellow == 0:
				if x_y==x_r and y_y==y_r:
					hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
					come_red   = False
					x_r        = a-50
					y_r        = b
				elif x_y==x_g and y_y==y_g:
					hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
					come_green   = False
					x_g          = a-50
					y_g          = b
				elif x_b==x_y and y_b==y_y:
					hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
					come_blue     = False
					x_y           = a-50
					y_y           = b
				if diceSides[6] != 5:
					color_num = 0

		array_pos[0] = (x_b, y_b)
		array_pos[1] = (x_r, y_r)
		array_pos[2] = (x_g, y_g)
		array_pos[3] = (x_y, y_y)

		if number_belu == 0 and come_blue and (x_b, y_b) in array_ask and (x_b, y_b) != array_taple[0]:
			array_taple[0] = (x_b, y_b)
			asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'blue')
		elif number_red == 0 and come_red and (x_r, y_r) in array_ask and (x_r, y_r) != array_taple[1]:
			array_taple[1] = (x_r, y_r)
			asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'red')
		elif  number_green == 0 and come_green and (x_g, y_g) in array_ask and (x_g, y_g) != array_taple[2]:
			array_taple[2] = (x_g, y_g)
			asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'green')
		elif  number_yellow == 0 and come_yellow and (x_y, y_y) in array_ask and (x_y, y_y) != array_taple[3]:
			array_taple[3] = (x_y, y_y)
			asking(num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, number_belu, number_red, number_green, number_yellow, number, notRolled, color_num, come_blue, come_red, come_green, come_yellow, 'yellow')
		

		array_taple[0] = (x_b, y_b)
		array_taple[1] = (x_r, y_r)
		array_taple[2] = (x_g, y_g)
		array_taple[3] = (x_y, y_y)


		if tp_blue:
			(x_b, y_b) = tp(x_b, y_b, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y)
			tp_blue = False
			if x_b==x_r and y_b==y_r:
				hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
				come_red   = False
				x_r        = a-50
				y_r        = b
			elif x_b==x_g and y_b==y_g:
				hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
				come_green   = False
				x_g          = a-50
				y_g          = b
			elif x_b==x_y and y_b==y_y:
				hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'blue')
				come_yellow   = False
				x_y           = a-50
				y_y           = b
		if tp_red:
			(x_r, y_r) = tp(x_r, y_r, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y)
			tp_red = False
			if x_b==x_r and y_b==y_r:
				hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
				come_blue  = False
				x_b        = a-50
				y_b        = b
			elif x_r==x_g and y_r==y_g:
				hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
				come_green   = False
				x_g          = a-50
				y_g          = b
			elif x_r==x_y and y_r==y_y:
				hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'red')
				come_yellow   = False
				x_y           = a-50
				y_y           = b
		if tp_green:
			(x_g, y_g) = tp(x_g, y_g, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y)
			tp_green = False
			if x_g==x_r and y_g==y_r:
				hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
				come_red   = False
				x_r        = a-50
				y_r        = b
			elif x_b==x_g and y_b==y_g:
				hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
				come_blue    = False
				x_b          = a-50
				y_b          = b
			elif x_g==x_y and y_g==y_y:
				hit(x_y, y_y, 'yellow', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'green')
				come_yellow   = False
				x_y           = a-50
				y_y           = b
		if tp_yellow:
			(x_y, y_y) = tp(x_y, y_y, num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y)
			tp_yellow = False
			if x_y==x_r and y_y==y_r:
				hit(x_r, y_r, 'red', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
				come_red   = False
				x_r        = a-50
				y_r        = b
			elif x_y==x_g and y_y==y_g:
				hit(x_g, y_g, 'green', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
				come_green   = False
				x_g          = a-50
				y_g          = b
			elif x_b==x_y and y_b==y_y:
				hit(x_b, y_b, 'blue', num, x_b, y_b, x_r, y_r, x_g, y_g, x_y, y_y, 'yellow')
				come_blue     = False
				x_y           = a-50
				y_y           = b


		if (x_b == a and y_b == b-450) or (x_r == a and y_r == b-450) or (x_g == a and y_g == b-450) or (x_y == a and y_y == b-450):
			voice_main.change_volume(0)
			if text_speak[0] == 'speak' and not win:
				pygame.mixer.music.play(0)
			win = True
			# else:
			# 	voice_victory.change_volume(0)
			# 	voice_victory.play_sound(0)
		# array_ezafe  = [(x_b, y_b), (x_r, y_r), (x_g, y_g), (x_y, y_y)]

		# array_pos[0] = array_ezafe[0]
		# array_pos[1] = array_ezafe[1]
		# array_pos[2] = array_ezafe[2]
		# array_pos[3] = array_ezafe[3]

		array_pos[0] = (x_b, y_b)
		array_pos[1] = (x_r, y_r)
		array_pos[2] = (x_g, y_g)
		array_pos[3] = (x_y, y_y)



		if not come_blue:
			array_pos[0]    = (0, 0)
			array_taple[0]  = (0, 0)
		if not come_red:
			array_pos[1]    = (0, 0)
			array_taple[1]  = (0, 0)
		if not come_green:
			array_pos[2]    = (0, 0)
			array_taple[2]  = (0, 0)
		if not come_yellow:
			array_pos[3]    = (0, 0)
			array_taple[3]  = (0, 0)


		counter_tas = True
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				k, j = event.pos
				# j = j+b-100
				# k = k+a-200
				# print('k = ' , k , ' j = ' , j)
				if k>=w-250 and k<=w-250+165 and j>=h-100 and j<=h-13:
					if win:
						pygame.mixer.music.stop()
					if text_speak[0] == 'speak':
						voice_button.play_sound(0)
					menu()

				elif k>10 and k<62 and j>20 and j<72 :
					if text_speak[0] == 'speak':
						# pygame.mixer.music.pause()
						voice_main.puase()
						text_speak[0] = 'dontspeak'
						text_speak[1] = 1
					elif text_speak[0] == 'dontspeak':
						# pygame.mixer.music.unpause()
						voice_main.unpause(-1)
						text_speak[0] = 'speak'
						text_speak[1] = 1
				elif k>=w/2+335 and k<=w/2+385 and j>=h/2+165 and j<=h/2+215 and counter_tas and not win:
					# print(counter_tas)
					shans = False
					if (color_num == 0 and not come_blue) or (color_num == 1 and not come_red) or (color_num == 2 and not come_green) or (color_num == 3 and not come_yellow):
						shans = True
					counter_tas = False
					if text_speak[0] == 'speak':
						# pygame.mixer.music.play()
						voice_tas.play_sound(0)
					if shans:
						for j in range(1, 30):
							if wc >= 4:
								wc = 0
							randomDiceSide = random.randint(0, 11)
							# u, z-100
							# u-90, z-140
							screen.blit(diceSides_shans[randomDiceSide] , (w/2+345, h/2+155))
							screen.blit(img_map, (a, b-450))
							for i in range(num):
								if num-i == 1 and come_blue and (x_b != a-50):
									if y_b in array_right:
										screen.blit(walkRight_b[wc // 2], (x_b, y_b))
									elif y_b in array_left:
										screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
								elif num-i == 2 and come_red and (x_r != a-50):
									if y_r in array_right:
										screen.blit(walkRight_r[wc // 2], (x_r, y_r))
									elif y_r in array_left:
										screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
								elif num-i == 3 and come_green  and (x_g != a-50):
									if y_g in array_right:
										screen.blit(walkRight_g[wc // 2], (x_g, y_g))
									elif y_g in array_left:
										screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
								elif num-i == 4 and come_yellow and (x_y != a-50):
									if y_y in array_right:
										screen.blit(walkRight_y[wc // 2], (x_y, y_y))
									elif y_y in array_left:
										screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
							wc = wc+1
							pygame.time.delay(30)
							pygame.display.update()
						if randomDiceSide == 0 or randomDiceSide == 9:
							randomDiceSide = 0
						elif randomDiceSide == 1:
							randomDiceSide = 1
						elif randomDiceSide == 3 or randomDiceSide == 10:
							randomDiceSide = 2
						elif randomDiceSide == 2 or randomDiceSide == 5 or randomDiceSide == 8 or randomDiceSide == 11:
							randomDiceSide = 5
						elif randomDiceSide == 4 or randomDiceSide == 7:
							randomDiceSide = 4
						elif randomDiceSide == 6:
							randomDiceSide = 3
					else:
						for j in range(1, 30):
							if wc >= 4:
								wc = 0
							randomDiceSide = random.randint(0, 5)
							# u, z-100
							# u-90, z-140
							screen.blit(diceSides[randomDiceSide] , (w/2+345, h/2+155))
							screen.blit(img_map, (a, b-450))
							for i in range(num):
								if num-i == 1 and come_blue and (x_b != a-50):
									if y_b in array_right:
										screen.blit(walkRight_b[wc // 2], (x_b, y_b))
									elif y_b in array_left:
										screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
								elif num-i == 2 and come_red and (x_r != a-50):
									if y_r in array_right:
										screen.blit(walkRight_r[wc // 2], (x_r, y_r))
									elif y_r in array_left:
										screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
								elif num-i == 3 and come_green  and (x_g != a-50):
									if y_g in array_right:
										screen.blit(walkRight_g[wc // 2], (x_g, y_g))
									elif y_g in array_left:
										screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
								elif num-i == 4 and come_yellow and (x_y != a-50):
									if y_y in array_right:
										screen.blit(walkRight_y[wc // 2], (x_y, y_y))
									elif y_y in array_left:
										screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
							wc = wc+1
							pygame.time.delay(50)
							pygame.display.update()	 #animation e charkhidane tass
					finalSide    = randomDiceSide + 1
					diceSides[6] = randomDiceSide
					if number == 0:
						if come_blue:
							if finalSide == 6:
								number_belu  = finalSide
							else:
								number_belu  = finalSide
								color_num    = color_num+1
								number       = number+1
						else:
							if finalSide == 6:
								come_blue = True
							else:
								color_num    = color_num+1
								number       = number+1
					elif number == 1:
						if come_red:
							if finalSide == 6:
								number_red  = finalSide
							else:
								number_red = finalSide
								color_num  = color_num+1
								number     = number+1
						else:
							if finalSide == 6:
								come_red = True
							else:
								color_num    = color_num+1
								number       = number+1
					elif number == 2:
						if come_green:
							if finalSide == 6:
								number_green  = finalSide
							else:
								number_green = finalSide
								color_num    = color_num+1
								number       = number+1
						else:
							if finalSide == 6:
									come_green = True
							else:
								color_num    = color_num+1
								number       = number+1
					else:
						if come_yellow:
							if finalSide == 6:
								number_yellow  = finalSide
							else:
								number_yellow = finalSide
								color_num     = color_num+1
								number        = number+1
						else:
							if finalSide == 6:
								come_yellow= True
							else:
								color_num    = color_num+1
								number       = number+1
					# number    = number+1
					# color_num = color_num+1
					if number == num:
						number = 0
					if color_num == num:
						color_num = 0
					# pygame.time.delay(150)
					time.sleep(0.3)
		# screen.blit(img_bluegoti, (x_b, y_b))
		if wc >= 4:
			wc = 0
		for i in range(num):
			if num-i == 1 and come_blue and (x_b != a-50):
				if y_b in array_right:
					screen.blit(walkRight_b[wc // 2], (x_b, y_b))
				elif y_b in array_left:
					screen.blit(walkLeft_b[wc // 2], (x_b, y_b))
			elif num-i == 2 and come_red and (x_r != a-50):
				if y_r in array_right:
					screen.blit(walkRight_r[wc // 2], (x_r, y_r))
				elif y_r in array_left:
					screen.blit(walkLeft_r[wc // 2], (x_r, y_r))
			elif num-i == 3 and come_green  and (x_g != a-50):
				if y_g in array_right:
					screen.blit(walkRight_g[wc // 2], (x_g, y_g))
				elif y_g in array_left:
					screen.blit(walkLeft_g[wc // 2], (x_g, y_g))
			elif num-i == 4 and come_yellow and (x_y != a-50):
				if y_y in array_right:
					screen.blit(walkRight_y[wc // 2], (x_y, y_y))
				elif y_y in array_left:
					screen.blit(walkLeft_y[wc // 2], (x_y, y_y))
		wc = wc + 1
		if win:
			screen.blit(img_victory, (a, b-350))



		# walkCounter = walkCounter+1
		pygame.display.update()
		pygame.display.flip()
		pygame.time.delay(50)

menu()


