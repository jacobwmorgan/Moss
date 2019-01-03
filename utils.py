import time,random,datetime,os,sys
import itemsmod as t
import chars as c


def openFile(dr):
    li = []
    with open(di +".txt",r) as data:
        for i in data.readlines():
            li.append(i)
    return li


def loading():
    for x in range (0,3):  
        b = ("Loading" + "." * x)
        sys.stdout.write('\r'+b)
        sys.stdout.flush()
        time.sleep(0.5)

def checkString(s):
    isString = isinstance(s,str)
    return isString
#doesnt work and i have no idea how to do it 
def xpBar(x,y):
    z = x//y
    z * 10
    string = (" " + "#" * z)
    print(string)

class Quests():
    def checkQuestDir():
        if os.path.exists("quests") == False:
            print("Quests could not be found \n Please reinstall game and try again \n If this problem reacures please contact the dev")
            exit()
        else:
            print("\nQuest dir ☑\n")

    def addQuest(quest):
        li = c.player.listOfQuests
        if quest not in li:
            li.append(quest)
        else:
            print("You already have this quest in your quest book")

    def listQuests():
        print("==== Quest Book ====")
        li = c.player.listOfQuests
        if  li != []:
            selectedNumber = 0
            while True:
                print("==== W - Up , S - Down , B - Back , Press Enter to Confirm ====")
                selected = li[selectedNumber]
                oldSelectedName = selected.name
                selected.name = selected.name + "<X>"
                for i in li:
                    print("\n"+i.name)
                command = input(">>").lower().strip(" ")
                if command == "w":
                    if selectedNumber == 0:
                        print("Can not go any higher")
                    else:
                        selectedNumber -= 1
                elif command == "s":
                    if selectedNumber == len(li)-1:
                        print("Can not go any lower")
                    else:
                        selectedNumber +=1
                elif command == "":
                    selected.name = oldSelectedName
                    selected.view(selected)
                    selected.name = selected.name + "<X>"
                elif command == "b":
                    break
                else:
                    print("Invalid Command")
                selectedItem.name = oldSelectedName
                   
        else:
            print("You have no quests")

    

class Save():
    def checkSaveDir():
        if os.path.exists("saves") == False:
            print("save directory does not exist\n")
            print("making save directory...\n")
            os.mkdir("saves")
        else:
            print("\nSave dir ☑\n")
    def load():
        if os.listdir("saves") == []:
            print("There are no save files")
        else:
            print("I have no idea how to make this lol")


class Story():
    def grabStory(dr):
        with open("story\\"+dr+".txt","r") as data:
            lines = data.readlines()
            for i in lines:
                print(i)
                time.sleep(0.5)
    def start():
        c.player.playedBefore = True
        c.player.changeName()
        Story.grabStory("start")
