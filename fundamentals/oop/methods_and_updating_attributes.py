class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie


class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = round(self.price * (1-percent_off), 2)
    
    # Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = round(self.price + tax, 2)
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")

# Create two shoe instances
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
        
# The skater shoes go on sale by 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2)
skater_shoe.on_sale_by_percent(0.2)
print(skater_shoe.price)
        
# The dress shoes go on sale by 10% reduction:
# dress_shoe.price = dress_shoe.price * (1 - 0.1)
dress_shoe.on_sale_by_percent(0.1)
print(dress_shoe.price)
        
# The skater shoes go on sale AGAIN by another 10%:
# skater_shoe.price = skater_shoe.price * (1 - 0.1)
skater_shoe.on_sale_by_percent(0.1)
print(skater_shoe.price)

# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)


toms_shoe = Shoe("Toms", "Slip-Ons", 54.95)
toms_shoe.on_sale_by_percent(0.1)
print(toms_shoe.price)
print(toms_shoe.total_with_tax(0.07))
toms_shoe.cut_price_by(5)
print(toms_shoe.price)
print(toms_shoe.total_with_tax(0.07))