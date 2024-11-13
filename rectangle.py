import unittest

def area(a, b):
    '''Принимает стороны прямоугольника - числа a и b, возвращает площадь этого прямоугольника'''
    return a * b

def perimeter(a, b):
    '''Принимает стороны прямоугольника - числа a и b, возвращает периметр этого прямоугольника'''
    return 2 * a + 2 * b

class RectangleTestCase(unittest.TestCase):
    def test_zero_area_01(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_area_02(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_general_1_area_03(self):
        res = area(9, 16)
        self.assertEqual(res, 144)
    
    def test_general_2_area_04(self):
        res = area(13, 8)
        self.assertEqual(res, 104)
    
    def test_general_3_area_05(self):
        res = area(98467, 73863)
        self.assertEqual(res, 7273068021)
    
    def test_zero_perimeter_06(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_square_perimeter_07(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_general_1_perimeter_08(self):
        res = perimeter(9, 16)
        self.assertEqual(res, 50)
    
    def test_general_2_perimeter_09(self):
        res = perimeter(13, 8)
        self.assertEqual(res, 42)
    
    def test_general_1_perimeter_10(self):
        res = perimeter(98467, 73863)
        self.assertEqual(res, 344660)