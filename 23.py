#-------------------------------------------------------------------------------
# Name:        РјРѕРґСѓР»СЊ1
# Purpose:
#
# Author:      РЈС‡РµРЅРёРє
#
# Created:     06.11.2017
# Copyright:   (c) РЈС‡РµРЅРёРє 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
class Sircle:
    def rightr(self, r):
        if r<0:
            print("I'll change r=abs(r)")
            self.__r=abs(r)
        else:
            self.__r=r
    def getr(self):
        return self.__r
    def setr(self, value):
        Sircle.rightr(self, value)
        self.S()
    def delr(self):
        del self.__r
    r = property(getr,setr,delr)
    def S(self):
        self.s=math.pi*self.r*self.r
    def compareS(self, sircle):
        a=self.s
        b=sircle.s
        print(a,b)
        if (a==b):
            print("==")
    def __init__(self, x, y):
        self.coord=(x,y)
        self.__r = 0
sircle1=Sircle(0,0)
sircle1.r=-12
sircle2=Sircle(3,5)
sircle2.r=11
sircle1.compareS(sircle2)
