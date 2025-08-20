#=== Banking System Challenge ===

from datetime import datetime
from abc import ABC, abstractmethod

class Costumer:
    def __init__(self, user_name, password, address):
        self._user_name = user_name
        self._password = password
        self.address = address
        self.accounts = []

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

class PhisicalPerson(Costumer):
    def __init__(self, user_name, password, complete_name, cpf, address):
        super().__init__(user_name, password, address)
        self.complete_name = complete_name
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

class LegalEntity(Costumer):
    def __init__(self, user_name, password, company_name, cnpj, address):
        super().__init__(user_name, password, address)
        self.company_name = company_name
        self._cnpj = cnpj

    @property
    def cnpj(self):
        return self._cnpj            

class CostumerManager:
    def __init__(self):
        self.users = []
        self.current_user = {}

    def register_physical_person(self, user_name, password, complete_name, cpf, address):
        user = PhisicalPerson(user_name, password, complete_name, cpf, address)
        self.users.append(user)
        return user

    def register_legal_entity(self, user_name, password, company_name, cnpj, address):
        user = LegalEntity(user_name, password, company_name, cnpj, address)
        self.users.append(user)
        return user
        
    def login(self, user_name, password):
        for user in self.users:
            if user_name == user.user_name and password == user.password:
                self.current_user = user
                return True
        return False

class Account:
    def __init__(self, number, costumer):
        self._agency = 1
        self._number = number
        self._balance = 0
        self._costumer = costumer
        self.withdraw_times = 0
        self.withdraw_limit = 500
        self.WITHDRAW_TIMES_LIMIT = 3
        self.history = History()

    @property
    def agency(self):
        return self._agency

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    @property
    def costumer(self):
        return self._costumer

# class CheckingAccount(Account):
    # def __init__(self, number, costumer, withdraw_limit=500, withdraw_times_limit=3):
    #     super().__init__(number, costumer)
    #     self._withdraw_limit = withdraw_limit
    #     self._WITHDRAW_TIMES_LIMIT = withdraw_times_limit  
    #     self.withdraw_times = 0

    # @property
    # def withdraw_limit(self):
    #     return self._withdraw_limit

    # @property
    # def WITHDRAW_TIMES_LIMIT(self):
    #     return self._WITHDRAW_TIMES_LIMIT    

class AccountManager:
    def __init__(self):
        self.accounts = []
        self.current_account = {}

    def create_account(self, costumer):
        account_number = len(self.accounts) + 1
        account = Account(account_number, costumer)
        self.accounts.append(account)
        costumer.accounts.append(account)
        return account
    
    def login(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                self.current_account = account
                return True
        return False

class Transaction(ABC):
    def __init__(self, amount):
        self._date = datetime.now()
        self._amount = amount

    @property
    def date(self):
        return self._date

    @property
    def amount(self):
        return self._amount    

    @abstractmethod
    def register(self, account):
        pass    

class Deposit(Transaction):
    def register(self, account):
        account._balance += self.amount
        account.history.add_transaction(self)

class Withdraw(Transaction):
    def register(self, account):
        if account.withdraw_times < account.WITHDRAW_TIMES_LIMIT and self.amount <= account.balance and self.amount <= account.withdraw_limit:
            account._balance -= self.amount
            account.withdraw_times += 1
            account.history.add_transaction(self)
            return True
        else:
            return False

class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)    

    def generate_report(self, type_filter=None):
        for transaction in self.transactions:
            if type_filter is None or isinstance(transaction, type_filter): 
                yield transaction

class BankingUI:
    def __init__(self, costumer_manager, account_manager):
        self.costumer_manager = costumer_manager
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
        
        if self.costumer_manager.login(username, password):
            print("Login successful!")
            return True
        else:
            print("Invalid credentials!")
            return False            

    def _handle_registration(self):
        
        user = input('''User type:
        1. Physical Person
        2. Legal Entity
        
        Choose: ''') 

        if user == '1':
            username = input("Username: ")
            password = input("Password: ")
            complete_name = input("Complete Name: ")
            cpf = input("CPF: ")
            address = input("Address: ")
            print("Registration successful!")
            return self.costumer_manager.register_physical_person(username, password, complete_name, cpf, address)
        elif user == '2':
            username = input("Username: ")
            password = input("Password: ")
            company_name = input("Company Name: ")
            cnpj = input("CNPJ: ")
            address = input("Address: ")
            print("Registration successful!")
            return self.costumer_manager.register_legal_entity(username, password, company_name, cnpj, address)
        else:
            print("Error during registration.")
            return False

    def _show_user_menu(self):
        print(f"""
        === Welcome {self.costumer_manager.current_user.user_name} ===
        1. Enter Account
        2. Create Account
        3. Logout
        """)
        return int(input("Choose: "))

    def _handle_create_account(self):
        account = self.account_manager.create_account(self.costumer_manager.current_user)
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
        print(f"\nAccount Extract for account number {account.number}:")
        for transaction in account.history.generate_report():
            print(f"{transaction.date.strftime('%d/%m/%Y %H:%M:%S')} - "
              f"{transaction.__class__.__name__}: {transaction.amount}")
        print(f"Current Balance: {account.balance}")

    def _handle_withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        withdraw = Withdraw(amount)
        if withdraw.register(self.account_manager.current_account):
            print("Withdrawal successful!")
        else:
            print("Unauthorized transaction!")

    def _handle_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        deposit = Deposit(amount)
        deposit.register(self.account_manager.current_account)
        print("Deposit successful!")

def main():
    user_manager = CostumerManager()
    account_manager = AccountManager()
    ui = BankingUI(user_manager, account_manager)
    
    ui.run_main_menu() 

if __name__ == "__main__":
    main()  

