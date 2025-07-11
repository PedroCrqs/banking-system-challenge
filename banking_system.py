
login = True
user_name = ''
password = ''
name = ''
cpf = 0
birthday = ''
address = ''
new_user = {}
all_users = []

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
        if (user_name == "" or password == ''):
            print('''
              Please enter a valid username and password.''')
        elif (user_name and password):
            found = False
            for user in all_users:
                if user_name == user['user_name'] and password == user['password']:
                    print('''
              Login successful!''')
                    found = True
                    login = False
                    break

            if not found:
                print('''
              Invalid username or password.''')
                continue
        
    elif (welcome == 2):
        user_name = input('''
              Choose a username: ''')
        password = input('''
              Choose a password: ''')
        name = input('''
              Complete name: ''')
        cpf = int(input('''
              CPF: '''))
        birthday = input('''
              Birthday(dd/mm/yy): ''')
        address = input('''
              Address(st - num - district - city / state): ''')
        if (user_name and password and name and cpf and birthday and address):
            new_user = {
                'user_name': user_name,
                'password': password,
                'name': name,
                'cpf': cpf,
                'birthday': birthday,
                'address': address
            }
            print('''
              User registered successfully!''')
            all_users.append(new_user)
            continue
        else:
            print('''
              Please fill in all fields.''')
            continue
    
    else:
        print('''
              Please enter a valid option.''')
        continue

#=== Login page Loop End ===

balance = 0
WITHDRAW_LIMIT = 500
WITHDRAW_TIMES_LIMIT = 3
withdraw_times = 0
menuLoop = True
extract = [f'''
              Extract:
           
              Balance: R$ {balance}''']

def ask_menu(): #=== Function to ask if the user wants to continue or end system ===
    toDo = int(input('''      
              What do you want to do?
                      
                1. for menu
                2. for end
                      
              '''))
    return toDo == 1

def withdraw(balance: int, withdraw_limit: int, withdraw_times: int, withdraw_times_limit: int, withdraw_value: int) -> tuple:
    if withdraw_value <= 0: #===function to withdraw money===
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
              Sucessfull withdraw! Your balance: R$ {balance}
              ''')
        return balance, withdraw_times

def deposit(deposit_value, balance, extract): #===function to deposit money===
    global menuLoop    
    if deposit_value <= 0:
        print('Please enter a positive value.')
        return
    else:
        balance += deposit_value
        extract.append(f'''
              Deposit: R$ +{deposit_value}
              Balance: R$ {balance}''')
        print(f'''                      
              Sucessfull deposit! Your balance: R$ {balance}''')    
        return balance

#=== Main account Menu Loop ===

while (menuLoop):
    if (user_name):
        try:
            menu = int(input(f'''     
              Hello {new_user['name'].split()[0]}! Chose one number:

                1. for Extract
                2. for Withdraw
                3. for Deposit
                4. for End       
                         

              ''')
        )
        except ValueError:
            print('''
              Please enter a valid number.''')    
            continue 
        if (menu == 1):
            print(f'''  
             {''.join(extract)}     
                             ''')
            if ask_menu():
                menuLoop = True
            else:
                menuLoop = False 
        
        elif (menu == 2):
            try:
                withdraw_value = int(input('''
              Value: R$ '''))
            except ValueError:
                print('''
              Please enter a valid number.''')
                continue
            result = withdraw(balance, WITHDRAW_LIMIT, withdraw_times, WITHDRAW_TIMES_LIMIT, withdraw_value)
            if result:
                balance, withdraw_times = result
                ask_menu()

        elif (menu == 3):
            try:
                deposit_value = int(input('''
              Value: R$ '''))
            except ValueError:
                print('''
              Please enter a valid number.''')                       
                continue

            result = deposit(deposit_value, balance, extract)
            if result:
                balance = result
                ask_menu()

    elif (menu == 4):
        print('''
              See ya!''')
        break
    else:    
        print('''
              Please chose one valid option''')
        continue

