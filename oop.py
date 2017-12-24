import random

class Pirate:
    def __init__(self, name, board_weight):
        self.name = name
        self.board_weight = board_weight
        self.count()

    def count(self):
        self.zoloto=0
        self.empty=0
        self.bolezn=0
        self.vse=0
        while (self.board_weight>0):
            chest = Chest()
            if self.board_weight>=chest.weight:
                self.vse+=1
                if chest.inchest==-1:
                    self.bolezn+=chest.effects
                if chest.inchest==0:
                    self.empty+=1
                if chest.inchest==1:
                    self.zoloto+=chest.effects
                self.board_weight-=chest.weight
            else:
                break


class Chest:
    def __init__(self):
        self.weight = int(random.uniform(4, 11))
        self.inchest = int(random.uniform(-2, 2))#1 - zoloto, 0 - empty, -1 - bolezn
        self.inChest()

    def inChest(self):
        if self.inchest==1:
            self.effects = int(random.uniform(15, 100))
        if self.inchest==0:
            self.effects = 0
        if self.inchest==-1:
            self.effects = int(random.uniform(3, 10))


pirates = [Pirate("Anton", 36), Pirate("Jack", 6), Pirate("Ahmed", 51), Pirate("Nastia", 24)]
print("Everyone's chests: ", pirates[0].name, "-", pirates[0].vse, ";", pirates[1].name, "-", pirates[1].vse, ";", pirates[2].name, "-", pirates[2].vse, ";", pirates[3].name, "-", pirates[3].vse)
piratezoloto = [pirates[0].zoloto, pirates[1].zoloto, pirates[2].zoloto, pirates[3].zoloto]
piratebolezn = [pirates[0].bolezn, pirates[1].bolezn, pirates[2].bolezn, pirates[3].bolezn]
pirateempty = [pirates[0].empty, pirates[1].empty, pirates[2].empty, pirates[3].empty]

print(piratezoloto)
print(piratebolezn)
print(pirateempty)

name=""
for i in range(4):
    if piratezoloto[i] == max(piratezoloto):
        name+=pirates[i].name+" "
print(name, " has the most gold")

name=""
for i in range(4):
    if piratebolezn[i] == max(piratebolezn):
        name+=pirates[i].name+" "
print(name, " is sick most of all")

name=""
for i in range(4):
    if pirateempty[i] == min(pirateempty):
        name+=pirates[i].name+" "
print(name, " has the less empty chests")



'''maxzoloto = pirate1.zoloto
maxbolezn = 0
minempty = 0
allchests = 0
name=""



if pirate2.zoloto>maxzoloto:
    maxzoloto = pirate2.zoloto
    name=pirate2.name+" "
elif pirate2.zoloto == maxzoloto:
    name+=pirate2.name+" "
if pirate3.zoloto>maxzoloto:
    maxzoloto = pirate3.zoloto
    name=pirate3.name+" "
elif pirate3.zoloto == maxzoloto:
    name+=pirate3.name+" "
if pirate4.zoloto>maxzoloto:
    maxzoloto = pirate4.zoloto
    name=pirate4.name+" "
elif pirate4.zoloto == maxzoloto:
    name+=pirate4.name+" "


name=""
if pirate2.bolezn>maxbolezn:
    maxbolezn = pirate2.bolezn
    name=pirate2.name+" "
elif pirate2.bolezn == maxbolezn:
    name+=pirate2.name+" "
if pirate3.bolezn>maxbolezn:
    maxbolezn = pirate3.bolezn
    name=pirate3.name+" "
elif pirate3.bolezn == maxbolezn:
    name+=pirate3.name+" "
if pirate4.bolezn>maxbolezn:
    maxbolezn = pirate4.bolezn
    name=pirate4.name+" "
elif pirate4.bolezn == maxbolezn:
    name+=pirate4.name+" "


name=""
if pirate2.empty == minempty:
    name+=pirate2.name+" "
elif pirate2.empty<minempty:
    minempty = pirate2.empty
    name=pirate2.name+" "
if pirate3.empty == minempty:
    name+=pirate3.name+" "
elif pirate3.empty<minempty:
    minempty = pirate3.empty
    name=pirate3.name+" "
if pirate4.empty == minempty:
    name+=pirate4.name+" "
elif pirate4.empty<minempty:
    minempty = pirate4.empty
    name=pirate4.name+" "
'''






