from helpers import  create_new_user_helper, create_new_account_helper, get_account_balance_helper, deposit_into_account_helper

print('------------------------\nWelcome to the Bank!\n------------------------\n')

if __name__ == '__main__':
    task = input('What would you like to do?\n\n'
                            'Enter \"1\" to Create User\n'
                            'Enter \"2\" to Create Account\n'
                            'Enter \"3\" to Check Account Balance\n'
                            'Enter \"4\" to Deposit Money\n'
                            '------------------------\n\n')

    if task == "1":
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        email = input('Enter your email: ')
        dob = input('Enter you date of birth (YYYY-MM-DD): ')
        password = input('Enter a password: ')

        create_new_user_helper(first_name, last_name, email, dob, password)

    elif task == "2":
        email = input('Enter your email: ')

        create_new_account_helper(email)


    elif task == "3":
        email = input('Enter email: ')
       
        Account = get_account_balance_helper(email)
        print(" Your balance is " + str(Account.Balance))


    elif task == "4":
        email = input('Enter email: ')
        amount = input('How much are you depositing? ')

        deposit_into_account_helper(email, amount)

