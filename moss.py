import time,random,datetime,os,sys
import utils as u
import itemsmod as t
import chars as c

u.Save.checkSaveDir()

def titleScreen():
    try:
        print("      Welcome to Moss\n         1 Play 1\n         2 Load 2\n         3 Exit 3")
        while True:
            command = input(">>").strip(" ")
            if command == "1":
                game()
            elif command == "2":
                u.Save.load()
            elif command == "3":
                sys.exit()
            else:
                print("Invalid Command")
    except KeyboardInterrupt:
        sys.exit()
        
def game():
    while True:
        pass

titleScreen()
