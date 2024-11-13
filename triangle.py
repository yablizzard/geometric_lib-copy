import unittest

def area(a, h):
    '''Принимает сторону и проведённую к этой стороне высоту трекгольника - числа a и h, возвращает площадь этого треугольника'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает стороны треугольника - числа a, b и c, возвращает периметр этого треугольника'''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_area_01(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_square_area_02(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
    
    def test_general_1_area_03(self):
        res = area(9, 16)
        self.assertEqual(res, 72)
    
    def test_general_2_area_04(self):
        res = area(13, 8)
        self.assertEqual(res, 52)
    
    def test_general_3_area_05(self):
        res = area(98467, 73863)
        self.assertEqual(res, 3636534010.5)
    
    def test_zero_perimeter_06(self):
        res = perimeter(10, 0, 20)
        self.assertEqual(res, 30)
    
    def test_square_perimeter_07(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
    
    def test_general_1_perimeter_08(self):
        res = perimeter(9, 16, 9)
        self.assertEqual(res, 34)
    
    def test_general_2_perimeter_09(self):
        res = perimeter(13, 8, 7)
        self.assertEqual(res, 28)
    
    def test_general_1_perimeter_10(self):
        res = perimeter(98467, 73863, 36722)
        self.assertEqual(res, 209052)