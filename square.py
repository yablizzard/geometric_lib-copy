import unittest

def area(a):
    '''Принимает длину стороны квадрата - число a, возвращает площадь этого квадрата'''
    return a * a

def perimeter(a):
    '''Принимает длину стороны квадрата - число a, возвращает периметр этого квадрата'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area_01(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_general_1_area_02(self):
        res = area(9)
        self.assertEqual(res, 81)
    
    def test_general_2_area_03(self):
        res = area(13)
        self.assertEqual(res, 169)
    
    def test_general_3_area_04(self):
        res = area(98467)
        self.assertEqual(res, 9695750089)
    
    def test_zero_perimeter_05(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_general_1_perimeter_06(self):
        res = perimeter(9)
        self.assertEqual(res, 36)
    
    def test_general_2_perimeter_07(self):
        res = perimeter(13)
        self.assertEqual(res, 52)
    
    def test_general_1_perimeter_8(self):
        res = perimeter(98467)
        self.assertEqual(res, 393868)