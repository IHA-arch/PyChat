import pyautogui as pg
import random2
from time import sleep
import string


def random(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    lum = lower+upper+num
    temp = random2.sample(lum, length)
    send = "".join(temp)
    return send

def typer(length, message):
    if not message:
        temp = random(length)
    else:
        temp = message

    pg.typewrite(temp)
    pg.typewrite(["enter"])

def banner():
    j = random2.randrange(9)
    print('\033[1;3{}m mmmmm                  mmm  #               m   \n #   "# m   m         m"   " # mm    mmm   mm#mm \n #mmm#" "m m"         #      #"  #  "   #    #   \n #       #m#    """   #      #   #  m"""#    #   \n #       "#            "mmm" #   #  "mm"#    "mm \n         m"                                      \n        ""\n'.format(j))

def about():
    print('\033[1;31mCreate By     \t\t\t        \033[1;36m>\033[1;37m \tIHA\n\033[1;31mWritten Language\t        \t\033[1;36m>\033[1;37m \tPython3 & shell\n\033[1;31mSupported Operation System\t\t\033[1;36m>\033[1;37m \tKali Linux\n\033[1;31mPurpose\t\t\t\t\t\033[1;36m>\033[1;37m\tType message where mouse click\n\033[1;31mGitHub \t\t\t\t\t\033[1;36m>\033[1;37m\thttps://github.com/IHA-arch\n\n\n')

        

def pychat():
    banner()
    print("\033[1;31m1              \033[1;37mRandom")
    print("\033[1;31m2              \033[1;37mDefine by user")
    print("\033[1;31m3              \033[1;37mAbout")
    try:
        choice = int(input("\033[1;34mSelect:\033[1;33m"))
    except KeyboardInterrupt:
        print("Exiting....")
        exit()
    except:
        print("please enter an intger value")
        exit()
    if choice == 1:
        try:
            length = int(input("\033[1;31mEnter the length of your message:\033[1;33m"))
            sent = int(input("\033[1;31mHow many time send[0 for infinity(∞)]:\033[1;33m"))
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except:
            print("please enter an intger value")
            exit()
        if sent == 0:
            print("click mouse cursor where you type")
            sleep(5)
            pg.click()
            message = ''
            while True:
                typer(length, message)
        else:
            print("click mouse curser where you type")
            sleep(5)
            pg.click()
            message=''
            for i in range(sent):
                typer(length, message)
    elif choice == 2:
        try:
            message = input("\033[1;31mEnter message:\033[1;33m")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except:
            exit()
        try:
            sent = int(input("\033[1;31mHow many time send[0 for infinity(∞)]:\033[1;33m"))
        except KeyboardInterrupt:
            print("Exiting...")
            exit
        except:
            print("please enter an intger value")
            exit()
        if sent == 0:
            print("click mouse cursor where you type")
            sleep(5)
            pg.click()
            length=''
            while True:
                typer(length, message)
        else:
            print("click mouse curser where you type")
            sleep(5)
            pg.click()
            length=''
            for i in range(sent):
                typer(length, message)
    elif choice == 3:
        about()

    else:
        print("Please choose only 1 or 2")


pychat()
