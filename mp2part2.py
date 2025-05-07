'''
Requirements

Display a menu with the following options:
Convert Celsius to Fahrenheit
Convert Fahrenheit to Celsius
Exit
Prompt the user to enter their choice.
Based on the user's choice, prompt for the necessary input (temperature in Celsius or Fahrenheit).
Perform the conversion and display the result.
If the user chooses to exit (option 3), terminate the program.
Handle invalid inputs gracefully and prompt the user to enter a valid choice.
'''

print('Temperatur converter')

def celToFahr(a):
    cel = (a*(9/5))+32
    return cel

def fahrToCel(a):
    fahr = (a - 32) * (5/9)
    return fahr

while True:
    print('Menu: ')
    print('1. Celcius to Fahrenheit')
    print('2. Fahrenheit to Celcius')
    print('3. Exit')

    choice = input('Enter your choice(1-3): ')
    if choice == "1":
        tmp = eval(input('Enter Celcius tmp: '))
        print('Fahrenheit Tmp = ', "%.2f" % celToFahr(tmp))

    elif choice == "2":
        tmp = eval(input('Enter Fahernhiet tmp: '))
        print('Celcius tmp = ',"%.2f" % fahrToCel(tmp))

    elif choice == "3":
        print('Thank you!')
        break
    else:
        print('Invalid Choice!')