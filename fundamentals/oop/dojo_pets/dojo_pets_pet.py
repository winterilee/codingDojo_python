
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


# TODO NINJA BONUS: Use Modules to separate out the classes into different files.