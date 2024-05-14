# LIBRARIES IMPORTED. Datetime imported to retrieve current date.
import datetime


# USER LOGIN. details requested. Variables are defined that record if a user's password has been matched and if the user should be considered as "logged in"
user_logged_in = False
while user_logged_in == False:
    user_logged_in = False
    user_found = False
    username = input("Enter username:")
    password = input("Enter password:")

# PASSWORD CHECK. Password input is check against password/user data stored in user.txt. If the password (case sensitive) and the username (not case sensitive) match then the user is considered logged in and the variable user_logged in is toggled to true.
    with open("user.txt","r",encoding="UTF-8") as userfile:

        for user in userfile:
            userdetails = user.split(",")
            saved_user = userdetails[0].strip("\n").strip()
            saved_password = userdetails[1].strip("\n").strip()
  
            if saved_user.lower() == username.lower():
                user_found = True
                if saved_password == password:
                    user_logged_in = True
                else:
                    print("\n-------------------------------\n Incorrect Password - please try again\n-------------------------------\n")

    if user_found == False:
        print("\n-------------------------------\nNo user found\n-------------------------------\n")

# USER MENU. Once a user is logged in a menu is displayed. A different menu is displayed if the username is "Admin". After each user request is complete, the programme returns to the menu, via a loop. Each user commend is nested within the menu loop.
while user_logged_in == True:

    if username.lower() == "admin":
    
        menu = input('''
------------MENU-------------

Select one of the following Options below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
s - Statistics

--------------------------
Enter selection: ''').lower()

    else:

        menu = input('''

------------MENU-------------

Select one of the following Options below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit

--------------------------
Enter selection: ''').lower()

# NEW USER REGISTRATION. If the user inputs "r" they are prompted to create a new user. The password must be confirmed, and errors are displayed if they do not match. Once successful the new user details are saved to user.txt and the message "new user created" is displayed.
    if menu == 'r':
        if user.lower == "admin":
            new_username = input(
"""\n----------NEW USER-----------
Please enter your new username: """)

            new_password_confirmed = False

            while new_password_confirmed == False:
                new_password = input("Please enter your new password:")
                new_password_confirm = input("Confirm your new password: ")
        
                if new_password == new_password_confirm:
                    new_password_confirmed = True
                    print ("\n### New user created ###\n")
                
                    with open("user.txt","a",encoding="UTF-8") as users_save_file:
                        users_save_file.write(f"\n{new_username}, {new_password}")

                else:
                    print ("\n### Passwords do not match. Please try again. ####\n")

        else: print("Only the administrator may add users")

# ADD NEW TASK. If the user inputs "a" they are prompted to create a new task and enter the tasks details. Once successful the new task details are saved to tasks.txt and the message "new task created" is displayed.


    elif menu == 'a':

        task_user = input("Who is the task assigned to? ")
        task_title = input("What is the name of the task?")
        task_description = input("Describe the task: ")
        task_due_date = input("When is the task due?")
        date_added = datetime.date.today()
        task_details = [task_user,task_title,task_description,task_due_date,date_added]
        task_completed = "No"
        
        with open("tasks.txt","a",encoding="UTF-8") as tasks_save_file:
            tasks_save_file.write(f"\n{task_user}, {task_title}, {task_description}, {task_due_date}, {date_added}, {task_completed}")
        print("\n###New Task Added###")

# VIEW ALL TASKS. If the user inputs "va" all tasks are displayed. The tasks are loaded from task.txt and looped through to read each one. The task details are split into a list and each list item is printed.


    elif menu == 'va':

        with open("tasks.txt","r",encoding="UTF-8") as task_read_file:
            for task in task_read_file:
                task_read_details = task.split(", ")
                for item in task_read_details:
                    item.strip("'").strip()
            print(f"""         
_______________TASK DETAILS_________________

Task:\t\t\t{task_read_details[1]}
Assigned to:\t\t{task_read_details[0]}
Date assigned:\t\t{task_read_details[3]}
Due date:\t\t{task_read_details[4]}
Task Complete?\t\t{task_read_details[5]}
Task Description:
{task_read_details[2]}""")

# VIEW ALL USER TASKS. If the user inputs "vm" all the current user's tasks are displayed. The tasks are read from task.txt into a list, and each list item is printed. Howvever only tasks matching the current user's name are printed.
    elif menu == 'vm':

        with open("tasks.txt","r",encoding="UTF-8") as task_read_file:
            for task in task_read_file:
                task_read_details = task.split(", ")
                for item in task_read_details:
                    item.strip("'").strip()
            if(task_read_details[0].lower()==username.lower()):
                print(f"""         
_______________TASK DETAILS_________________

Task:\t\t\t{task_read_details[1]}
Assigned to:\t\t{task_read_details[0]}
Date assigned:\t\t{task_read_details[3]}
Due date:\t\t{task_read_details[4]}
Task Complete?\t\t{task_read_details[5]}
Task Description:
{task_read_details[2]}""")


        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

# ADMIN STATISTICS. If the user selects "e" the number of users and tasks are printed. This only works if the user is "Admin". The tasks and users are counted with loops, that count each line of the respective text.txt and user.txt file.
    elif menu == 'e':

        print('Goodbye!!!')
        exit()

    elif menu == "s":
        with open("user.txt","r",encoding="UTF-8") as users_save_file:
            user_count = 0
            for line in users_save_file:
               user_count += 1

        with open("tasks.txt","r",encoding="UTF-8") as tasks_save_file:
            tasks_count = 0
            for line in tasks_save_file:
               tasks_count += 1
        print(f"""
----------------Admin Statistics-----------------

Current number of users:{user_count}
Current number of tasks:{tasks_count} """)

    else:
        print("You have made a wrong choice, Please Try again")