class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Player(Entity):
    def __init__(self, name, position, health):
        super().__init__(name, position)
        self.health = health

    def interact(self):
        print()
        print(f"Player {self.name} with {self.health} health")

class NPC(Entity):
    def interact(self):
        print()
        print(f"NPC {self.name} says: Hello!")

class Object(Entity):
    def interact(self):
        print()
        print(f"Object {self.name} can be picked up")