import time,random,datetime,os,sys

print("Welcome to Moss")

class Player():
    def __init__(self,health,maxhealth,xp,maxxp,lvl,df,atk,__flichance,__chance):
        self.health = 100
        self.maxhealth = 100
        self.xp = 0
        self.maxxp = 100
        self.lvl = 1
        self.df = 10
        self.atk = 1
        self.__flichance = 10
        self.__chance = 95

    def levelUp(self):
        if self.xp >= self.maxxp:
            if self.__chance >= 50:
                self.__chance -= self.chance//20
            if self.__flichance <= 90:
                self.__flichance += self.flichance//20
            self.maxxp*=2
            self.lvl += 1
            self.xp -= self.xp
            print("LEVEL UP\nLvl:{} - MaxXp:{}").format(self.lvl,self.maxxp)
            

class Enemy():
    def __init__(self,health,maxhealth,reward,lvl,df,atk):
        self.health = health
        self.maxhealth = maxhealth
        self.reward = reward
        self.lvl = lvl
        self.df = df
        self.atk = atk

        

#ITEMS-----------------------------------------
class Item():
    def __init__(self,name,amount,__price,val):
        self.name = name
        self.amount = amount
        self.__price = __price
        self.val = self.amount * __price


class wood(Item):
    def __init__(self):
        self.name = "Wood"
        self.amount = 0
        self.__price = 10
        self.val = Item.val


        
    

#WEAPONS---------------------------------------
class Weapon():
    def __init__(self,name,atk,df,price):
        self.name = name
        self.atk = atk
        self.df = df
        self.price = price

class stonedagger(Weapon):
    def __init__(self):
        self.name = "Stone Dagger"
        self.atk = 8
        self.df = 2
        self.price = 200

class rustysword(Weapon):
    def __init__(self):
        self.name = "rusty sword"
        self.atk = 15
        self.df = 4
        self.price = 400

class metalsword(Weapon):
    def __init__(self):
        self.name = "metalsword"
        self.atk = 20
        self.df = 8
        self.price = 800

class steelsword(Weapon):
    def __init__(self):
        self.name = "steelsword"
        self.atk = 25
        self.df = 10
        self.price = 1000

class mastersword(Weapon):
    def __init__(self):
        self.name = "mastersword"
        self.atk = 40
        self.df = 16
        self.price = 4000

class diabolus(Weapon):
    def __init__(self):
        self.name = "diabolus"
        self.atk = 55
        self.df = 32
        self.price = 6000
#---------------------------------------------
class Inventory():
    def __init__(self):
        self.items = {}
        self.weapons = {}
    #eg inventory.add_item(Item('Sword', 5, 1, 2))
    def addItem(self, item):
        self.items[item.name] = item

    def returnItems(self):
        print("\t".join(["Name","Amount","Val"]))
        for item in self.items.values():
            print("\t".join([str(x)for x in [item.name,item.amount,item.val]]))

    def addWeapon(self,item):
        self.weapons[item.name] = item
        
    def returnWeapons(self):
        print("\t".join(["Name","Atk","Df","Val"]))
        for item in self.weapons.values():
            print("\t".join([str(x)for x in [item.name,item.atk,item.df,item.price]]))
            
        
