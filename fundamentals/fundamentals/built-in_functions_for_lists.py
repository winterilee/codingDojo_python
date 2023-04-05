my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
# 3


my_list = [1,5,2,8,4]
my_list.pop()
print(my_list)
# output:
# [1,5,2,8]


some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
len(some_nums)
# Use antoher python built-in function and print the result.
print(some_nums.index(12))
# Remove an item from the list. Remember to verify that it was removed.
some_nums.pop(1)
print(some_nums)
# Utilize a method from the documentation and print the result.
some_nums.sort()
print(some_nums)
print(max(some_nums))

more_nums = some_nums[:]
more_nums.reverse()
print(more_nums)
print(sorted(more_nums))