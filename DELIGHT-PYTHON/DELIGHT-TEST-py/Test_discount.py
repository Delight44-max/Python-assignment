import unittest
import discount 

class TestDiscountFunction(unittest.TestCase):

    def test_save10_discount(self):
        result = discount.apply_discount("Shoes", 100, "SAVE10")
        self.assertEqual(result, 90.0)

    def test_half_off_discount(self):
        result = discount.apply_discount("Jacket", 200, "HALFOFF")
        self.assertEqual(result, 100.0)

    def test_no_discount_code(self):
        result = discount.apply_discount("Bag", 50, "NONE")
        self.assertEqual(result, 50.0)

    def test_lowercase_code(self):
        result = discount.apply_discount("Gloves", 80, "save10")
        self.assertEqual(result, 72.0)

    def test_invalid_code(self):
        result = discount.apply_discount("Socks", 60, "random")
        self.assertEqual(result, 60.0)