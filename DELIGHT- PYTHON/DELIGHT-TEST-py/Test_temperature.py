import unittest
import temperature

class TestTemperatureAdvisoryFunction(unittest.TestCase):

    def test_celsius_above_threshold(self):
        result = temperature.temperature_advisory(35, 'C', 30)
        self.assertEqual(result, "Heat alert")

    def test_celsius_below_threshold(self):
        result = temperature.temperature_advisory(25, 'C', 30)
        self.assertEqual(result, "Cold advisory")

    def test_fahrenheit_above_threshold(self):
        result = temperature.temperature_advisory(100, 'F', 95)
        self.assertEqual(result, "Heat alert")

    def test_fahrenheit_below_threshold(self):
        result = temperature.temperature_advisory(80, 'F', 90)
        self.assertEqual(result, "Cold advisory")

    def test_celsius_equal_to_threshold(self):
        result = temperature.temperature_advisory(30, 'C', 30)
        self.assertEqual(result, "Heat alert")
   
    
        





















