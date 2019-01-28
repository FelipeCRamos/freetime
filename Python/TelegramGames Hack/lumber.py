# LumberJack Hack
# Made by FelipeCRamos

import cv2
import mss
import numpy as np
import time
import pyautogui as pag

class Pixel:
    def __init__(self, y, x):
        self.y = y
        self.x = x


last_key = 'right'
# Second Level Mapping
secLevelLeft = Pixel(270, 330)
secLevelRight = Pixel(270, 550)

# First Level Mapping
fisLevelLeft = Pixel(485, 330)
fisLevelRight = Pixel(485, 550)

# Cropped screen sizes
cropped_screen = {'top': 120, 'left': 200, 'width': 400, 'height': 400}

while('Own3d the entire sh*t'):
    with mss.mss() as screen_cap:
        screen = np.array(screen_cap.grab(cropped_screen))
        # Some debug shit here
        print("\n~")
        print("L2: {} - R2: {}".format(
            screen[secLevelLeft.y, secLevelLeft.x][0],
            screen[secLevelRight.y, secLevelRight.x][0]))
        print("L1: {} - R1: {}".format(
            screen[fisLevelLeft.y, fisLevelLeft.x][0],
            screen[fisLevelRight.y, fisLevelRight.x][0]))
        # End of the debug shit

        # Defines the color threshold for wood/sky pixels
        threshold = 200

        # The time between one play and another
        sleep_time = 1/2

        if(screen[fisLevelLeft.y+80, fisLevelLeft.x+70][0] == 254):
            print("\n\n\nAguardando...\n\n\n")
            try:
                for i in range(0, 10):
                    print("{}...".format(i))
                    time.sleep(1)
                    continue
            except KeyboardInterrupt:
                print("\nSaindo...")
                exit()

        # l1 check
        if(screen[fisLevelLeft.y, fisLevelLeft.x][0] < threshold):
            print("Pressing right!")
            pag.press('right')
            last_key = 'right'
            time.sleep(sleep_time)

        # r1 check
        elif(screen[fisLevelRight.y, fisLevelRight.x][0] < threshold):
            print("Pressing left!")
            pag.press('left')
            last_key = 'left'
            time.sleep(sleep_time)

        # If none of the sides have a wood stick, press the last_key
        else:
            print("~ Pressed 'last_key' ({})".format(last_key))
            pag.press(last_key)
            time.sleep(sleep_time)

        # Uncomment this to see the cv2 window showing
        # the area that is being cropped
        # cv2.imshow('pwn3d', np.array(screen))

        # A random code that needs to be there to everything work fine
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
