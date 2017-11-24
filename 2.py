#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Ученик
#
# Created:     09.10.2017
# Copyright:   (c) Ученик 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def printN(self):
    print(self.noise)
class Little_child:
    noise=0
    def __init__(self, a=5):
        self.noise=a
    printNoise=printN
anna=Little_child(16)
anna.printNoise()
lisa=Little_child()
lisa.printNoise()
lisa.noise=10
lisa.printNoise()