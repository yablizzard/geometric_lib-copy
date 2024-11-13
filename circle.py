import math
import unittest

def area(r):
    '''Принимает радиус круга - число r, возвращает площадь этого круга'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает радиус круга - число r, возвращает периметр этого круга'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area_01(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_general_1_area_02(self):
        res = area(9)
        self.assertEqual(res, math.pi * 81)
    
    def test_general_2_area_03(self):
        res = area(13)
        self.assertEqual(res, math.pi * 169)
    
    def test_general_3_area_04(self):
        res = area(98467)
        self.assertEqual(res, math.pi * 9695750089)
    
    def test_zero_perimeter_05(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_general_1_perimeter_06(self):
        res = perimeter(9)
        self.assertEqual(res, math.pi * 18)
    
    def test_general_2_perimeter_07(self):
        res = perimeter(13)
        self.assertEqual(res, math.pi * 26)
    
    def test_general_1_perimeter_8(self):
        res = perimeter(98467)
        self.assertEqual(res, math.pi * 196934)