# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada

# Create another user called user_2!
user_2 = User()

# Print user_ada's last name.
print(user_ada.last_name)

# Print user_2's last name. (Yes, they should be the same)
print(user_2.last_name)

# Run the code, pause, go back and step through one line at a time
# What do you notice about the order it runs in?
# Write down any other questions you have.
# does it have the same age as well?
print(user_2.age)

# Sensei Exercise: try just printing the variable, user_ada.
print(user_ada)
#   What prints to the terminal?
# pointers?


# declare a class and give it name Shoe
class Shoe:		
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True

skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type) # Classic Sk8-Hi
print(dress_shoe.type)	# Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

# Ninja Challenges!
# Open this code on the Trace website to get a better view of all the variables and their attributes.
# Make a new instance of a shoe
toms_shoe = Shoe("Toms", "Slip-Ons", 54.95)
print(toms_shoe.type)
# Update the in_stock attribute to False
toms_shoe.in_stock = False
print(toms_shoe.in_stock)