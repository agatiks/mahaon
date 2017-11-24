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

class Little_child:
    noise=0
    def __init__(self, a):
        self.noise=a
    def printNoise(self):
        print(self.noise)
anna=Little_child(16)
anna.printNoise()