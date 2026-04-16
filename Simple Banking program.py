def show_balance():
    print(f'Your balance is ${balance:.2f}')


def deposit():
    amount = float(input('Enter an amount to be deposited: '))

    if amount < 0:
        print('Amount cannot be less than zero')
        return 0
    else:
        return amount
    

def withdraw():
    amount = float(input('Enter the amount to be withdrawn: '))
    if amount > balance:
        print('Insufficient funds')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0')
        return 0
    else:
        return amount

    

balance = 0
is_running = True

while is_running:
    print('Banking program')
    print('1 Show Balance')
    print('2 Deposit')
    print('3 Withdraw')
    print('4 Exit')

    choise = input('Enter your choise (1-4): ')

    if choise == '1':
        show_balance()
        
    elif choise == '2':
      balance += deposit()
    elif choise == '3':
       balance -= withdraw()
    elif choise == '4':
        is_running = False
    else:
        print('That is not a valid choise')

print('Thank you have a nice day')
    
