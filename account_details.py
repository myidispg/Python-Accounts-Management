import random
import datetime


class UserAccount:

    current_balance = None
    name = None
    phone = None
    starting_balance = None
    transaction_particulars = None
    account_number = None
    password = None
    date_of_birth = None

    def credit_amount(self, amount, particulars):
        self.current_balance += amount
        self.transaction_particulars = particulars

    def debit_amount(self, amount, particulars):
        self.current_balance -= amount
        self.transaction_particulars = particulars

    def set_current_balance(self, balance):
        self.current_balance = balance

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_starting_balance(self, starting_balance):
        self.starting_balance = starting_balance

    def set_password(self, password):
        self.password = password

    def set_dob(self, dob):
        self.date_of_birth = dob

    def generate_account_number(self):
        self.account_number = random.randrange(1000, 10000)

    def get_balance(self):
        return self.current_balance

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_starting_balance(self):
        return self.starting_balance

    def get_password(self):
        return self.password

    def get_dob(self):
        return self.date_of_birth

    def get_account_number(self):
        return self.account_number

    def generate_file(self):
        file = open(str(self.account_number) + ".txt", "w")
        file.write("Account Number-" + str(self.account_number) + "\n")
        file.write("Password-" + str(self.password) + "\n")
        file.write("Name-" + str(self.name) + "\n")
        file.write("Phone Number-" + str(self.phone) + "\n")
        file.write("Date of birth-" + str(self.date_of_birth) + "\n")
        file.write("Starting Balance-" + str(self.starting_balance) + "\n")
        file.write("Current Balance-" + str(self.current_balance) + "\n")
        file.close()
        file = open(str(self.account_number) + "-balancesheet.txt","w")
        file.write(str(datetime.date.today()) + " Account created +" + str(self.starting_balance) + "\n")
        file.close()

    def get_info_from_file(self, file):
        contents = file.read()
        file.close()
        x = contents.split("\n")

        for line in x:
            if "Account Number" in line:
                y = line.split("-")
                self.account_number = y[1]
            if "Password" in line:
                y = line.split("-")
                self.password = y[1]
            if "Name" in line:
                y = line.split("-")
                self.name = y[1]
            if "Phone Number" in line:
                y = line.split("-")
                self.phone = y[1]
            if "Date of birth" in line:
                y = line.split("-")
                self.date_of_birth = y[1]
            if "Starting Balance" in line:
                y = line.split("-")
                self.starting_balance = int(y[1])
            if "Current Balance" in line:
                y = line.split("-")
                self.current_balance = int(y[1])

    def update_balance_main(self):
        file = open(str(self.account_number) + ".txt", "r")
        lines = file.readlines()
        file.close()
        file = open(str(self.account_number) + ".txt", "w")
        for line in lines:
            if "Current Balance" in line:
                pass
            else:
                file.write(line)
        file.write("Current Balance-" + str(self.current_balance) + "\n")
        file.close()

    def update_balance_balancesheet(self, action):
        file = open(str(self.account_number) + "-balancesheet.txt", "a")
        if action == 'credit':
            file.write(
                str(datetime.date.today()) + " " + str(self.transaction_particulars) + " +" + str(self.starting_balance)
                + "\n")
        else:
            file.write(
                str(datetime.date.today()) + " " + str(self.transaction_particulars) + " -" + str(self.starting_balance)
                + "\n")
        file.close()

    def print_balance_sheet(self):
        file = open(str(self.account_number) + "-balancesheet.txt", "r")
        contents = file.read()
        print(contents)







