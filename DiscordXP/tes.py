import pyautogui as pt

def nav_to(a, b):
    try:
        post_user = pt.locateOnScreen(a)
        pt.moveTo(post_user[0]+15, post_user[1]+15, duration=.001)
        pt.rightClick()
        del_msg = pt.locateOnScreen(a)
        pt.moveTo(post_user[0]+15, post_user[1]+15, duration=.001)
        pt.click()
        pt.press('enter')
    except:
        print('Gambar tidak ditemukan')
        return 0

# main 
if __name__ == '__main__':
    try: 
        user_png = 'image/user.png'
        del_png = 'image/delete_msg.png'
        nav_to(user_png, del_png)
        print('Kode berhasil')
        exit()
    except:
        print('Kode gagal')
        exit()
