import keyboard as key
import time as t
import random as r
import pyautogui as pt

# username = 'Adon_Neet#1973' # change into your username

## yeah, for spam text in farming act, edit as you want
# spam = ['koya slap @{user}'.format(user=username), 'owo slap @{user}'.format(user=username), 'tes, lagi farming xp', '123, spontan, uhuy', 'dvorak', 'qwerty', 'aoaoao, esok masih ada hari', 'konnichiwa', 'turu, besok masih bisa di lanjut', 'hallo, saya afk', 'semangat, besok masih ada hari']
spam = ['Ole ole ole ole... ole', 'Tes, 1 2 3', 'Hallo, konnichiwa!', 'tes, lagi farming xp', '123, spontan, uhuy', 'dvorak', 'qwerty', 'aoaoao, esok masih ada hari', 'konnichiwa', 'turu, besok masih bisa di lanjut', 'hallo, saya afk', 'semangat, besok masih ada hari']

## yeah, its for koya or antoher command spam :D
#spam = 'koya slap @{user}'.format(user=username) # it is for koya

stop = False    # as boolean detector when iteration stopped, global scope

# target for image


def greeter():
    print("""
    =============================
    Welcome to cheat XP Discord program
    
    How to use:
        Press P           : start
        Ctrl + Q  (push)  : stop the iteration (when started)
        press esc         : exit from program

    Note:
        - It's automatically delete your own msg
        - When you want to exit, you must stop the iteration


    ~ AdonNeet
    =============================    
    """)


# the nav to image method, and do the job
def delete():
    try:
        #
    except:
        #


# the msg method
def message(ans):
    pt.write(ans)
    pt.press('enter')

# the cdwn method
def countdown(waktu): 
    while waktu > 0:
        if(key.is_pressed('q') and key.is_pressed('ctrl')):
            global stop
            stop = True 
            print('>> Farming stopped')  
            break
        else:   
            timer = '{:02d} second'.format(waktu)
            print(timer, end="\r")
            t.sleep(1)
            waktu -= 1

# greeter, yeah for starting
greeter()

while True:
    try:
        if(key.is_pressed('p')):
            print('\n>> Start the farming')
            count = 0 # as iteration counter, local scope
            while True:
                countdown(int(r.randint(60, 65)))  # min 60, 60-70 for avoiding ban (or random it)
                if(stop == True):
                    stop = False
                    break
                else:
                    count += 1
                    delete()
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

