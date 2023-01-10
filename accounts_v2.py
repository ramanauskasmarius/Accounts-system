from getpass import getpass

class User:

    def __init__(self, email, password, name, lastname):

        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
    
class Account(User):

    def __init__(self, email, password, name, lastname, balance):

        super().__init__(email, password, name, lastname)

        self.balance = balance
        

    def account_info(self):

        print('Your account information:')

        print(f'Your name: {self.name}')
        print(f'Your lastname: {self.lastname}')
        print(f'Your email adress: {self.email}')
        print(f'Your current balance: {self.balance}')

    def deposit(self, amount):

        self.amount = amount

        self.balance = self.balance + self.amount

        print (f'Your updated balance is: {self.balance}')

    def withdraw(self, amount):

        self.amount = amount

        if self.amount > self.balance:

            print('Not enough money in account')
            print (f'Your current balance is: {self.balance}')

        else:
            
            self.balance = self.balance - self.amount

            print (f'Your updated balance is: {self.balance}')

    def transfer(self, amount):

        self.amount = amount

        if self.amount > self.balance:

            print('Not enough money in account')
            print (f'Your current balance is: {self.balance}')

        else:
            
            self.balance = self.balance - self.amount

            print (f'You have successfuly transfered {self.amount}')

            print (f'Your updated balance is: {self.balance}')

    def receive(self, amount):

        self.amount = amount

        self.balance = self.balance + self.amount



def all_users(all_accounts):

    with open('accounts.txt', 'r') as f:

            for line in f.readlines():

                temp = line.rstrip()

                email, password, name, lastname, balance= temp.split('|')

                all_accounts.append(Account(email, password, name, lastname, int(balance)))

    return all_accounts


def register(all_accounts):
    
    while True:

        entered_email = input('Enter email: ')

        if check_if_exists(entered_email, all_accounts):

            break

        else:

            print('This email is already in use.')
            continue

    name = input('Enter your name: ')
    lastname = input('Enter your lastname: ')

    while True:

        entered_password = getpass('Enter password: ').lower()
        entered_password2 = getpass('Confirm your password: ').lower()

        if entered_password == entered_password2:

            break

        else:

            print('Your passwords dont match, try again.')
            continue
        
            
    all_accounts.append(Account(entered_email, entered_password, name, lastname))
    write_to_file(entered_email, entered_password, name, lastname) 
    return all_accounts



def check_if_exists(entered_email, all_accounts):

    for i in range(len(all_accounts)):

        if entered_email == all_accounts[i].email:

            return False

    return  True

        
    
def write_to_file(entered_email, entered_password, name, lastname):

    with open('accounts.txt', 'a') as f:

        f.write(entered_email + '|' + entered_password + '|' + name + '|' + lastname + '|' + '0' + '\n')



def login(all_accounts):

    while True:

        email = input ('Enter email: ')
        password = getpass ('Enter password: ')

        for i in range(len(all_accounts)):

            if email == all_accounts[i].email and password == all_accounts[i].password:

                print('Successfuly logged in.')
                return i

            else:

                continue
        
        print('Wrong email or password')
        print('T to try again or X to exit')
        choice = input('').lower()

        if choice == 'x':

            return False

        else:

            continue

def update_accounts(all_accounts):

    with open('accounts.txt', 'w') as f:

        for i in range(len(all_accounts)):

            f.write(all_accounts[i].email + '|' + all_accounts[i].password + '|' + all_accounts[i].name + '|' + all_accounts[i].lastname + '|' + str(all_accounts[i].balance) +'\n')





all_accounts = []



all_accounts = all_users(all_accounts)


while True:

    print("Choose number from menu:")
    print('1. Register')
    print('2. Login')
    print('3. Exit')

    choose = input()

    if choose == '1':

        register(all_accounts)

    elif choose == '2':

        i = login(all_accounts)

        if i > -1:

            while True:

                print("Choose number from menu:")
                print('0. Account information')
                print('1. Update name')
                print('2. Update lastname')
                print('3. Deposit')
                print('4. Withdraw')
                print('5. Transfer')
                print('6. Check balance')
                print('7. Exit')

                choice = input()

                if choice == '0':

                    all_accounts[i].account_info()
                    continue

                if choice == '1':

                    all_accounts[i].name = input('Enter name: ')

                    update_accounts(all_accounts)
                    continue

                elif choice == '2':

                    all_accounts[i].lastname = input('Enter lastname: ')

                    update_accounts(all_accounts)
                    continue

                elif choice == '3':

                    while True:

                        amount = int(input('How much would you like to deposit? '))

                        if int(amount):

                            all_accounts[i].deposit(amount)
                            break

                        else:

                            print('You entered wrong number.')
                            continue

                    update_accounts(all_accounts)
                    continue

                elif choice == '4':

                    while True:

                        amount = int(input('How much would you like to withdraw? '))

                        if int(amount):

                            all_accounts[i].withdraw(amount)
                            break

                        else:

                            print('You entered wrong number.')
                            continue

                    update_accounts(all_accounts)
                    continue

                elif choice == '5':

                    while True: 

                        print("Enter receiver's information:")

                        receiver_email = input('Enter email: ')
                        receiver_name = input('Enter name: ')
                        receiver_lastname = input('Enter lastname: ')

                        for v in range(len(all_accounts)):

                            if all_accounts[v].email == receiver_email and all_accounts[v].name == receiver_name and all_accounts[v].lastname == receiver_lastname:

                                amount = int(input('How much money you would like to send? '))

                                if all_accounts[i].balance >= int(amount):

                                    all_accounts[i].transfer(amount)
                                    all_accounts[v].receive(amount)
                                    


                            else:

                                continue
                        update_accounts(all_accounts)
                        break



                elif choice == '6':

                    print(f'Your current balance is: {all_accounts[i].balance}')


                else:

                    break



    elif choose == '3':

        break

    else:

        continue