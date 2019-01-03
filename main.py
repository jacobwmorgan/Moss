import time,random,datetime,os,sys
import utils as u
import itemsmod as t
import chars as c

u.Quests.checkQuestDir()
u.Save.checkSaveDir()

def titleScreen():
    try:
        print("         =Moss=\n         1 Play 1\n         2 Load 2\n         3 Exit 3\n\n  A game by Jacob Morgan")
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
    if c.player.playedBefore == False:
        #u.Story.start()
        print("Place holder,//Story will be added later")
    while True:
        c.player.levelUp()
        c.player.playerQuickUi()
        command = input("1.)Explore\n2.)Bag\n3.)Quests\nb.)Exit\n>>").lower().strip(" ")
        if command == "1":
            pass
        elif command == "2":
            t.Inventory.bagMenu(t.Inventory)
        elif command == "3":
            pass
        elif command == "b":
            sys.exit()
        else:
            print("Invalid command")
            
        
titleScreen()
