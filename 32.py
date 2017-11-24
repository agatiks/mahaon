#-------------------------------------------------------------------------------
# Name:        модуль2
# Purpose:
#
# Author:      Ученик
#
# Created:     06.11.2017
# Copyright:   (c) Ученик 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Animal:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
class Predator(Animal):
    def bit(self, victim):
        if isinstance(victim, Mammal):
            victim.die()
            print(self.name, "- Я сгрыз", victim.name)
class Tiger(Predator):
    pass
class Mammal(Predator):
    def die(self):
        del self
class Zebra(Mammal):
    pass
tiger=Tiger("zebra",10)
zebra=Zebra("tiger",20)
tiger.bit(zebra)

