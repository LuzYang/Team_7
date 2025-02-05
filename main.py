from entities import Player, NPC, Object

def interact_with_all(entities):
    for entity in entities:
        entity.interact()
        print()

def main():
    entities = []

    while True:
        print("\n1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            name = input("Name: ")
            choice = input("Type (1-Player, 2-NPC, 3-Object): ")
            
            if choice == "1":
                entities.append(Player(name, (0, 0, 0), 100))
            elif choice == "2":
                entities.append(NPC(name, (0, 0, 0)))
            elif choice == "3":
                entities.append(Object(name, (0, 0, 0)))
                
        elif choice == "2":
            interact_with_all(entities)
        elif choice == "3":
            break

if __name__ == "__main__":
    main()