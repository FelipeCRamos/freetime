# Mr. Muscle Hack
# Author: FelipeCRamos
# Tested platform: Windows 10 x64
# Still working on Unix version

import numpy as np
from PIL import ImageGrab, Image
import cv2, time, os

import ctypes

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

try:
	system = os.uname().sysname
	sysval = 0
except AttributeError:
	# probably is a windows pc
	sysval = 1


def process(original_image):
	return cv2.cvtColor(np.array(original_image), cv2.COLOR_BGR2GRAY)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y



# Accuracy of the comparison
if(sysval == 1):
	ac = 48
	bar_color = 48
else:
	ac = 140
	bar_color = 44

# Space Key
space = 0x39

start = Point(150, 142)
end = Point(691, 150)

start2 = Point(150, 150)
end2 = Point(541, 10)
c = Point(271, 5) # stands for center (medium point)
c2 = Point(540,15)



print("Waiting")
now = time.time()
while(True):
	try:
		if(sysval == 1):
			screen = ImageGrab.grab(bbox = (start.x, start.y, end.x, end.y)) # start (x, y) end (x, y)
			new_screen = process(screen)
			if((new_screen[c.y, c.x + ac] == bar_color) and (new_screen[c.y, c.x - ac] == bar_color)):
				PressKey(space)
				ReleaseKey(space)
				print("\n> Space pressed!")
		else:
			os.system("screencapture -R{},{},{},{} frame.png".format(start2.x, start2.y, end2.x, end2.y))
			screen = Image.open("frame.png")
			new_screen = process(screen)
			if((new_screen[c2.y, c2.x + ac] == bar_color) and (new_screen[c2.y, c2.x - ac] == bar_color)):
				PressKey(space)
				ReleaseKey(space)
				print("\n> Space pressed!")
			# new_screen[c2.y, c2.x + ac] = 255
			# new_screen[c2.y, c2.x - ac] = 255
		
		# print(".")
		
		cv2.imshow('pwn3d', np.array(new_screen))
		# print("Loop took {} seconds.".format(time.time()-now))
		now = time.time()
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
	except KeyboardInterrupt:
		print("Exiting...")
		exit()
