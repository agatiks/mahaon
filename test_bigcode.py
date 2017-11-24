#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Ученик
#
# Created:     22.11.2017
# Copyright:   (c) Ученик 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from bigcode import Matrix
matrixtest=Matrix(2, [[3,4],[5,4]])
matrixtest1=Matrix(2, [[4,4],[5,5]])
class TestBigcode(unittest.TestCase):

    def setUp(self):
        print('setUp перед!')

    def tearDown(self):
        print('tearDown после!')

    def test_TableMatrix(self):
        print('test' + str(matrixtest))
        self.assertEqual(str(matrixtest), "[3, 4]\n[5, 4]\n")

    def test_Diagonal(self):
        self.assertEqual(matrixtest.countMatrix(), "7")

    def test_Transpose(self):
        self.assertEqual(matrixtest.transposeMatrix(), "[[5, 3], [4, 4]]")

    def test_CompareSumms(self,other):
        self.assertEqual(matrixtest>matrixtest1, False)

    def test_SummMatrix(self,other):
        self.assertEqual(matrixtest+matrixtest1, [[7,8],[10,9]])


if __name__ == '__main__':
   unittest.main()