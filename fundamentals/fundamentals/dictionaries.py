#literal notation
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# List Syntax:
# my_list[0] = 4

# Dictionary Syntax:
# my_dict["some_string"] = some_value


# Challenge yourself!

person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
# Create another person dictionary called person_2 and print it to the terminal
person_2 = {"first_name": "Winter", "last_name": "Lee", "favorite_color": "Cerulean", "favorite_food": "pasta"}

print(person_2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# Add 2 key-value pairs to this dictionary.
capitals["sko"] = "Seoul"
capitals["can"] = "Ottawa"

# print the capitals dictionary to see how it changed!

print(capitals)


# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"

# Changes person's "last_name" value to "Bobada"
person["last_name"] = "Bobada"
print(person)

if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")


countries_so_far = {"Mexico": 1, "Morocco": 1}
new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# To add Albania to the list
countries_so_far["Albania"] = 1
# To add 1 to the Mexico tally
countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# your code here to finish updating your travel log!
countries_so_far["Togo"] = 1
countries_so_far["Morocco"] += 1
print(countries_so_far)


# Accessing Values
print(person["first_name"])
full_name = person["first_name"] + " " + person["last_name"]
print(full_name)


# Removing Values
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything
print(capitals)