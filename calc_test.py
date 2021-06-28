# Let's import unittest and pytest as these are the dependencies
import unittest
import pytest

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    # Assertions to write our test cases
    # We will use our basic calc example to write the tests first then the code

    def test_add(self):
        # Naming conventions is essential
        self.assertEqual(self.calc.add(3, 2), 5) # if 3 + 2 = 5 is True test would pass
        # return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1) # 3 - 2 = 1

    def test_multi(self):
        self.assertEqual(self.calc.multi(2, 2), 4) # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2) # 6 / 3 = 2