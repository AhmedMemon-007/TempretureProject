# unit_converter.py

class UnitConverter:
    def __init__(self):
        pass

    def meters_to_feet(self, meters):
        return meters * 3.28084

    def kilograms_to_pounds(self, kilograms):
        return kilograms * 2.20462

    def volume_to_gallons(self, volume):
        return volume * 0.264172

    def convert_between_systems(self, value, from_unit, to_unit):
        if from_unit == 'meters' and to_unit == 'feet':
            return self.meters_to_feet(value)
        elif from_unit == 'kilograms' and to_unit == 'pounds':
            return self.kilograms_to_pounds(value)
        # Add more conversion cases as needed
        else:
            raise ValueError("Invalid conversion")

