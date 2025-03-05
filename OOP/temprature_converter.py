class TemperatureConverter:
    def __init__(self, temp: float = 0.0):
        if temp < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self.__temperature = temp

    def setTemperature(self, temp: float) -> None:
        if temp < -273.15:
            print("Error: Temperature cannot be below absolute zero.")
        else:
            self.__temperature = temp

    def toFahrenheit(self) -> float:
        return (self.__temperature * 9/5) + 32

    def toKelvin(self) -> float:
        return self.__temperature + 273.15
