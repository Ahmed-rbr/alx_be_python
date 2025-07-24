FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


temperature = int(input('Enter the temperature to convert: '))
temperature_type = input(
    'Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()

match temperature_type:
    case 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    case 'C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    case '_':
        print('something Went wrong')
