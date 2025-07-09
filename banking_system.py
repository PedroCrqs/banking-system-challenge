print('''
              Hello, welcome to the Banking System!''')
user_name = input('''
              What is your name? ''')
balance = 500
WITHDRAW_LIMIT = 500
WITHDRAW_TIMES_LIMIT = 3
withdraw_times = 0
menuLoop = True

def ask_menu():
    toDo = int(input('''
                     
              What do you want to do?
                      
                1. for menu
                2. for end
                      
              '''))
    return toDo == 1

def withdraw(balance: int, withdraw_limit: int, withdraw_times: int, withdraw_times_limit: int, withdraw_value: int) -> tuple:
    if withdraw_value <= 0:
        print('Please enter a positive value.')
        return
    elif (withdraw_value > balance or withdraw_value > withdraw_limit or withdraw_times >= withdraw_times_limit):
        print('Unauthorized transaction')
        return
    else:
        balance -= withdraw_value
        withdraw_times += 1
        print(f'Sucessfull withdraw! Your balance: R$ {balance}')
        return balance, withdraw_times
    
while (menuLoop):
    if (user_name):
        try:
            menu = int(input(f'''     
              Hello {user_name}! Chose one number:
              
                1. for balance
                2. for withdraw
                3. for deposit
                4. for end       
                         

              ''')
        )
        except ValueError:
            print('''
              Please enter a valid number.''')    
            continue 
        if (menu == 1):
            print(f'''
              Balance: R$ {balance}
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
            withdraw(balance, WITHDRAW_LIMIT, withdraw_times, WITHDRAW_TIMES_LIMIT, withdraw_value)

        elif (menu == 3):
            try:
                deposit_value = int(input('''
              Value: R$ '''))
            except ValueError:
                print('''
              Please enter a valid number.''')                       
                continue    
            if deposit_value <= 0:
                print('Please enter a positive value.')
                continue
            else:
                balance += deposit_value
                print(f'''
                      
              Sucessfull deposit! Your balance: R$ {balance}''')    
                if ask_menu():
                    menuLoop = True
                else:
                    menuLoop = False 
    elif (menu == 4):
        print('''
              See ya!''')
        break
    else:    
        print('''
              Please chose one valid option''')
        continue

