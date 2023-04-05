num1 = 42   # variable declaration, initialize number(integer)
num2 = 2.3  # variable declaration, initialize number(float)
boolean = True  # variable declaration, initialize Boolean
string = 'Hello World'  # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration, initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana')   # variable declaration, initialize Tuples
print(type(fruit))  # log statement, type check
print(pizza_toppings[1])   # log statement, access value 
pizza_toppings.append('Mushrooms')  # add value
print(person['name'])   # log statement, access value
person['name'] = 'George'   # change value
person['eye_color'] = 'blue'    # add value
print(fruit[2]) # log statement

if num1 > 45:   # conditional if
    print("It's greater")   # log statement
else:   # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if, length check
    print("It's a short word!") # log statement
elif len(string) > 15:  # conditional else if, length check
    print("It's a long word!")  # log statement
else:   # conditional else
    print("Just right!")    # log statement

for x in range(5):  # for loop, stop at 5
    print(x)    # log statement
for x in range(2,5):    # for loop, start at 2, stop at 5
    print(x)    # log statement
for x in range(2,10,3): # for loop, start at 2, stop at 10, increment by 3
    print(x)    # log statement
x = 0   # variable declaration, initialize number(integer)
while(x < 5):   # while loop, conditional less than 5
    print(x)    # log variable
    x += 1  # increment by 1

pizza_toppings.pop()    # delete value
pizza_toppings.pop(1)   # delete value

print(person)   # log variable
person.pop('eye_color') # delete value
print(person)   # log variable

for topping in pizza_toppings:  # for loop
    if topping == 'Pepperoni':  # conditional if
        continue    # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if, IndexError: list index out of range
        break   # break

def print_hello_ten_times():    # function
    for num in range(10):   # for loop, stop at 10, NameError: num is not defined
        print('Hello')  # log statement

print_hello_ten_times() # execute function

def print_hello_x_times(x): # function, parameter x
    for num in range(x):    # for loop, stop at x, NameError: num is not defined
        print('Hello')  # log statement

print_hello_x_times(4)  # execute function, argument 4

def print_hello_x_or_ten_times(x = 10): # function, parameter x = 10
    for num in range(x):    # for loop, stop at x, NameError: num is not defined
        print('Hello')  #log statement

print_hello_x_or_ten_times()    # execute function
print_hello_x_or_ten_times(4)   # execute function, argument 4


"""
Bonus section
"""
    # multiline comment

# print(num3)   # NameError: num3 is not defined
# num3 = 72 # variable declaration, initialize number(integer)
# fruit[0] = 'cranberry'    # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    # KeyError: 'favorite_team" doesn't exist in the Dictionary
# print(pizza_toppings[7])  # IndexError: list index out of range
#   print(boolean)  # NameError: name boolean is not defined
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  # AttributeError: 'tuple' object has no attribute 'pop'