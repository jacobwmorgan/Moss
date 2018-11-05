###Items and stuff
#ITEMS--------------------------------------------------------------------------
class Item():
    name = ""
    amount = 0
    price = 0
    baseeff  = 0 


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
    name = ""
    eff = 0
    price = 0
    time = 10

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
    name = ""
    atk = 0
    df = 2
    price = 0

class fists(Weapon):
    name = "Hands"
    atk  = 5
    df = 0
    df = 1

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
