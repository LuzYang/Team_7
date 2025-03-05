from sqlite3 import converters
from temprature_converter import TemperatureConverter


class main():
    def __init__(self):
        pass
    print("Program starting.")
    print("Initializing temperature converter...")
    converters = TemperatureConverter()
    print("Temperature converter initialized.\n")

    while True:
        print("Options:")
        print("1) Set temperature (in Celsius)")
        print("2) Convert to Celsius")
        print("3) Convert to Fahrenheit")
        print("4) Convert to Kelvin")
        print("0) Exit program")
        choice = input("Choice: ")

        if choice == '1':
            try:
                temp = float(input("Enter temperature in Celsius: "))
                converters.setTemperature(temp)
                print(f"Temperature set to {temp}°C.\n")
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")

        elif choice == '2':
            print(f"Temperature in Celsius: {converters.toCelsius():.2f}°C\n")

        elif choice == '3':
            print(
                f"Temperature in Fahrenheit: {converters.toFahrenheit():.2f}°F\n")

        elif choice == '4':
            print(f"Temperature in Kelvin: {converters.toKelvin():.2f} K\n")

        elif choice == '0':
            print("Program ending. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# # Run the program
if __name__ == "__main__":
    main()

