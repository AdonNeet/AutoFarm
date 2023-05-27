import keyboard as key
import time as t
import random as r
import pyautogui

spam = "w!hunt"

stop = False    # as boolean detector when iteration stopped, global scope

def greeter():
    print("""
    =============================
    Welcome to auto owo Hunt program
    
    How to use:
        Press P           : start
        Ctrl + Q  (push)  : stop the iteration (when started)
        press esc         : exit from program

    Note:
        When you want to exit, you must stop the iteration

    ~ AdonNeet
    =============================    
    """)

def message(ans):
    pyautogui.write(ans)
    pyautogui.press('enter')

def countdown(waktu): 
    while waktu > 0:
        if(key.is_pressed('q') and key.is_pressed('ctrl')):
            global stop
            stop = True 
            print('>> Hunting stopped')  
            break
        else:   
            timer = '{:02d} second'.format(waktu)
            print(timer, end="\r")
            t.sleep(1)
            waktu -= 1

# greeter
greeter()

while True:
    try:
        if(key.is_pressed('p')):
            print('\n>> Start the farming')
            count = 0 # as iteration counter, local scope
            while True:
                countdown(int(r.randint(10, 15)))  # min 60, 60-70 for avoiding ban (or random it)
                if(stop == True):
                    stop = False
                    break
                else:
                    count += 1
                    message(r.choice(spam))
                    print('info : {}th iteration done'.format(count))
        elif(key.is_pressed('esc')):
            print('>> Exit from program')
            break
        else:
            continue
    except:
        if(key.is_pressed('esc')):
            print('>> Exit from program')
            break
        else:
            continue