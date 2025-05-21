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
    def __init__(self, balance, amount):
        self.balance = balance
        self. amount = amount
        print('Blazibank Banking System')
        
    def check_balance(self, balance):
        print(f"balance is: {self.balance} ")
        
    def deposit(self, balance, amount):
        self.amount = float(input("Enter deposit amount: "))
        self.balance += self.amount
        print("\n Deposited: ", self.amount)
        history.append("Deposit ", "$", self.amount)
        
    def withraw():
        amount = float(input("Enter withdrawal amount: "))
        balance -= amount
        print("\n Withrawn: ", amount)
        history.append("Withraw, ", "$",amount)

    def v_history():
        # for i, item in enumerate(history):
        #     print (f"{i+1}. {item}", sep="\n")
        print('list')
        
    while True:
        print('Menu: ')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withraw')
        print('4. View History')
        print('5. Exit')

        choice = input('Enter your choice(1-5): ')
        if choice == "1":
            check_balance(self, balance)
            
        elif choice == "2":
            deposit()
            
        elif choice == "3":
            withraw()
            
        
        elif choice == "4":
            v_history()
            
        elif choice == "5":
            print('Thank you!')
            break
        else:
            print('Invalid Choice!')