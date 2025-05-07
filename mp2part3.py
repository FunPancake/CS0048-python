'''
Requirements
Display a menu with the following options:
Add Task
Remove Task
View Tasks
Exit
Prompt the user to enter their choice.
Based on the user's choice:
If "Add Task" (option 1), prompt for the task description and add it to the list.
If "Remove Task" (option 2), prompt for the task description and remove it from the list if it exists.
If "View Tasks" (option 3), display all tasks in the list.
If "Exit" (option 4), terminate the program.
Handle invalid inputs gracefully and prompt the user to enter a valid choice.
'''

print('Simple Calculator')

task= []

def addTask():
    task.append(input('Input a task: '))

def removeTask():
    task.remove(input('Enter task: '))

def viewTask():
    for i, item in enumerate(task):
        print (f"{i+1}. {item}", sep="\n")



while True: 
    print('Menu: ')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Tasks')
    print('4. Exit')

    choice = input('Enter your choice(1-4): ')
    if choice == "1":
        addTask()

    elif choice == "2":
        removeTask()

    elif choice == "3":
        viewTask()
        print('\n')

    elif choice == "4":
        print('Thank you!')
        break
    else:
        print('Invalid Choice!')