import unittest 
from tuple_converter import tuple_to_list


class testTupleConvertFunction(unittest.TestCase):
    def test_that_tuple_to_list_function_exits(self):
        self.assertTrue(callable(tuple_to_list))