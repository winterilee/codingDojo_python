# Assignment: Dojo Pets

# TODO 1. Create a Ninja class with the ninja attributes:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninjas:
    def __init__(self, first_name , last_name , treats , pet_food , pet_name, pet_type, pet_tricks, pet_sound):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.treats_inventory = 5
        self.pet_food = pet_food
        self.pet_food_inventory = 100
        self.pet = Pet(pet_name, pet_type, pet_tricks, pet_sound)
    
    def display_ninja(self):
        print(f"Ninja Name: {self.first_name} {self.last_name}\nPet Name: {self.pet.name}\nTreats: {self.treats} (Remaining amount: {self.treats_inventory})\nPet Food: {self.pet_food} (Remaining amount: {self.pet_food_inventory})")
        print("-" * 20)
        return self
    
    def walk(self):
        print(f"Walking {self.pet.name}.")
        return self
    
    def give_treat(self):
        if Ninjas.enough_treats(self.treats_inventory):
            print(f"Treating {self.pet.name} {self.treats}!")
            self.treats_inventory -= 1
        else:
            print(f"Oh no!!! You need more treats for your pet!")
        return self
    
    def feed(self):
        if Ninjas.enough_food(self.pet_food_inventory):
            print(f"Feeding {self.pet.name} {self.pet_food}!")
            self.pet_food_inventory -= 5
        else:
            print(f"Oh no!!! You need more pet food!")
        return self
    
    def bathe(self):
        print(f"Bathing {self.pet.name}.")
        return self
    
    @staticmethod
    def enough_treats(amount):
        if amount < 0:
            return False
        else:
            return True
    
    @staticmethod
    def enough_food(amount):
        if amount < 5:
            return False
        else:
            return True


# TODO 2. Create a Pet class with the pet attributes:
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Pet:
    def __init__(self, name , type , tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 100
    
    def sleep(self):
        self.energy += 25
        print(f"Current energy of {self.name}: {self.energy}")
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Current energy of {self.name}: {self.energy}")
        print(f"Current health of {self.name}: {self.health}")
        return self
    
    def play(self):
        self.health += 5
        print(f"Current health of {self.name}: {self.health}")
        return self
    
    def noise(self):
        print(self.sound)
        return self


ninja1 = Ninjas("Pine", "Apple", "Churu", "Purina", "Coconut", "Cat", "High Five", "meowwwww")
ninja2 = Ninjas("Passion", "Fruit", "Blue Buffalo", "Wellness", "Yogurt", "Dog", "Rollover", "woof woof")

ninja1.pet_food_inventory = 5
ninja1.feed().walk().bathe().feed().display_ninja()

ninja2.display_ninja().pet.eat().play().noise()