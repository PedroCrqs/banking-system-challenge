#=== Banking System Challenge ===

from datetime import datetime
main_menu = True

class User:
    def _init__(self):
        self.all_users = []
        self.current_user = {}
        self.menu_user = True

    def new_user(self, user_name, password, name, cpf:int, birthday:int, address):
            if (user_name and password and name and cpf and birthday and address):
                new_user = {
                        'user_name': user_name,
                        'password': password,
                        'name': name,
                        'cpf': cpf,
                        'birthday': birthday,
                        'address': address,
                    }
                print('''
                    User registered successfuly!''')
                self.all_users.append(new_user)
            else:
                print('''
                    Please fill in all fields.''')
    
    def login(self, user_name='', password=''):
        if (user_name == '' or password == ''):
                print('''
                Please enter a valid username and password.''')
        elif (user_name and password):
            found = False
            for user in self.all_users:
                if user_name == user['user_name'] and password == user['password']:
                    print('''
                Login successful!''')
                    found = True
                    self.current_user = user
                    return False, True, True
            if not found:
                print('''
                Invalid username or password.''')
                return True, False, False
            
    def user_logout(self): 
        print('''
            Logging user out!''')
        self.menu_user = False
        return
                    
class Account: 
    def __init__(self):
        self.accounts =  []
        self.current_account = {}
        self.withdraw_limit = 500
        self.WITHDRAW_TIMES_LIMIT = 3
        self.account_menu = True
                                 
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

    def enter_account(self):
        if not self.accounts:
                print('''
                You have no accounts yet! Please create one.''')
        self.current_account = int(input('''
                Agency: 0001
                Choose an account number: '''))
        if self.current_account < 0:
            print('''
                Invalid account number.''')
                    
        else:
            self.current_user.update(self.accounts[self.current_account - 1])
            return False, False, True

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

main_system = Main_System()

while True: #=== Main system loop ===

    #=== Login page Loop ===

    while(menu_user):
        welcome = int(input('''
                Hello, welcome to the FuBank!
                    1. for login
                    2. for register
                        
                '''))
        if (welcome == 1):
            user_name = input('''
                Username: ''')
            password = input('''
                Password: ''')
            menu_user, account_menu, main_menu = main_system.__login__(user_name, password)
            continue                     
        elif (welcome == 2):
            user_name = input('''
                Choose a username: ''')
            password = input('''
                Choose a password: ''')
            name = input('''
                Complete name: ''')
            cpf = input('''
                CPF: ''')
            birthday = input('''
                Birthday(dd/mm/yy): ''')
            address = input('''
                Address(st - num - district - city / state): ''')
            main_system.new_user(user_name, password, name, cpf, birthday, address)
            continue
        else:
            print('''
                Please enter a valid option.''')
            continue

    #=== Login page Loop End ===

    #=== Account Menu Loop ===

    while(account_menu): 
        current_account = {}
        if (main_system.current_user):
            try:
                menu = int(input(f'''     
                Hello {main_system.current_user['name'].split()[0]}! Chose one number:

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
                menu_user, account_menu, main_menu = main_system.enter_account()                              
            elif (menu == 2): 
                main_system.new_account()
                continue
            elif (menu == 3):
                menu_user, account_menu, main_menu = main_system.user_logout()
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

    while (main_menu):
        if (main_system.current_user):
            try:
                menu = int(input(f'''     
                Welcome to account number {main_system.current_user['account_number']}! Choose one number:

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
                {''.join(main_system.current_user['extract'])}     
                                ''')
                main_menu = main_system.ask_menu() 
            elif (menu == 2): 
                try:
                    withdraw_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')
                    continue
                main_system.withdraw(withdraw_value)
                main_menu = main_system.ask_menu()
            elif (menu == 3): 
                try:
                    deposit_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')                       
                    continue
                main_system.deposit(deposit_value)
                main_menu = main_system.ask_menu()
            elif (menu == 4): 
                menu_user, account_menu, main_menu = main_system.account_logout() 
            elif (menu == 5): 
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()
            else:    
                print('''
                Please chose one valid option''')
                continue

#=== Transaction Menu Loop ends ===