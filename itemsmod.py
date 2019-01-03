import time,random,datetime,os,sys
import utils as u
import chars as c

###Items and stuff
#ITEMS--------------------------------------------------------------------------
class Item():
    def __init__(self):
        self.name = ""
        self.amount = 0
        self.price = 0
        self.baseeff  = 0 
    
    def inspect(self):
        val = self.amount*self.price
        print("\n================\n{}\nYou have : {}\nValue{}".format(self.name,self.amount,str(val)))

class wood(Item):
        name = "wood"
        amount = 0
        price = 10
        baseeff  = 10

##    name = "wood"
##    amount = 0
##    price = 10
##    baseeff = 10

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
    name = "Tool"
    eff = 0
    price = 0
    time = 10

    def farm(self):
        if c.player.location != "Wilderness":
            print("You can not farm for materials in your current location")
        else:
            while True:
                command = input("What do you want to farm?\n1.)Wood\n2.)Stone\n>>").strip(" ")
                if command == "1":
                    print("You travel to a nearby forest and use your {} to chop down some trees\nChopping...".format(name))
                    time.sleep(time)
                    
                elif command == "2":
                    print("You travel to a nearby mountain and use your {} to dig into the mountain\nDigging...".format(name))
                    time.sleep(time)

                else:
                    print("Invalid Command")

    def inspect(self):
        print("\n================\n{}\nEfficiency:{}\n================".format(self.name,self.eff))

        while True:
            if c.player.equippedTool ==self:
                print("=EQUIPPED=")
            command= input("1.)Equip\nb.)Back\n>>").lower().strip(" <X>")
            if command =="1":
                if c.player.equippedTool == self:
                    print("This item is already equipped")
                c.player.equippedTool = self
                print("Equipped:{}".format(c.player.equippedTool.name))
            elif command == "b":
                break
            else:
                print("Invalid Command")


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
    price = 0
    def inspect(self):
        print("\n================\n{}\nAttack:{}\nPrice:{}\n================".format(self.name,self.atk,self.price))

        while True:
            if c.player.equippedWeapon ==self:
                print("=EQUIPPED=")
            command= input("1.)Equip\nb.)Back\n>>").lower().strip(" <X>")
            if command =="1":
                if c.player.equippedWeapon == self:
                    print("This item is already equipped")
                c.player.equippedWeapon = self
                print("Equipped:{}".format(c.player.equippedWeapon.name))
            elif command == "b":
                break
            else:
                print("Invalid Command")


class rock(Weapon):
    name = "Rock"
    atk  = 5
    price = 0


class stonedagger(Weapon):
    name = "stonedagger"
    atk = 8
    price = 200

class rustysword(Weapon):
    name = "rusty sword"
    atk = 15
    price = 400

class metalsword(Weapon):
    name ="metalsword"
    atk = 20
    price = 800

class steelsword(Weapon):
    name = "steelsword"
    atk = 25
    price = 1000

class mastersword(Weapon):
    name = "mastersword"
    atk = 40
    price = 4000

class diabolus(Weapon):
    name = "diabolus"
    atk = 55
    price = 6000

#-------------------------------------------------------------------------------
class Inventory():
    bag = []
    #eg inventory.add_item(Item('Sword', 5, 1, 2))
    # inventory.addTool()
    def add(self,item):
        self.bag.append(item)
        print("You obtained a {}".format(item.name))
    def bagMenu(self):
        if self.bag != []:
            
            selectedNumber = 0
            while True:
                print("==== W - Up , S - Down , B - Back , Press Enter to Confirm ====")
                selectedItem = self.bag[selectedNumber]
                oldSelectedItemName = selectedItem.name
                selectedItem.name = selectedItem.name + "<X>"
                for i in self.bag:
                    print("\n"+i.name)
##                    sys.stdout.write("\r"+i.name)
##                    sys.stdout.flush()
                command = input(">>").lower().strip(" ")
                if command == "w":
                    if selectedNumber == 0:
                        print("Can not go any higher")
                    else:
                        selectedNumber -= 1
                elif command == "s":
                    if selectedNumber == len(self.bag)-1:
                        print("Can not go any lower")
                    else:
                        selectedNumber += 1
                elif command == "":
                    selectedItem.name = oldSelectedItemName
                    selectedItem.inspect(selectedItem)
                    selectedItem.name = selectedItem.name + "<X>"
                elif command == "b":
                    break
                else:
                    print("Invalid command")
                selectedItem.name = oldSelectedItemName
                print(str(selectedNumber))
                print(str(len(self.bag)-1))
                
        else:
            print("The bag is empty")


Inventory.add(Inventory,rock)
Inventory.add(Inventory,hammer)



        
