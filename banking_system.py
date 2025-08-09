#=== Banking System Challenge ===

menu_user = True
account_menu = True
main_menu = True


class Main_System:
    
    def __init__(self):
        self.all_users = []
        self.accounts =  []
        self.current_user = {}
        self.current_account = {}
        self.withdraw_limit = 500
        self.WITHDRAW_TIMES_LIMIT = 3
        
    def __new_user__(self, user_name, password, name, cpf=int, birthday=int, address=''):
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
            main_system.all_users.append(new_user)
        else:
            print('''
                Please fill in all fields.''')

    def __login__(self, user_name='', password=''):
        if (user_name == '' or password == ''):
                print('''
                Please enter a valid username and password.''')
        elif (user_name and password):
            found = False
            for user in main_system.all_users:
                if user_name == user['user_name'] and password == user['password']:
                    print('''
                Login successful!''')
                    found = True
                    main_system.current_user = user
                    return False, True, True
            if not found:
                print('''
                Invalid username or password.''')
                return True, False, False
                    
                                 
    def __new_account__(self):
        account_number = len(main_system.accounts) + 1
        main_system.accounts.append({
                    'agency': '0001',
                    'account_number': account_number,
                    'user_name': main_system.current_user['user_name'],
                    'balance': 0,
                    'withdraw_times': 0,
                    'extract': []
                })
        print(f'''
                Account created successfuly!
                Your agency is: 0001
                Your account number is: {account_number}''')

    def __enter_account__(self):
        if not main_system.accounts:
                print('''
                You have no accounts yet! Please create one.''')
        main_system.current_account = int(input('''
                Agency: 0001
                Choose an account number: '''))
        if main_system.current_account < 0:
            print('''
                Invalid account number.''')
                    
        else:
            main_system.current_user.update(main_system.accounts[main_system.current_account - 1])
            return False, False, True

    def __withdraw__(self, withdraw_value=0):
        idx = main_system.current_account - 1
        account = main_system.accounts[idx]
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
            main_system.current_user.update(account)
            return

    def __deposit__(self, deposit_value=0):
        idx = main_system.current_account - 1
        account = main_system.accounts[idx]
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
            main_system.current_user.update(account)
            return

    def __ask_menu__(self): 
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

    def __user_logout__(self): 
        print('''
                Logging user out!''')
        return True, False, False

    def __account_logout__(self): 
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
            main_system.__new_user__(user_name, password, name, cpf, birthday, address)
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
                menu_user, account_menu, main_menu = main_system.__enter_account__()                              
            elif (menu == 2): 
                main_system.__new_account__()
                continue
            elif (menu == 3):
                menu_user, account_menu, main_menu = main_system.__user_logout__()
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
                main_menu = main_system.__ask_menu__() 
            elif (menu == 2): 
                try:
                    withdraw_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')
                    continue
                main_system.__withdraw__(withdraw_value)
                main_menu = main_system.__ask_menu__()
            elif (menu == 3): 
                try:
                    deposit_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')                       
                    continue
                main_system.__deposit__(deposit_value)
                main_menu = main_system.__ask_menu__()
            elif (menu == 4): 
                menu_user, account_menu, main_menu = main_system.__account_logout__() 
            elif (menu == 5): 
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()
            else:    
                print('''
                Please chose one valid option''')
                continue

#=== Transaction Menu Loop ends ===