#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Ученик
#
# Created:     16.10.2017
# Copyright:   (c) Ученик 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cat:
    def getx(self):
        return self.__x
    def setx(self, value):
        self.__x=value
    def delx(self):
        del self.__x
    x = property(getx,setx,delx)
vasia=Cat();
vasia.x=17
print(vasia.x)

