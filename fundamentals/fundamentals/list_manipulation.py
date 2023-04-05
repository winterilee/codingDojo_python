drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]


# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
print(drawers[1])

# Change "pens" to "useless manuals"
drawers[2] = "useless manuals"

# Change the first value to whatever is the second value
drawers[0] = drawers[1]

# What should the list look like now?
# ['envelops', 'envelops', 'useless manuals']

# Print the list! Does it match your prediction?
print(drawers)


nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]


nums = [1,2,3,4,5]

# Challenge: Append some values to the list!
nums.append(77)
print(nums)
nums.append("88")
print(nums)


words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

print(words[0:3])
copy_of_copy_of_words = copy_of_words[:]
copy_of_copy_of_words.append("coding")
print(copy_of_copy_of_words)
copy_of_copy_of_words.append(words[0:1])
copy_of_copy_of_words.append(words[4])
print(copy_of_copy_of_words)