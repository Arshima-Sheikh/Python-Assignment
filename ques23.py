def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get user input
choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()
temperature = float(input("Enter the temperature to convert: "))

if choice == 'C':
    converted_temp = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
elif choice == 'F':
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid input. Please enter 'C' or 'F'.")
