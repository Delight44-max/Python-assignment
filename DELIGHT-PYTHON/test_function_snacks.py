import unittest
import function_snacks

class Testfunctionsnacks(unittest.TestCase):

    def test_divisible_by_5(self):
        self.assertEqual(function_snacks.divide(25), 5.0)

    def test_not_divisible_by_5(self):
        self.assertEqual(function_snacks.divide(7), 2)

    def test_raises_error_on_string(self):
        with self.assertRaises(ValueError):
            function_snacks.divide("delight")

    def test_works_with_float_input(self):
        self.assertEqual(function_snacks.divide(10.0), 3.16)