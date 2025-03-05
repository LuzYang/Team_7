class SmartDevice:
    def __init__(self,deviceName):
        self.deviceName=deviceName
        self.status="off"
  
        
class SmartLight(SmartDevice):
    def __init__(self,deviceName,brightness=50):
        super().__init__(deviceName)
        self.brightness=brightness

    def operate(self):
        if self.status == "off":
            self.status = "on"
            print(f"{self.deviceName} is now on. Brightness: {self.brightness}%")
        else:
            self.status = "off"
            print(f"{self.deviceName} is now off")

class SmartThermostat(SmartDevice):
    def __init__(self,deviceName,temperature=22):
        super().__init__(deviceName)
        self.temperature=temperature
    def operate(self):
        if self.status == "off": 
            self.status = "on"
            print(f"{self.deviceName} is now on. Temperature: {self.temperature}°C")
        else:
            self.status = "off"
            print(f"{self.deviceName} is now off")


class SmartLock(SmartDevice):
    def __init__(self,deviceName):
        super().__init__(deviceName)
        self.status="locked"
    def operate(self):
        if self.status == "locked":
            self.status = "unlocked"
            print(f"{self.deviceName} UNLOCKED")
        else:
            self.tatus = "locked"
            print(f"{self.deviceName} LOCKED")
