#=====importing libraries===========
from datetime import date

#====Login Section====
print("Welcome to Task Manager\n")

# open user file so it can be read
user_file = open('user.txt', 'r')
all_users = user_file.read()
user_file.close()

# create a list of users containing username and password
users_list = all_users.split("\n")

# variable used to break while loop when correct details entered
breaker = False     

# loop until correct details entered
while True:
    # ask user for login details
    username = input("Username:\t")
    password = input("Password:\t")

    # check entered username and password against user list
    for user in users_list:
        deets = user.split(', ')
        if username == deets[0] and password == deets[1]:
            print("\nSuccessfully logged in!\n")
            breaker = True;
            break
    
    if breaker:
        break

    # give error message to say wrong details entered after for loop
    print("\nWrong credentials entered. Please try again...\n")

#====Main Menu====
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    if username == "admin":
        menu = input('''Select one of the following options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
s - View stats
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following options below:
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()



    if menu == 'r' and username == "admin":
        print("\nRegister New User\n")
        # ask user for login details
        username = input("New Username:\t")
        password = input("New Password:\t")
        password_confirm = input("Confirm New Password:\t")

        if password == password_confirm:
            # open user file to append
            with open("user.txt", "a") as file:
                file.write(username + ", " + password + "\n")

            print("\nNew user created\n")
        else:
            print("\nThe passwords did not match\n")
    elif menu == 'a':
        print("\nAdd New Task\n")
        # get task details from user
        username = input("Username:\t")
        title = input("Task Title:\t")
        desc = input("Description:\t")
        today = date.today()
        assigned_date = today.strftime("%d %b %Y")
        print("Assigned:\t" + assigned_date)
        due_date = input("Due Date:\t")

        # write new task to tasks.txt
        with open("tasks.txt", "a") as file:
            file.write(username + ", " + title + ", " + desc + ", " + assigned_date + ", " + due_date + ", " + "No" + "\n")

        print("\nNew task created\n")
    elif menu == 'va':
        # read the tasks file
        with open("tasks.txt", "r") as file:
            all_tasks = file.read()
        
        # create a list of tasks
        task_list = all_tasks.split("\n")

        # print number of tasks (-1 to ignore final empty line)
        print(f"\nThere are currently {len(task_list)-1} tasks assigned to all users:\n")

        # loop through list of tasks and print to screen
        for task in task_list:
            # split task into each seperate detail
            deets = task.split(', ')
            
            # break for loop if we reached the last line of the file
            if len(deets) <= 1:
                break

            # print in a readable format
            print("-----------------------------------------------------------------------------------------")
            print("Task:\t\t" + deets[1])
            print("Assigned to:\t" + deets[0])
            print("Date assigned:\t" + deets[3])
            print("Due Date:\t" + deets[4])
            print("Task Complete?\t" + deets[5])
            print("Description:\n\t" + deets[2] + "\n")
    elif menu == 'vm':
        # read the tasks file
        with open("tasks.txt", "r") as file:
            all_tasks = file.read()
        
        # create a list of tasks
        task_list = all_tasks.split("\n")

         # create subset list for currently logged in user
        user_tasks = []
        for task in task_list:
            deets = task.split(", ")
            if deets[0] == username:
                user_tasks.append(deets[0] + ", " + deets[1] + ", " + deets[2] + ", " + deets[3] + ", " + deets[4] + ", " + deets[5])

        # print number of tasks assigned to currently logged in user
        print(f"\nThere are currently {len(user_tasks)} tasks assigned to {username}:\n")

        # loop through list of tasks and print to screen
        for task in user_tasks:
            # split task into each seperate detail
            deets = task.split(', ')

            # print in a readable format
            print("-----------------------------------------------------------------------------------------")
            print("Task:\t\t" + deets[1])
            print("Assigned to:\t" + deets[0])
            print("Date assigned:\t" + deets[3])
            print("Due Date:\t" + deets[4])
            print("Task Complete?\t" + deets[5])
            print("Description:\n\t" + deets[2] + "\n")
            
    elif menu == 's' and username == "admin":
        print("\nTask Manager Statistics\n")

        # read the tasks file
        with open("tasks.txt", "r") as file:
            all_tasks = file.read()
        
        # create a list of tasks
        task_list = all_tasks.split("\n")

        # print number of tasks (-1 to ignore empty final line)
        print(f"Total number of tasks:\t{len(task_list)-1}")

        # read the user file
        with open("user.txt", "r") as file:
            all_users = file.read()
        
        # create a list of tasks
        user_list = all_users.split("\n")

        # print number of tasks (-1 to ignore empty final line)
        print(f"Total number of users:\t{len(user_list)-1}\n")
    elif menu == 'e':
        print('\nGoodbye!!!\n')
        # close files and exit
        
        exit()

    else:
        print("\nYou have made a wrong choice. Please try again...\n")
