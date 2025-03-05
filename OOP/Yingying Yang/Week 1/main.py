from smartdevice import SmartDevice,SmartLight,SmartLock,SmartThermostat
def add_smart_device(devices):
    print("\n=== Add Smart Device ===")
    print("1. Smart Light")
    print("2. Smart Thermostat")
    print("3. Smart Lock")
    try:
        device_type = int(input("Choose device type (1-3): "))
        device_name = input("Enter device name: ")

        if device_type == 1:
            brightness = int(input("Enter brightness (0-100): "))
            device = SmartLight(device_name, brightness)
        elif device_type == 2:
            temperature = float(input("Enter temperature (16-30): "))
            device = SmartThermostat(device_name, temperature)
        elif device_type == 3:
            device = SmartLock(device_name)
        else:
            print("Invalid device type!")
            return devices

        devices.append(device)
        print(f"{device_name} added successfully!")
        return devices

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return devices

def operate_devices(devices):
    if not devices:
        print("No devices available. Add a device first.")
        return

    print("\n=== Available Devices ===")
    for i, device in enumerate(devices, 1):
        print(f"{i}. {device.deviceName}")

    try:
        choice = int(input("Select device to operate (enter number): ")) - 1
        
        if 0 <= choice <len(devices):
            devices[choice].operate()
        else:
            print("Invalid device selection!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    devices = []
    
    while True:
        print("\n=== Smart Home System ===")
        print("1. Add Smart Device")
        print("2. Operate Devices")
        print("0. Exit")
        
        try:
            menu_choice = int(input("Enter your choice: "))
            
            if menu_choice == 1:
                devices = add_smart_device(devices)
            elif menu_choice == 2:
                operate_devices(devices)
            elif menu_choice == 0:
                print("Exiting Smart Home System...")
                break
            else:
                print("Invalid choice. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

