# Define Global Conversion Factors at the top of the script
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global factor.
    """
    # Formula: (F - 32) * factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global factor.
    """
    # Formula: (C * factor) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    try:
        # Prompt for temperature and convert to float
        temp_str = input("Enter the temperature to convert: ")
        temperature = float(temp_str)
    except ValueError:
        # Handle cases where the input is not a numeric value
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Prompt for the unit and standardize the input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # If Fahrenheit, convert to Celsius and display
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == 'C':
        # If Celsius, convert to Fahrenheit and display
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()