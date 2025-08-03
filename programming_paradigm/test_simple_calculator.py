import unittest
from simple_calculator import SimpleCalculator

class TestTestSimpleCalculatorlass(unittest.TestCase):
    """Test Cases For Various Scenarios"""
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-1,-1),-2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(1,-1), 2)
        self.assertEqual(self.calc.subtract(-1,1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,2), 6)
        self.assertEqual(self.calc.multiply(-3,-2), 6)
        self.assertEqual(self.calc.multiply(3,-2), -6)
        self.assertEqual(self.calc.multiply(-3,2), -6)
        self.assertEqual(self.calc.multiply(-3,0), 0)
        self.assertEqual(self.calc.multiply(0,2), 0)
    
    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(6.0,2.0), 3.0)
        self.assertAlmostEqual(self.calc.divide(6.0,0), ZeroDivisionError)