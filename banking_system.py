#=== Banking System Challenge ===

from datetime import datetime

class User:
    def __init__(self, user_name, password, complete_name, cpf, address):
        self.user_name = user_name
        self.password = password
        self.complete_name = complete_name
        self.cpf = cpf
        self.address = address

class UserManager:
    def __init__(self):
        self.users = []
        self.current_user = {}

    def register_user(self, user_name, password, complete_name, cpf, address):    
        user = User(user_name, password, complete_name, cpf, address)
        self.users.append(user)
        return user
        
    def login(self, user_name, password):
        for user in self.users:
            if user_name == user.user_name and password == user.password:
                self.current_user = user
                return True
            return False

    def merge_user_changes(self):
        user_name = self.current_user.user_name
        password = self.current_user.password
        for user in self.users:
            if user.user_name == user_name:
                user.password = password
                user = self.current_user
                return user

class Account:
    def __init__(self, number, user_name):
        self.agency = 1
        self.number = number
        self.balance = 0
        self.user_name = user_name
        self.extract = []
        self.withdraw_times = 0
        self.withdraw_limit = 500
        self.WITHDRAW_TIMES_LIMIT = 3

class AccountManager:
    def __init__(self):
        self.accounts = []
        self.current_account = {}

    def create_account(self, user_name):
        account_number = len(self.accounts) + 1
        account = Account(account_number, user_name)
        self.accounts.append(account)
        return account
    
    def login(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                self.current_account = account
                return True
            return False

    def deposit(self, amount):
        self.current_account.balance += amount
        self.current_account.extract.append({
            "date": datetime.now(),
            "type": "deposit",
            "amount": amount
        })

    def withdraw(self, amount):
        if (self.current_account.withdraw_times >= self.current_account.WITHDRAW_TIMES_LIMIT or amount > self.current_account.balance or self.current_account.withdraw_limit < amount):
            return False
        else:
            self.current_account.balance -= amount
            self.current_account.extract.append({
                "date": datetime.now(),
                "type": "withdraw",
                "amount": amount
            })
            self.current_account.withdraw_times += 1
            return True

class BankingUI:
    def __init__(self, user_manager, account_manager):
        self.user_manager = user_manager
        self.account_manager = account_manager

    def run_main_menu(self):
        while True:
            try:
                choice = self._show_main_menu()
                if choice == 1:
                    if self._handle_login():
                        self.run_user_menu()
                elif choice == 2:
                    self._handle_registration()
                elif choice == 3:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option!")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

    def run_user_menu(self):
         while True:
            choice = self._show_user_menu()
            if choice == 1:
                if self._handle_account_login():
                    self.run_account_menu()
                else:
                    continue
            elif choice == 2:
                self._handle_create_account()
            elif choice == 3:
                break
    
    def run_account_menu(self):
        while True:
            choice = self._show_account_menu()
            if choice == 1:
                self._handle_extract()
            elif choice == 2:
                self._handle_withdraw()
            elif choice == 3:
                self._handle_deposit()
            elif choice == 4:
                break  
            # ...
    
    def _show_main_menu(self):
        print("""
        === FuBank ===
        1. Login
        2. Register
        3. Exit
        """)
        return int(input("Choose: "))
    
    def _handle_login(self):
        username = input("Username: ")
        password = input("Password: ")
        
        if self.user_manager.login(username, password):
            print("Login successful!")
            return True
        else:
            print("Invalid credentials!")
            return False            

    def _handle_registration(self):
        username = input("Username: ")
        password = input("Password: ")
        complete_name = input("Complete Name: ")
        cpf = input("CPF: ")
        address = input("Address: ")

        user = self.user_manager.register_user(username, password, complete_name, cpf, address)
        if user:
            print("Registration successful!")
            return True
        else:
            print("Error during registration.")
            return False

    def _show_user_menu(self):
        print(f"""
        === Welcome {self.user_manager.current_user.complete_name} ===
        1. Enter Account
        2. Create Account
        3. Logout
        """)
        return int(input("Choose: "))

    def _handle_create_account(self):
        account = self.account_manager.create_account(self.user_manager.current_user.user_name)
        print(f"Account created successfully! Your account number is {account.number}.")

    def _handle_account_login(self):
        account_number = int(input("Enter your account number: "))
        if self.account_manager.login(account_number):
            print("Account login successful!")
            return True
        else:
            print("Invalid account number!")
            return False

    def _show_account_menu(self):
        print(f"""
        === Account Menu ===
        1. Extract
        2. Withdraw
        3. Deposit
        4. Logout
        """)
        return int(input("Choose: "))
    
    def _handle_extract(self):
        account = self.account_manager.current_account
        print(f"Account Extract for {account.user_name}:")
        for transaction in account.extract:
            print(f"{transaction['date']} - {transaction['type']}: {transaction['amount']}")
        print(f"Current Balance: {account.balance}")

    def _handle_withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.account_manager.withdraw(amount):
            self.user_manager.merge_user_changes()
            print("Withdrawal successful!")
        else:
            print("Unauthorized transaction!")

    def _handle_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.account_manager.deposit(amount)
        self.user_manager.merge_user_changes()
        print("Deposit successful!")

def main():
    user_manager = UserManager()
    account_manager = AccountManager()
    ui = BankingUI(user_manager, account_manager)
    
    ui.run_main_menu() 

if __name__ == "__main__":
    main()  

