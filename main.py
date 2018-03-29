import account_details
import pathlib
import os


print("Welcome to Bank Account Management System\n")

user_account = account_details.UserAccount()


def verify_user_details(account_number):
    path = pathlib.Path(str(account_number) + ".txt")
    if path.exists():
        password = input("Enter password- ")
        file = open(account_number + ".txt", "r")
        found = False
        for line in file:
            if password in line:
                found = True
                break
        if found:
            print("You are logged in successfully")
            return True
        else:
            print("Invalid Password")
            return False
    else:
        print("The account does not exist")
        return False


def create_new_account(user_account=account_details.UserAccount()):
    name = input("Enter your name - ")
    user_account.set_name(name)
    phone = input("Enter your phone number-")
    phone = str(phone)
    user_account.set_phone(phone)
    dob = input("Enter your date of birth - ")
    user_account.set_dob(dob)
    starting_bal = int(input("Enter the starting balance- "))
    user_account.set_starting_balance(starting_bal)
    user_account.set_current_balance(starting_bal)
    password = input("Enter your preferred account password- ")
    user_account.set_password(password)
    user_account.generate_account_number()
    print("Your automatically generated account number is - " + str(user_account.get_account_number()))
    user_account.generate_file()
    return user_account


def access_account_menu(user_account = account_details.UserAccount()):
    print("What operation would you like to perform?- ")
    print("1. Add Balance")
    print("2. Withdraw money")
    print('3. Show balance sheet')
    print('4. Change password')
    print('5. Go to previous menu')
    print('6. Exit Program')
    choice = int(input('Enter option number to continue - '))
    if choice == 1:
        add_amount = int(input("Enter the amount that wish you to add - "))
        transaction_particulars = input("Enter transaction particulars- ")
        user_account.credit_amount(add_amount, transaction_particulars)
        user_account.update_balance_main()
        user_account.update_balance_balancesheet('credit')
        print("Your updated current balance is - " + str(user_account.get_balance()))
        access_account_menu(user_account)
    elif choice == 2:
        subtract_amount = int(input("Enter the amount that you wish to withdraw - "))
        transaction_particulars = input("Enter transaction particulars- ")
        user_account.debit_amount(subtract_amount, transaction_particulars)
        user_account.update_balance_main()
        user_account.update_balance_balancesheet('debit')
        print("Your updated current balance is - " + str(user_account.get_balance()))
        access_account_menu(user_account)
    elif choice == 3:
        user_account.print_balance_sheet()
    elif choice == 4:
        print("We will need more info for verification.")
        date_birth = input("Please enter your date of birth in dd/mm/yyyy format only - ")
        phone_number = input("Please enter your phone number - ")
        if date_birth == user_account.get_dob() and phone_number == user_account.get_phone():
            new_password = input("Enter new password - ")
            user_account.set_password(new_password)
            user_account.generate_file()
            print("Your account password has been updated!")
            access_account_menu(user_account)
        else:
            print("You entered the wrong details.")
            access_account_menu(user_account)
    elif choice == 5:
        pass
    elif choice == 6:
        exit(0)
    else:
        print("Please enter a valid option.")
        access_account_menu(user_account)
    return user_account


while True:
    print("What operation would you like to perform?- ")
    print("1. Access account")
    print("2. Create a new account")
    print('3. Delete account')
    print('4. Exit')
    choice = int(input('Enter option number to continue - '))
    if choice == 1:
        print('You are accessing a pre-existing account')
        account_number = input("Enter account number- ")
        if verify_user_details(account_number):
            file = open(account_number + ".txt", "r+")
            user_account.get_info_from_file(file)
            user_account = access_account_menu(user_account)
        else:
            print("You entered the wrong details")

    elif choice == 2:
        print('You are creating a new  account')
        user_account = create_new_account()
    elif choice == 3:
        print('You are deleting an existing account')
        delete_account_number = input("Enter the account number- ")
        path = pathlib.Path(delete_account_number + ".txt")
        if path.exists():
            password = input("Enter password- ")
            file = open(delete_account_number + ".txt", "r")
            found = False
            for line in file:
                if password in line:
                    found = True
                    file.close()
                    os.remove(delete_account_number + ".txt")
                    os.remove(delete_account_number + "-balancesheet.txt")
                    print("The account has been deleted!")
                    break
            if found:
                pass
            else:
                print("You entered the wrong password!")
        else:
            print("The account does not exist.")

    elif choice == 4:
        print("Exiting the program now")
        exit(0)
    else:
        print('Invalid option selection')
