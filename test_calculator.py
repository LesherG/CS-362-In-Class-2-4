import unittest
import calculator

class TestCalculatorMethods(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(2,2), 4)
        self.assertEqual(calculator.add(-3,2), -1)
        self.assertEqual(calculator.add(-2,-25), -27)
        self.assertEqual(calculator.add(0,0), 0)
        self.assertEqual(calculator.add(0,-3), -3)
        
    def test_subtract(self):
        self.assertEqual(calculator.subtract(4,2), 2)
        self.assertEqual(calculator.subtract(2,0), 2)
        self.assertEqual(calculator.subtract(-3,-6), 3)
        self.assertEqual(calculator.subtract(7,-28), 35)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2,2), 4)
        self.assertEqual(calculator.multiply(7,2), 14)
        self.assertEqual(calculator.multiply(90,10), 900)
        self.assertEqual(calculator.multiply(2,-2), -4)
        self.assertEqual(calculator.multiply(-2,-2), 4)
        
    def test_divide(self):
        self.assertEqual(calculator.divide(4,2), 2)
        self.assertEqual(calculator.divide(1,2), .5)
        self.assertEqual(calculator.divide(1,-4), -.25)
        self.assertEqual(calculator.divide(51,17), 3)
        
        
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(2,0)
            calculator.divide(0,0)
        
if __name__ == '__main__':
    unittest.main()

