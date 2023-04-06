my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


for key in my_dict.keys():
    print(key)
for val in my_dict.values():
    print(val)
for key, val in my_dict.items():
    print(key + ": " + val)


# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(users[0]["last"]) # prints Lovelace

print(resume_data["skills"][1])
# My prediction: "back_end"
print(users[2]["first"])
# My prediction: Eric

resumes = [

    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies":["rock climbing", "knitting"]
    },

    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies":["rock climbing", "knitting"]
    },

    {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies":["rock climbing", "knitting"]
    },

]

# Print the first listed language of the 2nd resume
print(resumes[1]["languages"][0])