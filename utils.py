import time,random,datetime,os,sys
import itemsmod as t
import chars as c

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
