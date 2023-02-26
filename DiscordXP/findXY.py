import pyautogui as pt
import keyboard as key
import time as t

if __name__ == '__main__':
    while True:
        t.sleep(2)
        if(key.is_pressed('q') and key.is_pressed('ctrl')):
            break
        print(pt.position())