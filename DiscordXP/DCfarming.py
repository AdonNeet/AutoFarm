import keyboard as key
import time as t
import random as r
import pyautogui

username = 'Adon_Neet#xxxx' # change into your username

## yeah, for spam text in farming act, edit as you want
spam = ['koya slap @{user}'.format(user=username), 'owo slap @{user}'.format(user=username), 'tes, lagi farming xp', '123, spontan, uhuy', 'dvorak', 'qwerty', 'aoaoao, esok masih ada hari', 'konnichiwa', 'turu, besok masih bisa di lanjut', 'hallo, saya afk', 'semangat, besok masih ada hari']

## yeah, its for koya or antoher command spam :D
#spam = 'koya slap @{user}'.format(user=username) # it is for koya

stop = False    # as boolean detector when iteration stopped, global scope

def greeter():
    print("""
    =============================
    Welcome to cheat XP Discord program
    
    How to use:
        press P     : start
        push Q      : stop the iteration (when started)
        press esc   : exit from program

    Note:
        When you want to exit, you must stop the iteration

    ~ AdonNeet
    =============================    
    """)

def countdown(waktu): 
    while waktu > 0:
        if(key.is_pressed('q')):
            global stop
            stop = True 
            print('>> Farming berhenti')
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
            print('>> Start the farming')
            count = 0 # as iteration counter, local scope
            while True:
                countdown(int(r.randint(60, 65)))  # min 60, 60-70 for avoiding ban (or random it)
                if(stop == True):
                    stop = False
                    break
                else:
                    count += 1
                    pyautogui.write(r.choice(spam))
                    pyautogui.press('enter')
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
