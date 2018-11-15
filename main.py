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
    #Doesnt work on repl and my schools stupid and wont let us use python outside the computer room :)
    #if c.player.playedBefore == False:
       # u.Story.start()
    while True:
        c.player.levelUp()
        print("\n==============================\n{}\nLvl:{}\nHp:{}\nLocation:{}\n==============================".format(c.player.name,c.player.lvl,c.player.health,c.player.location))
        command = input("1.)Explore\n2.)Bag\n3.)Quests\n>>")

titleScreen()
