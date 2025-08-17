import unittest
from Tuple import new_tuple


class TestTupleFunction(unittest.TestCase):
    def test_function_exits(self):

        self.assertTrue(callable(new_tuple))



    def test_that_tuple_numbers_exit(self):
        numbers = (1, 2, 3)
        result = new_tuple(numbers, 4)
        
        self.assertEqual(result, (1, 2, 3, 4))


    def test_tuple_number_not_equal(self):
        numbers = (1, 2, 3)
        result = new_tuple(numbers, 4)

        self.assertNotEqual(result, (1, 2, 3))

