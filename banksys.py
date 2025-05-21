"""
Menu
- balance
- withraw
- deposit
- history

functions
- withraw
- deposit
- check_balance
- history

conditions
- loop menu till break exit
- after withraw and deposit call back check_balance
- list history of transaction
- handle errors
    - insufficient ammount
    - entered is not a number
    - return program to menu delay after check_balance

deposit/withraw -> array -> checkbalance -> transaction log -> menu
"""
history = []
class Bank:
    def __init__(self):
        self.balance = 0
        self.amount = 0
        print('Blazibank Banking System')
        
    def check_balance(self):
        print(f"Your Current Balance is: ", self.balance)
        
    def deposit(self):
        amount = float(input("Enter Deposit amount: "))
        self.balance += amount
        print("\nDeposited: ", amount)
        history.append("Deposit: " + str(amount))
        
    def withraw(self):
        amount = float(input("Enter Withraw amount: "))
        if self.balance >= amount:
            self.balance -= amount 
            print("\nWithrawn: ", str(amount))
            history.append("Withraw: " + str(amount))
        else:
            print("Insufficient Balance!")
        

    def v_history(self):
        print("\nList of Transaction: ")
        for i, item in enumerate(history):
            print (f"{i+1}. {item}", sep="\n")
        
s = Bank()
while True:
    print('\n\nMenu: ')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withraw')
    print('4. View History')
    print('5. Exit')

    choice = input('Enter your choice(1-5): ')
    if choice == "1":
        s.check_balance()
        
    elif choice == "2":
        s.deposit()
        
    elif choice == "3":
        s.withraw()
        
    elif choice == "4":
        s.v_history()
        
    elif choice == "5":
        print('Thank you!')
        break
    else:
        print('Invalid Choice!')
