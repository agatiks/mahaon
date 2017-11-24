#-------------------------------------------------------------------------------
# Name:        РјРѕРґСѓР»СЊ1
# Purpose:
#
# Author:      РЈС‡РµРЅРёРє
#
# Created:     15.11.2017
# Copyright:   (c) РЈС‡РµРЅРёРє 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
import random
class Matrix:
    _count=0
    def __init__(self, size, method,x=0,y=0):
        self.method=method
        self._size=size
        self.x=x
        self.y=y
        self.matrix=createMatrix(self)
        self.summ()
        Matrix._count+=1
    def __str__(self):
        st=""
        for i in range(self._size):
            st+=str(self.matrix[i])+'\n'
        return st
    def countMatrix(self):
        n=0
        for i in range( self._size):
            n+=self.matrix[i][i]
        return(n)
    def transposeMatrix(self):
        b=[[0]*self._size for i in range(self._size)]
        for i in range(self._size):
            for j in range(self._size):
                b[j][i]=self.matrix[i][j]
        m=Matrix(self._size, b)
        return m
    def __add__(self, other):
        if self._size==other._size:
            b=[[0]*self._size for i in range(self._size)]
            for i in range(self._size):
                for j in range(self._size):
                    b[i][j]=self.matrix[i][j]+other.matrix[i][j]
            return Matrix(self._size, b)
        else:
            print("No +")
    def summ(self):
        self.summ=0
        for i in range(self._size):
            for j in range(self._size):
                self.summ+=self.matrix[i][j]
    def __lt__(self, other):
        if self.summ>other.summ:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.summ==other.summ:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.summ<other.summ:
            return True
        else:
            return False

    @property
    def get(self):
        return Matrix._count
        return self._size
def createMatrix(m):
    matrix=[[0]*m._size for i in range(m._size)]
    if (m.method=="rnd"):
        for i in range (m._size):
            for j in range (m._size):
                matrix[i][j]=int(random.uniform(m.x, m.y))
    else:
        matrix=m.method
    return matrix
'''matrix1=Matrix(3, "rnd",0,10)
print(str(matrix1))
matrix1=matrix1.transposeMatrix()
print(str(matrix1))
matrix2=Matrix(3,[[3,5,7],[5,8,1],[1,7,4]])
print(str(matrix2))
print(matrix2.countMatrix())
print(str(matrix2+matrix1))'''
matrix1=Matrix(5, "rnd",0,10)
matrix2=Matrix(5, "rnd",0,10)
matrix3=Matrix(4, "rnd",0,10)
matrix4=Matrix(4, "rnd",0,10)
matrix5=Matrix(3, "rnd",0,10)

print(matrix1)
print(matrix1.countMatrix())
print(matrix2)
print(matrix2.countMatrix())
print(str(matrix3))
print(str(matrix2+matrix1))
print(str(matrix3.transposeMatrix()))
print(str(matrix4))
print(str(matrix4.transposeMatrix()))
print(str(matrix5))
print(matrix3>matrix4)