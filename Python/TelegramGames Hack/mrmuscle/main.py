#!/usr/bin/env python3

"""
Bot for the game Mr. Muscle from @gamee on Telegram
Made by FelipeCRamos
"""

# MacOS X Optimized
# Read more on: https://python-mss.readthedocs.io/usage.html#import
from mss.darwin import MSS

import mss.tools
import pyautogui as pg
import time

class Pixel:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

# Pixel Mappings
middle = Pixel(640, 200)
bar_width = 184
threshold = 4

# Pixels to check on left/right sides
pLeft = Pixel(middle.x - int(bar_width/2), middle.y)
pRight = Pixel(middle.x + int(bar_width/2), middle.y)

# Screen area to crop
monitor = {
    'top': middle.y,
    'left': pLeft.x,
    'width': pRight.x - pLeft.x,
    'height': 2
}

# Start countdown
for i in range(5):
    print("Starting program in {} seconds...".format(5-i))
    time.sleep(1)

with MSS() as sct:
    while True:
        sct_img = sct.grab(monitor)

        left_pixel = sct_img.pixel(threshold, 1) == (10, 41, 61)
        right_pixel = sct_img.pixel(pRight.x - pLeft.x-(threshold+1), 1) == (10, 41, 61)

        # block pixel color: (10, 41, 61)
        if right_pixel and left_pixel:
            pg.press('space')   # Press SPACEBAR
            print("PRESSED! {}".format(time.ctime()))
            time.sleep(0.3)
