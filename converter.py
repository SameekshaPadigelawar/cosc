import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Set up the CLI parser
parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit.")

# Add argument for temperature value
parser.add_argument("temperature", type=float, help="Temperature value to convert")

# Add mutually exclusive group for conversion direction
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--c2f", action="store_true", help="Convert Celsius to Fahrenheit")
group.add_argument("-f", "--f2c", action="store_true", help="Convert Fahrenheit to Celsius")

# Parse the command-line arguments
args = parser.parse_args()

# Perform conversion
if args.c2f:
    result = celsius_to_fahrenheit(args.temperature)
    print(f"{args.temperature}°C = {result:.2f}°F")
elif args.f2c:
    result = fahrenheit_to_celsius(args.temperature)
    print(f"{args.temperature}°F = {result:.2f}°C")
