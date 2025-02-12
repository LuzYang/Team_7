from game_characters import Warrior, Mage, Archer

def simulate_battle(characters):
    for char in characters:
        print(f"{char.__class__.__name__}: {char.attack()}")
        print(f"{char.__class__.__name__}: {char.defend()}")

def main():
    print("Program starting.")
    characters = []
    while True:
        print("\nMenu:")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            print("\n1 - Warrior\n2 - Mage\n3 - Archer")
            char_choice = input("Choose character: ")
            
            if char_choice == '1':
                characters.append(Warrior())
                
                print("Warrior created!")
            elif char_choice == '2':
                characters.append(Mage())
                
                print("Mage created!")
            elif char_choice == '3':
                characters.append(Archer())
                
                print("Archer created!")
            else:
                print("Invalid choice.")

        elif choice == '2':
            if characters:
                print("\nSimulating Battle...")
                simulate_battle(characters)
                characters.clear()
            else:
                print("No characters created yet.")

        elif choice == '0':
            print("\nProgram ending.")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
