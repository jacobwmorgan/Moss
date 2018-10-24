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


class Enemy():
    

class Item():
    def __init__(self,name,atk,df,weight,price):
        self.name = name
        self.atk = atk
        self.df = df
        self.weight = weight
        self.price = price

class Inventory():
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        self.items[item.name] = item

    def returnItems(self):
        print("\t".join(["Name","Atk","Df","Lb","Val"]))
        for item in self.items.values():
            print("\t".join([str(x)for x in [item.name,item.attack,item.armor,item.weight,item.price]]))
            
        
