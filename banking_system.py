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
            if withdraw_value <= 0:
                print('''
              Please enter a positive value.''')
                continue
            elif (withdraw_value > balance or withdraw_value > WITHDRAW_LIMIT or withdraw_times >= WITHDRAW_TIMES_LIMIT):
                print('''
              Unauthorized transaction''')
            else:
                balance -= withdraw_value
                withdraw_times += 1
                toDo = int(input(f'''
                      
              Sucessfull withdraw! Your balance: R$ {balance}'''))  
                if ask_menu():
                    menuLoop = True
                else:
                    menuLoop = False 
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
                toDo = int(input(f'''
                      
              Sucessfull deposit! Your balance: R$ {balance}'''))    
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

