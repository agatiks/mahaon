#-------------------------------------------------------------------------------
# Name:        РјРѕРґСѓР»СЊ1
# Purpose:
#
# Author:      РЈС‡РµРЅРёРє
#
# Created:     09.10.2017
# Copyright:   (c) РЈС‡РµРЅРёРє 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
class Sircle:
    def rightr(self, r):
        if r<0:
            print("I'll change r=abs(r)")
            self.r=abs(r)
        else:
            self.r=r
    def S(self):
        self.s=math.pi*self.r*self.r
    def compareS(self, sircle):
        a=self.s
        b=sircle.s
        print(a,b)
        if (a==b):
            print("==")
    def __init__(self, r, x, y):
        self.coord=(x,y)
        self.rightr(r);
        self.S();
sircle1=Sircle(-12,0,0)
sircle2=Sircle(11, 3,5)
sircle1.compareS(sircle2)
