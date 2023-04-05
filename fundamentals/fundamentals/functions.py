def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)


# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first_name, last_name):
    # your code here!
    return first_name + " " + last_name

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau

# Challenge 2: 
#   Call the function again using your own name and print the results!
my_name = full_name("Winter", "Lee")
print(my_name)