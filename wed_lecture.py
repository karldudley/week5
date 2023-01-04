# read a file and put it into a dictionary
file = open("user.txt", "r")

user_database = {}

for line_num, line in enumerate(file):
    user_database[line_num] = line

print(user_database)
