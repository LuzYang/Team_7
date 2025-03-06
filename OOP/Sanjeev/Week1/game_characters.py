from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass  # Placeholder for the attack logic that will be defined in subclasses

    @abstractmethod
    def defend(self):
        pass  # Placeholder for the defend logic that will be defined in subclasses

class Warrior(GameCharacter):
    def attack(self):
        return "Warrior attacks with a sword!"
    
    def defend(self):
        return "Warrior defends with a shield!"

class Mage(GameCharacter):
    def attack(self):
        return "Mage casts a fireball!"
    
    def defend(self):
        return "Mage defends with a magic barrier!"

class Archer(GameCharacter):
    def attack(self):
        return "Archer shoots an arrow!"
    
    def defend(self):
        return "Archer dodges the attack!"