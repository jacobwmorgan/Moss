
import time,random,datetime,os,sys
import utils as u
import itemsmod as t
import chars as c

#PLAYER-------------------------------------------------------------------------
class Player():
    def __init__(self):
        self.name = "Prisoner"
        self.health = 100
        self.maxhealth = 100
        self.xp = 0
        self.maxxp = 100
        self.lvl = 1
        self.df = 10
        self.atk = 1
        self.equippedWeapon = ""
        self.equippedTool = ""
        self.flichance = 10
        self.chance = 95
        self.playedBefore = False
        self.location = "Wilderness"

    def changeName(self):
        f = True
        while f :
            newname = str(input("What is your name ? :"))
            while True:
                confirm = input("Your name is {} ? \n 1.Yes \n 2.) No no it's ...\n>>".format(newname)).lower().strip(" ")
                if confirm == "1":                    
                    self.name = newname
                    f = False
                    break
                elif confirm == "2":
                    break
                else:
                    print("You only say 1 or 2 !!!!")
    def playerQuickUi(self):
        print("\n==============================\n{}\nLvl:{}\nHp:{}\nLocation:{}\n==============================".format(self.name,self.lvl,self.health,self.location))
     
    def levelUp(self):
        if self.xp >= self.maxxp:
            if self.chance >= 50:
                self.chance -= self.chance//20
            if self.flichance <= 90:
                self.flichance += self.flichance//20
            self.maxxp*=2
            self.lvl += 1
            self.xp -= self.xp
            print("LEVEL UP\nLvl:{} - MaxXp:{}".format(self.lvl,self.maxxp))

player = Player()
#ENEMYS-------------------------------------------------------------------------
class Enemy():
    
    name = ""
    health = 1 
    maxhealth = 1
    greward = 1
    xpreward = 1
    atk = 1
    chance = 1
    echance = 1
    
    def returnRandomEnemy(self):
        listOfEnemys = [goblin,murloc,orc]
        return random.choice(listOfEnemys)


class goblin(Enemy):
    name = "Goblin"
    health = 20
    maxhealth = 20
    greward = 50
    xpreward = 30
    atk = 4
    chance = 60
    echance = 30

class murloc(Enemy):
    name = "Murloc"
    health = 10
    maxhealth = 10
    greward = 30
    xpreward =  20
    atk = 4
    chance = 80
    echance = 50

class orc(Enemy):
    name = "Orc"
    health = 60
    maxhealth = 60
    greward = 100
    xpreward = 60
    atk = 8
    chance = 30
    echance = 30
