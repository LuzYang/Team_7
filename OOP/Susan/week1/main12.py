import csv
import json
from cryptography.fernet import Fernet

class IoTDevice:
    def __init__(self, device_id, location, data):
        self.device_id = device_id
        self.location = location
        self.data = data

    def to_dict(self):
        return {"device_id": self.device_id, "location": self.location, "data": self.data}

    @classmethod
    def from_dict(cls, device_dict):
        return cls(device_dict['device_id'], device_dict['location'], device_dict['data'])

    def serialize(self):
        return json.dumps(self.to_dict())

    @classmethod
    def deserialize(cls, serialized_data):
        device_dict = json.loads(serialized_data)
        return cls.from_dict(device_dict)


# Derived classes for specific IoT devices
class TemperatureSensor(IoTDevice):
    def __init__(self, device_id, location, data, temperature_unit="C"):
        super().__init__(device_id, location, data)
        self.temperature_unit = temperature_unit

    def to_dict(self):
        data = super().to_dict()
        data["temperature_unit"] = self.temperature_unit
        return data

    @classmethod
    def from_dict(cls, device_dict):
        sensor = super().from_dict(device_dict)
        sensor.temperature_unit = device_dict.get("temperature_unit", "C")
        return sensor


class HumiditySensor(IoTDevice):
    def __init__(self, device_id, location, data, humidity_unit="%"):
        super().__init__(device_id, location, data)
        self.humidity_unit = humidity_unit

    def to_dict(self):
        data = super().to_dict()
        data["humidity_unit"] = self.humidity_unit
        return data

    @classmethod
    def from_dict(cls, device_dict):
        sensor = super().from_dict(device_dict)
        sensor.humidity_unit = device_dict.get("humidity_unit", "%")
        return sensor


class MotionSensor(IoTDevice):
    def __init__(self, device_id, location, data, motion_status="Inactive"):
        super().__init__(device_id, location, data)
        self.motion_status = motion_status

    def to_dict(self):
        data = super().to_dict()
        data["motion_status"] = self.motion_status
        return data

    @classmethod
    def from_dict(cls, device_dict):
        sensor = super().from_dict(device_dict)
        sensor.motion_status = device_dict.get("motion_status", "Inactive")
        return sensor


# Custom Encryption and Decryption
class EncryptionHandler:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt(data, key):
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data.encode())
        return encrypted

    @staticmethod
    def decrypt(encrypted_data, key):
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data).decode()
        return decrypted


# Menu-driven interface to interact with the user
class IoTDataPipeline:
    def __init__(self):
        self.devices = []
        self.key = EncryptionHandler.generate_key()

    def display_menu(self):
        print("\nMenu:")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")

    def add_device(self):
        print("\nChoose device type:")
        print("1 - Temperature Sensor")
        print("2 - Humidity Sensor")
        print("3 - Motion Sensor")
        
        try:
            choice = int(input("Enter choice: "))
            
            device_id = input("Enter Device ID: ")
            location = input("Enter Device Location: ")
            data = input("Enter Data: ")

            if choice == 1:
                temperature_unit = input("Enter Temperature Unit (C/F): ")
                self.devices.append(TemperatureSensor(device_id, location, data, temperature_unit))
                print("TemperatureSensor added.")
            elif choice == 2:
                humidity_unit = input("Enter Humidity Unit: ")
                self.devices.append(HumiditySensor(device_id, location, data, humidity_unit))
                print("HumiditySensor added.")
            elif choice == 3:
                motion_status = input("Enter Motion Status (Active/Inactive): ")
                self.devices.append(MotionSensor(device_id, location, data, motion_status))
                print("MotionSensor added.")
            else:
                print("Invalid device type!")
        except ValueError:
            print("Invalid input. Please enter valid data.")

    def serialize_data(self):
        try:
            if not self.devices:
                print("No devices to serialize!")
                return
            
            with open("iot_data.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["device_id", "location", "data", "device_type", "extra_info"])
                for device in self.devices:
                    if isinstance(device, TemperatureSensor):
                        writer.writerow([device.device_id, device.location, device.data, "TemperatureSensor", device.temperature_unit])
                    elif isinstance(device, HumiditySensor):
                        writer.writerow([device.device_id, device.location, device.data, "HumiditySensor", device.humidity_unit])
                    elif isinstance(device, MotionSensor):
                        writer.writerow([device.device_id, device.location, device.data, "MotionSensor", device.motion_status])
            print("Data serialized to iot_data.csv.")
        except Exception as e:
            print(f"Error serializing data: {e}")

    def deserialize_data(self):
        try:
            with open("iot_data.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    device_id, location, data, device_type, extra_info = row
                    if device_type == "TemperatureSensor":
                        self.devices.append(TemperatureSensor(device_id, location, data, extra_info))
                    elif device_type == "HumiditySensor":
                        self.devices.append(HumiditySensor(device_id, location, data, extra_info))
                    elif device_type == "MotionSensor":
                        self.devices.append(MotionSensor(device_id, location, data, extra_info))
            print("Data deserialized from iot_data.csv.")
        except Exception as e:
            print(f"Error deserializing data: {e}")

    def encrypt_data(self):
        try:
            serialized_data = [device.serialize() for device in self.devices]
            encrypted_data = [EncryptionHandler.encrypt(data, self.key) for data in serialized_data]
            with open("encrypted_data.txt", "wb") as file:
                for encrypted in encrypted_data:
                    file.write(encrypted + b"\n")
            print("Data encrypted and saved to encrypted_data.txt.")
        except Exception as e:
            print(f"Error encrypting data: {e}")

    def decrypt_data(self):
        try:
            with open("encrypted_data.txt", "rb") as file:
                encrypted_data = file.readlines()
            decrypted_data = [EncryptionHandler.decrypt(data.strip(), self.key) for data in encrypted_data]
            for data in decrypted_data:
                print("Decrypted data:", data)
        except Exception as e:
            print(f"Error decrypting data: {e}")


def main():
    pipeline = IoTDataPipeline()

    while True:
        pipeline.display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                pipeline.add_device()
            elif choice == 2:
                pipeline.serialize_data()
            elif choice == 3:
                pipeline.deserialize_data()
            elif choice == 4:
                pipeline.encrypt_data()
            elif choice == 5:
                pipeline.decrypt_data()
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
