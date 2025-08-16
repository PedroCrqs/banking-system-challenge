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

    def create_account(self, number, user_name):
        account = Account(number, user_name)
        self.accounts.append(account)
        return account

class BankingUI:
    def __init__(self, user_manager):
        self.user_manager = user_manager                   

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
                self.run_account_menu()
            elif choice == 2:
                self._handle_create_account()
            elif choice == 3:
                self._handle_logout()
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

def main():
    user_manager = UserManager()
    account_manager = AccountManager()
    ui = BankingUI(user_manager, account_manager)
    
    ui.run_main_menu() 

if __name__ == "__main__":
    main()                   


class Account: 
    def __init__(self, current_user=None):
        self.current_user = current_user
        self.accounts =  []
        self.current_account = {}
        self.withdraw_limit = 500
        self.WITHDRAW_TIMES_LIMIT = 3
        self.account_menu = True
        self.main_menu = True
                                 
    def new_account(self):
        account_number = len(self.accounts) + 1
        self.accounts.append({
                    'agency': '0001',
                    'account_number': account_number,
                    'user_name': self.current_user['user_name'],
                    'balance': 0,
                    'withdraw_times': 0,
                    'extract': []
                })
        print(f'''
                Account created successfuly!
                Your agency is: 0001
                Your account number is: {account_number}''')

    def enter_account(self, enter_account_ui):
        current_account = enter_account_ui()
        if current_account <= len(self.accounts):
            self.current_account = self.accounts[current_account - 1]
            return True
       
    def enter_account_ui(self):
        if not self.accounts:
                print('''
                You have no accounts yet! Please create one.''')
        current_account = int(input('''
                Agency: 0001
                Choose an account number: '''))
        if current_account < 0:
            print('''
                Invalid account number.''')
        return current_account


    def withdraw(self, withdraw_value=0):
        idx = self.current_account - 1
        account = self.accounts[idx]
        if withdraw_value <= 0:
            print('''
                Please enter a positive value.              
            ''')
            return
        elif (withdraw_value > account['balance'] or withdraw_value > self.withdraw_limit or account['withdraw_times'] >= self.WITHDRAW_TIMES_LIMIT):
            print('''
                Unauthorized transaction              
            ''')
            return
        else:
            account['balance'] -= withdraw_value
            account['withdraw_times'] += 1
            account['extract'].append(f'''
                Withdraw: R$ -{withdraw_value}
                Balance: R$ {account['balance']}''')
            print(f'''
                Successful withdraw! Your balance: R$ {account['balance']}
            ''')
            self.current_user.update(account)
            return

    def deposit(self, deposit_value=0):
        idx = self.current_account - 1
        account = self.accounts[idx]
        if deposit_value <= 0:
            print('Please enter a positive value.')
            return
        else:
            account['balance'] += deposit_value
            account['extract'].append(f'''
                Deposit: R$ +{deposit_value}
                Balance: R$ {account['balance']}''')
            print(f'''                      
                Successful deposit! Your balance: R$ {account['balance']}''')
            self.current_user.update(account)
            return

    def ask_menu(self): 
        end_menu = int(input('''      
                What do you want to do?
                        
                    1. for menu
                    2. for end
                        
                '''))
        if (end_menu == 1):
            return True
        elif (end_menu == 2):
            print('''
                Thanks for using FuBank system! See you later!''')
            exit()    

    def account_logout(self): 
            print('''
                Logging account out!''')
            return False, True, False

user = User()
account = Account(user.current_user)

while True: #=== Main system loop ===

    #=== Login page Loop ===

    while(user.menu_user):
        welcome = int(input('''
                Hello, welcome to the FuBank!
                    1. for login
                    2. for register
                        
                '''))
        if (welcome == 1):
            login_success = user.login(user.login_ui)
            if login_success:
                user.menu_user = False
                print('Login successful!')
            else:
                print('''
                    Invalid username or password.''')  
            continue                     
        
        elif (welcome == 2):
            user.new_user(user.new_user_ui)
            continue
        
        else:
            print('''
                Please enter a valid option.''')
            continue

    #=== Login page Loop End ===

    #=== Account Menu Loop ===

    while(account.account_menu): 
        current_account = {}
        if (user.current_user):
            try:
                menu = int(input(f'''     
                Hello {user.current_user['name'].split()[0]}! Chose one number:

                    1. for Enter an existent account
                    2. for Create a new account
                    3. for Logout
                    4. for End
                    
                ''')
            )
            except ValueError:
                print('''
                Please enter a valid number.''')    
                continue 
            if (menu == 1): 
                account.main_menu = account.enter_account(account.enter_account_ui())                              
            elif (menu == 2): 
                account.new_account()
                continue
            elif (menu == 3):
                menu_user, account_menu, main_menu = user.user_logout()
            elif (menu == 4):
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()
            else:    
                print('''
                Please chose one valid option''')
                continue

    #=== Account Menu Loop End ===            

    #=== Transaction Menu Loop ===

    while (account.main_menu):
        if (account.current_account):
            try:
                menu = int(input(f'''     
                Welcome to account number {account.current_user['account_number']}! Choose one number:

                    1. for Extract
                    2. for Withdraw
                    3. for Deposit
                    4. for Logout
                    5. for End

                ''')
            )
            except ValueError:
                print('''
                Please enter a valid number.''')    
                continue 
            if (menu == 1): 
                print(f'''  
                {''.join(account.current_account['extract'])}     
                                ''')
                main_menu = account.ask_menu() 
            elif (menu == 2): 
                try:
                    withdraw_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')
                    continue
                account.withdraw(withdraw_value)
                main_menu = account.ask_menu()
            elif (menu == 3): 
                try:
                    deposit_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')                       
                    continue
                account.deposit(deposit_value)
                main_menu = account.ask_menu()
            elif (menu == 4): 
                menu_user, account_menu, main_menu = account.account_logout() 
            elif (menu == 5): 
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()
            else:    
                print('''
                Please chose one valid option''')
                continue

#=== Transaction Menu Loop ends ===