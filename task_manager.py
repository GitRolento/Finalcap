from datetime import date

# gather the username and the password from the user
file = open('user.txt', 'r')
users = file.read()
file.close()

username = input("Enter your username: ")
password = input("Enter your password: ")

# open user.txt and store the usernames in a list, then closer the fileadmin

usernames = []
passwords = []

users = users.split("\n")
# loop through each user and split the username up from the password
for user in users:
    my_user = user.split(", ")
    usernames.append(my_user[0])
    passwords.append(my_user[1])

# check to see if the entered username is is the usernames list, if it isnt re enter
while username not in usernames:
    username = input("Error! Please re-enter your username: ")

# find the index of the usdername to compare it to the password
# when theentrerned name is the same as the username, save the index
index = ""
for position, name in enumerate(usernames):
    if name == username:
        index = position

while password != passwords[index]:
    password = input("Incorrect password! Please re-enter: ")

while True:
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.

    if username == 'admin':
        menu = input('''Select one of the following Options below:
        r - Registering a user
        d - Display statistics
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    # if the user wants to register they have to use the admin name
    if menu == 'r' and username == 'admin':

        new_user = input("Enter the new username: ")
        new_pass = input("Enter the new password: ")
        confirm_password = input("Confirm your password: ")
        # the passwords will have to match the admin password which is sorted in the txt file
        while confirm_password != new_pass:
            print("Error! passwords don't match.")
            new_pass = input("Enter the new password: ")
            confirm_password = input("Confirm the new password: ")

        if new_pass == confirm_password:
            file = open('user.txt', 'a')
            file.write(f"\n{new_user}, {new_pass}")
            usernames.append(new_user)
            passwords.append(new_pass)
            file.close()

    elif menu == 'd' and username == 'admin':
        # here I will insert code to display statistics to the admin
        file = open('tasks.txt', 'r')

        number_lines = 0
        for line in file:
            number_lines += 1

        print(f"The total number of tasks is:     {number_lines}")
        print(f"The total numbers of users is:    {len(usernames)}")
    # assign task to a user
    elif menu == 'a':

        user_task = input("Enter the username of the person whom the task is assigned to: ")
        title = input("Enter the title for this task: ")
        description = input("Enter a description of this task: ")
        due_date = input("Enter the due date of this task (dd/mm/yy): ")

        today = date.today()

        current_date = today.strftime("%d/%m/%Y")

        file = open('tasks.txt', 'a')
        file.write(f"\n{user_task}, {title}, {description}, {due_date}, {current_date}, No")
        file.close()


    # if user wants to view all task the option will come upto them
    elif menu == 'va':
            with open('tasks.txt', 'r') as file:
                for line in file:

                    my_line = line.strip().split(", ")

                    print(f"Task:           {my_line[1]}")
                    print(f"Assigned to:    {my_line[0]}")
                    print(f"Date assigned:  {my_line[3]}")
                    print(f"Due date:       {my_line[4]}")
                    print(f"Task complete?  {my_line[5]}")
                    print(f"Task Description:\n{my_line[2]}\n")

    # if user wants to view all their own task the option will come upto them
    elif menu == 'vm':

        file = open('tasks.txt', 'r')
        for line in file:
            my_line = line.split(", ")
            if username == my_line[0]:
                print(f"Task:           {my_line[1]}")
                print(f"Assigned to:    {my_line[0]}")
                print(f"Date assigned:  {my_line[3]}")
                print(f"Due date:       {my_line[4]}")
                print(f"Task complete?  {my_line[5]}")
                print(f"Task Description:\n{my_line[2]}\n")
    # this will exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")