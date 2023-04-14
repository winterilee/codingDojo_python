# Assignment: Dojo Pets

# TODO 1. Create a Ninja class with the ninja attributes:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninjas:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
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


