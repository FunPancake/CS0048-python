'''
Requirements

Display a menu with the following options:
Add
Subtract
Multiply
Divide
Exit
Prompt the user to enter their choice.
Based on the user's choice, prompt for the necessary inputs (two numbers for operations 1-4).
Perform the chosen operation and display the result.
If the user chooses to exit (option 5), terminate the program.
Handle invalid inputs gracefully and prompt the user to enter a valid choice.
'''
print('Simple Calculator')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

while True: 
    print('Menu: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')

    choice = input('Enter your choice(1-5): ')
    if choice == "1":
        firstnum = eval(input('\nEnter First Number: '))
        secondnum = eval(input('\nEnter Second Number: '))
        print('The Sum is: ', add(firstnum, secondnum))

    elif choice == "2":
        firstnum = eval(input('\nEnter First Number: '))
        secondnum = eval(input('\nEnter Second Number: '))
        print('The Difference is: ', sub(firstnum, secondnum))

    elif choice == "3":
        firstnum = eval(input('\nEnter First Number: '))
        secondnum = eval(input('\nEnter Second Number: '))
        print('The Product is: ', mult(firstnum, secondnum))

    elif choice == "4":
        firstnum = eval(input('\nEnter First Number: '))
        secondnum = eval(input('\nEnter Second Number: '))
        print('The Quotient is: ', "%.2f" % div(firstnum, secondnum))

    elif choice == "5":
        print('Thank You!')
        break
    else:
        print('Invalid Choice!')

