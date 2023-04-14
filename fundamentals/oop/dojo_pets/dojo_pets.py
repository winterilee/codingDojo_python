# Assignment: Dojo Pets

# TODO 1. Create a Ninja class with the ninja attributes:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninjas:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print(f"Walking {self.pet}.")
    
    def feed(self):
        print(f"Feeding {self.pet} {self.pet_food}!")
    
    def bathe(self):
        print(f"Bathing {self.pet}")


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
    
    def eat(self):
        self.energy += 5
        self.health += 10
    
    def play(self):
        self.health += 5
    
    def noise(self):
        print(self.sound)


