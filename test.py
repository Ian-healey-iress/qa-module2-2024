# unittest 
# part of standard library.
# test cases by subclassing unittest.testCase. 
# can have multiple test methods per test case. 
# assertion methods 
# built on j-unit
# looks for test_..... methods and test_.... modules.
# python3 -m unittest test_calculator.py 

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calculator_class_exists(self):
        calc = Calculator() # attempt to make an object of the Calculator class.
        self.assertIsInstance(calc, Calculator) # Test if calc is instance of Calculator.

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: Inputs must be numeric"):
            calc.add("a", 5)

    def test_add_method_outputs_numeric(self):
        calc = Calculator()
        self.assertIsInstance(calc.add(1,2), (int, float))
    
    def test_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(1000, 2000), 3000)

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, 0), 0)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 5), 2)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(1, 0)

    @unittest.skip("skipping...") 
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "skipping also")
    def test_skip_if(self):
        pass

if __name__ == '__main__':
    unittest.main()
