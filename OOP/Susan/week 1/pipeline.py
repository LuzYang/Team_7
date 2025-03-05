import csv
import json
import os
from main1 import TemperatureSensor, HumiditySensor, MotionSensor
from encryption import EncryptionHandler

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
            device_id = input("Enter Device ID: ").strip()
            location = input("Enter Device Location: ").strip()
            data = input("Enter Data: ").strip()

            if choice == 1:
                temperature_unit = input("Enter Temperature Unit (C/F): ").strip()
                self.devices.append(TemperatureSensor(device_id, location, data, temperature_unit))
                print("TemperatureSensor added.")
            elif choice == 2:
                humidity_unit = input("Enter Humidity Unit: ").strip()
                self.devices.append(HumiditySensor(device_id, location, data, humidity_unit))
                print("HumiditySensor added.")
            elif choice == 3:
                motion_status = input("Enter Motion Status (Active/Inactive): ").strip()
                self.devices.append(MotionSensor(device_id, location, data, motion_status))
                print("MotionSensor added.")
            else:
                print("Invalid device type!")
        except ValueError:
            print("Invalid input. Please enter valid data.")

    def serialize_data(self):
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

    def deserialize_data(self):
        if not os.path.exists("iot_data.csv"):
            print("No data file found to deserialize!")
            return

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

    def encrypt_data(self):
        if not self.devices:
            print("No devices to encrypt!")
            return

        serialized_data = [device.serialize() for device in self.devices]
        encrypted_data = [EncryptionHandler.encrypt(data, self.key) for data in serialized_data]

        with open("encrypted_data.txt", "wb") as file:
            for encrypted in encrypted_data:
                file.write(encrypted + b"\n")

        print("Data encrypted and saved to encrypted_data.txt.")

    def decrypt_data(self):
        if not os.path.exists("encrypted_data.txt"):
            print("No encrypted file found to decrypt!")
            return

        with open("encrypted_data.txt", "rb") as file:
            encrypted_data = file.readlines()
        decrypted_data = [EncryptionHandler.decrypt(data.strip(), self.key) for data in encrypted_data]

        for data in decrypted_data:
            print("Decrypted data:", data)
