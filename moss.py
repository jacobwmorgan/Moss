import time,random,datetime,os,sys
import utilities as u

print("Welcome to Moss")

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
        self.equipped = ""
        self.__flichance = 10
        self.__chance = 95

    def changeName(self):
        while True:
            newname = str(input("What is your name ? :"))
            
                confirm = input("Your name is {} ? \n 1.Yes \n 2.) No no it's ...".format(newname)).lower().strip(" ")
                if confirm == "1":
                    self.name = newname
                    break
                elif confirm == "2":
                    pass
                else:
                    print("You only say 1 or 2 !!!!")
            
    def levelUp(self):
        if self.xp >= self.maxxp:
            if self.__chance >= 50:
                self.__chance -= self.__chance//20
            if self.__flichance <= 90:
                self.__flichance += self.__flichance//20
            self.maxxp*=2
            self.lvl += 1
            self.xp -= self.xp
            print("LEVEL UP\nLvl:{} - MaxXp:{}".format(self.lvl,self.maxxp))

player = Player()
#ENEMYS-------------------------------------------------------------------------
class Enemy():
    def __init__(self,name,health,maxhealth,greward,xpreward,atk,chance,echance):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.greward = greward
        self.xpreward = xpreward
        self.atk = atk
        self.chance = chance
        self.echance = echance

    def returnRandomEnemy():
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
#ITEMS--------------------------------------------------------------------------
class Item():
    def __init__(self,name,amount,baseeff,price):
        self.name = name
        self.amount = amount
        self.price = price
        self.baseeff


class wood(Item):
    name = "wood"
    amount = 0
    price = 10
    baseeff = 10

class stone(Item):
    name = "stone"
    amount = 0
    price = 20
    baseeff = 15

class metal(Item):
    name = "metal"
    amount = 0
    price = 30
    baseeff = 8

class gold(Item):
    name = "gold"
    amount = 0
    price = 1
    baseeff = 0

#TOOLS--------------------------------------------------------------------------
class Tool():
    def __init__(self,name,eff,price,time):
        self.name = name
        self.eff = eff
        self.price = price
        self.time = time

class hammer(Tool):
    name = "Hammer"
    eff = 1
    price = 1
    time = 2

class stoneMattock(Tool):
    name = "Stone Mattock"
    eff = 2.5
    price = 300
    time = 1.5

class rustyMattock(Tool):
    name = "Rusty Mattock"
    eff = 3
    price = 450
    time = 1.25
    

class metalMattock(Tool):
    name = "Metal Mattock"
    eff = 4
    price = 600
    time = 1

class magicMattock(Tool):
    name = "Magic Mattock"
    eff = 10
    price = 20000
    time = 0.1


#WEAPONS------------------------------------------------------------------------
class Weapon():
    def __init__(self,name,atk,df,price):
        self.name = name
        self.atk = atk
        self.df = df
        self.price = price

class stonedagger(Weapon):
    name = "stonedagger"
    atk = 8
    df = 2
    price = 200

class rustysword(Weapon):
    name = "rusty sword"
    atk = 15
    df = 4
    price = 400

class metalsword(Weapon):
    name ="metalsword"
    atk = 20
    df = 8
    price = 800

class steelsword(Weapon):
    name = "steelsword"
    atk = 25
    df = 10
    price = 1000

class mastersword(Weapon):
    name = "mastersword"
    atk = 40
    df = 16
    price = 4000

class diabolus(Weapon):
    name = "diabolus"
    atk = 55
    df = 32
    price = 6000

#-------------------------------------------------------------------------------
class Inventory():
    def __init__(self):
        self.items = {}
        self.weapons = {}
        self.tools = {}
    #eg inventory.add_item(Item('Sword', 5, 1, 2))
    # inventory.addTool()
    def addTool(self,item):
        self.tools[item.name] = item

    def returnTools(self):
        print("\t".join(["Name","Efficency","Val"]))
        for item in self.tools.values():
            print("\t",join([str(x)for x in [item.name,item.eff,item.price]]))

    def addItem(self, item):
        self.items[item.name] = item

    def returnItems(self):
        print("\t".join(["Name","Amount","Val"]))
        for item in self.items.values():
            print("\t".join([str(x)for x in [item.name,item.amount,item.price]]))

    def addWeapon(self,item):
        self.weapons[item.name] = item

    def returnWeapons(self):
        print("\t".join(["Name","Atk","Df","Val"]))
        for item in self.weapons.values():
            print("\t".join([str(x)for x in [item.name,item.atk,item.df,item.price]]))

    def returnBag(self):
        print("\t".join(["Name","Amount","Val"]))
        for item in self.items.values():
            print("\t".join([str(x)for x in [item.name,item.amount,item.price]]))

        print("\t".join(["Name","Efficency","Val"]))
        for item in self.tools.values():
            print("\t",join([str(x)for x in [item.name,item.eff,item.price]]))

        print("\t".join(["Name","Atk","Df","Val"]))
        for item in self.weapons.values():
            print("\t".join([str(x)for x in [item.name,item.atk,item.df,item.price]]))


u.hello()
