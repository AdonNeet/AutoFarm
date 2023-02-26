import pyautogui as pt
import keyboard as k
import time as t

# on linux 1871, 904 (discord blocing in rght side)
def nav_to():
    try:
        pt.keyDown('shift')
        pt.moveTo(1871, 904, duration=0.001)
        pt.click()
        pt.keyUp('shift')
        return 1
    except:
        print('Fail')
        return 0

# main 
if __name__ == '__main__':
    try: 
        t.sleep(5)
        if(nav_to() == 1):
            print('Berhasil di Run')
            exit()
        else: 
            print('Ada sesuatu yang bermasalah')
    except:
        print('Kode gagal')
        exit()
