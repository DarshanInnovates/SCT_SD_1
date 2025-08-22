# Temperature Converter between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


# Main Program
print("Temperature Converter")
print("Choose the input scale:")
print("1. Celsius (C)")
print("2. Fahrenheit (F)")
print("3. Kelvin (K)")

choice = int(input("Enter choice (1/2/3): "))
temp = float(input("Enter temperature value: "))

if choice == 1:  # Celsius input
    print(f"\nInput: {temp} °C")
    print(f"In Fahrenheit: {celsius_to_fahrenheit(temp):.2f} °F")
    print(f"In Kelvin: {celsius_to_kelvin(temp):.2f} K")

elif choice == 2:  # Fahrenheit input
    print(f"\nInput: {temp} °F")
    print(f"In Celsius: {fahrenheit_to_celsius(temp):.2f} °C")
    print(f"In Kelvin: {fahrenheit_to_kelvin(temp):.2f} K")

elif choice == 3:  # Kelvin input
    print(f"\nInput: {temp} K")
    print(f"In Celsius: {kelvin_to_celsius(temp):.2f} °C")
    print(f"In Fahrenheit: {kelvin_to_fahrenheit(temp):.2f} °F")

else:
    print("Invalid choice! Please run again.")
