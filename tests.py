import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit


class ConversionsTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        kelvin = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertAlmostEqual(kelvin, expected, 2)

    def test_convertCelsiusToKelvin_zero(self):
        kelvin = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(kelvin, expected, 2)

    def test_convertCelsiusToKelvin_negative(self):
        kelvin = convertCelsiusToKelvin(-273.15)
        expected = 0.0
        self.assertAlmostEqual(kelvin, expected, 2)

    def test_convertCelsiusToFahrenheit(self):
        fahrenheit = convertCelsiusToFahrenheit(300)
        expected = 572.0
        self.assertAlmostEqual(fahrenheit, expected, 2)

    def test_convertCelsiusToFahrenheit_zero(self):
        fahrenheit = convertCelsiusToFahrenheit(0)
        expected = 32.0
        self.assertAlmostEqual(fahrenheit, expected, 2)

    def test_convertCelsiusToFahrenheit_negative(self):
        fahrenheit = convertCelsiusToFahrenheit(-40)
        expected = -40.0
        self.assertAlmostEqual(fahrenheit, expected, 2)



if __name__ == '__main__':
    unittest.main()