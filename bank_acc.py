class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name  
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print(f'Your new account balance is: ${self.balance:.2f}')

    def display_balance(self):
        print(f'Your account balance is: ${self.balance:.2f}')

clark_kent = BankAccount('Clark', 'Kent', 123456, 'Savings', 4444, 2500.0)

clark_kent.deposit(96)
clark_kent.withdraw(25)

print(f'{clark_kent.balance}')