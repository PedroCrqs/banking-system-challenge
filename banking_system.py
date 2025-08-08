
#=== Banking System Challenge ===

class Main_System:
    
    def __init__(self):
        self.all_users = []
        self.accounts =  []
        self.current_user = {}
        self.current_account = {}

    def __new_user__(self, user_name='', password='', name='', cpf='', birthday='', address=''):
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
                    return False
            if not found:
                print('''
                Invalid username or password.''')
                return True
                    
                                 
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
        
account_menu = True
menu_loop = True
main_system = Main_System()
login = True   


def logout(): #=== Logout ===
        print('''
                Logging out!''')
        return False, False

def ask_menu(): 
    toDo = int(input('''      
            What do you want to do?
                    
                1. for menu
                2. for end
                    
            '''))
    if (toDo == 1):
        return True
    elif (toDo == 2):
        print('''
            Thanks for using FuBank system! See you later!''')
        exit()    

def withdraw(balance, extract, withdraw_limit, withdraw_times, withdraw_times_limit, withdraw_value):
    if withdraw_value <= 0: #=== Function to withdraw money ===
        print('''
            Please enter a positive value.              
            ''')
        return
    elif (withdraw_value > balance or withdraw_value > withdraw_limit or withdraw_times >= withdraw_times_limit):
        print('''
            Unauthorized transaction              
            ''')
        return
    else:
        balance -= withdraw_value
        withdraw_times += 1
        extract.append(f'''
            Withdraw: R$ -{withdraw_value}
            Balance: R$ {balance}''')
        print(f'''
            Successful withdraw! Your balance: R$ {balance}
            ''')
        return balance, extract, withdraw_times

def deposit(deposit_value, balance, extract): #=== Function to deposit money ===  
    if deposit_value <= 0:
        print('Please enter a positive value.')
        return
    else:
        balance += deposit_value
        extract.append(f'''
            Deposit: R$ +{deposit_value}
            Balance: R$ {balance}''')
        print(f'''                      
            Successful deposit! Your balance: R$ {balance}''')    
        return balance, extract

while True: #=== Main system loop ===

    #=== Login page Loop ===

    while(login):
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
            login = main_system.__login__(user_name, password)
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

            if (menu == 1): #=== Enter an existent account option ===
                main_system.__enter_account__()
                break

            elif (menu == 2): #=== Create a new account option ===
                main_system.__new_account__()
                continue
            
            elif (menu == 3): #=== Logout option ===
                logout()
                                        
            elif (menu == 4): #=== End option ===
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()

            else:    
                print('''
                Please chose one valid option''')
                continue

    #=== Account Menu Loop End ===            

    #=== Main account Menu Loop ===

    while (menu_loop):
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
            if (menu == 1): #=== Extract option ===
                print(f'''  
                {''.join(main_system.current_user['extract'])}     
                                ''')
                menu_loop = ask_menu() 
            
            elif (menu == 2): #=== Withdraw option ===
                try:
                    withdraw_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')
                    continue
                result = withdraw(main_system.current_user['balance'], main_system.current_user['extract'], WITHDRAW_LIMIT, main_system.current_user['withdraw_times'], WITHDRAW_TIMES_LIMIT, withdraw_value)
                if result:
                    main_system.current_user['balance'], main_system.current_user['extract'], main_system.current_user['withdraw_times'] = result
                    menu_loop = ask_menu()

            elif (menu == 3): #=== Deposit option ===
                try:
                    deposit_value = int(input('''
                Value: R$ '''))
                except ValueError:
                    print('''
                Please enter a valid number.''')                       
                    continue

                result = deposit(deposit_value, current_user['balance'], current_user['extract'])
                if result:
                    current_user['balance'], current_user['extract'] = result
                    menu_loop = ask_menu()

            elif (menu == 4): 
                account_menu, menu_loop = logout() 
                        
            elif (menu == 5): 
                print('''
                Thanks for using FuBank system! See you later!''')
                exit()

            else:    
                print('''
                Please chose one valid option''')
                continue

