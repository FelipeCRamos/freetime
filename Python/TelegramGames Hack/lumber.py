# LumberJack Hack
# Made by FelipeCRamos


import cv2
import numpy as np
from PIL import ImageGrab
import directkeys
import time

def process_img(original_image):
	processed_img = cv2.cvtColor(np.array(original_image), cv2.COLOR_BGR2GRAY)
	return processed_img

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

left = 0xDB
right = 0xDC
last_key = 0xDB
player = Point(362, 481)

tll = Point(360, 353)
tlr = Point(480, 353)



'''while(True):
	screen = ImageGrab.grab(bbox = (0, 0, tlr.x+100, tlr.y+100)) # x, y
	new_screen = process_img(screen)
	#if(new_screen[tlr.y, tlr.x])
	if(new_screen[tlr.y, tlr.x] == 89): #if right tree is on limit
		PressKey(0xDB)
		time.sleep(1/2)
		ReleaseKey(0xDB)
		print("Left toggled")
		last_key = 0xDB
	elif(new_screen[tll.y, tll.x] == 89):
		PressKey(0xDC)
		time.sleep(1/2)
		ReleaseKey(0xDC)
		print("Right toggled")
		last_key = 0xDC
	else:
		PressKey(last_key)

	print(new_screen[tlr.y, tlr.x])
	new_screen[tlr.y, tlr.x] = 0
	print(new_screen[tll.y, tll.x])
	new_screen[tll.y, tll.x] = 0
	cv2.imshow('pwn3d', np.array(new_screen))




	if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
'''

while(True):
	PressKey(0xDB)
	print("Pressing left")
	ReleaseKey(0xDB)
three_color = 0
three_heigh_limit = 0


# 481x362 (player_head)