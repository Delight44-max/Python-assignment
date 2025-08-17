import unittest

from get_tuple import change_tuple_item


class TestNumbersFunction(unittest.TestCase):
    def test_that_change_tuple_item_function_exits(self):

        self.assertTrue(callable(change_tuple_item))



  


    def test_that_list_in_the_tuple_changed(self):
        tup = (1, [3, 4], 5)
        result = change_tuple_item(tup, 1, 99)

        self.assertNotEqual(result, (1, [99, 4], 5))


    
        

                   