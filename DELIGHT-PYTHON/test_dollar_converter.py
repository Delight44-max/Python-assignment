import unittest
import dollar_converter

class TestDollarConverterFunction(unittest.TestCase):
    def test_that_dollar_converter_function_exists(self):
        result = dollar_converter.exchange(500)
        self.assertIsNotNone(result)

    def test_that_result_function_raises_validation_with_incorrect_value(self):
        with self.assertRaises(ValueError):
            dollar_converter.exchange("jahd")