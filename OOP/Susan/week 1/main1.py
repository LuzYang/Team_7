from pipeline import IoTDataPipeline

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
