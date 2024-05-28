# test_unit_converter.py
import unittest
from unit_converter import UnitConverter

class TestUnitConverter(unittest.TestCase):
    def setUp(self):
        self.converter = UnitConverter()

    def test_meters_to_feet(self):
        self.assertAlmostEqual(self.converter.meters_to_feet(1), 3.28084)
        self.assertAlmostEqual(self.converter.meters_to_feet(2), 6.56168)
        self.assertAlmostEqual(self.converter.meters_to_feet(0), 0)

    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(self.converter.kilograms_to_pounds(1), 2.20462)
        self.assertAlmostEqual(self.converter.kilograms_to_pounds(2), 4.40924)
        self.assertAlmostEqual(self.converter.kilograms_to_pounds(0), 0)

    def test_volume_to_gallons(self):
        self.assertAlmostEqual(self.converter.volume_to_gallons(1), 0.264172)
        self.assertAlmostEqual(self.converter.volume_to_gallons(2), 0.528344)
        self.assertAlmostEqual(self.converter.volume_to_gallons(0), 0)

    def test_convert_between_systems(self):
        self.assertAlmostEqual(self.converter.convert_between_systems(1, 'meters', 'feet'), 3.28084)
        self.assertAlmostEqual(self.converter.convert_between_systems(1, 'kilograms', 'pounds'), 2.20462)
        # Add more test cases for different conversions

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            self.converter.convert_between_systems(1, 'invalid', 'feet')

if __name__ == '__main__':
    unittest.main()
