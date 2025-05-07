import random

'''
Requirements

Display a menu with the following options:
Play Number Guessing Game
Exit
Prompt the user to enter their choice.
If the user chooses to play (option 1):
Generate a random number between 1 and 100.
Prompt the user to guess the number.
Provide feedback on whether the guess is too high, too low, or correct.
Continue prompting for guesses until the correct number is guessed.
Display the number of attempts taken to guess the correct number.
If the user chooses to exit (option 2), terminate the program.
Handle invalid inputs gracefully and prompt the user to enter a valid choice.
'''

print('Guess the Number')

lucky = random.randint(1,100)

chosen = eval(input('Enter Any no. from 1 up to 100: '))

if chosen == lucky:
    print('You have WON!')
elif chosen != lucky:
    print('The Number is: ', lucky, '\n','Try Again next time!')
