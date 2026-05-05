def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
def convert_temperature():
    print("=" * 45)
    print("       TEMPERATURE CONVERTER")
    print("=" * 45)
    print("Select the input scale:")
    print("  1. Celsius")
    print("  2. Fahrenheit")
    print("  3. Kelvin")
    print("  4. Exit")
    print("-" * 45)
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")
            continue
        try:
            value = float(input("Enter the temperature value: "))
        except ValueError:
            print("Invalid number. Please try again.\n")
            continue
        print()
        if choice == "1":
            if value < -273.15:
                print("Error: Temperature below absolute zero!\n")
                continue
            print(f"  {value}°C  =  {celsius_to_fahrenheit(value):.2f} °F")
            print(f"  {value}°C  =  {celsius_to_kelvin(value):.2f} K")
        elif choice == "2":
            if value < -459.67:
                print("Error: Temperature below absolute zero!\n")
                continue
            print(f"  {value}°F  =  {fahrenheit_to_celsius(value):.2f} °C")
            print(f"  {value}°F  =  {fahrenheit_to_kelvin(value):.2f} K")
        elif choice == "3":
            if value < 0:
                print("Error: Kelvin cannot be negative!\n")
                continue
            print(f"  {value} K  =  {kelvin_to_celsius(value):.2f} °C")
            print(f"  {value} K  =  {kelvin_to_fahrenheit(value):.2f} °F")
        print()
        again = input("Convert another? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break
        print()
if __name__ == "__main__":
    convert_temperature()
