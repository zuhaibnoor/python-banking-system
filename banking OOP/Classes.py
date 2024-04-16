#_______________________________________________________________ Import ______________________________________________________________
from customtkinter import *
import os
import datetime
import random
from CTkMessagebox import CTkMessagebox
from abc import ABC, abstractmethod
date_time = datetime.datetime.now()

#___________________________________________________________ Account Class ___________________________________________________________

class Account(ABC):
    def __init__(self):
        self.Account_No =[]
        self.balance = None
#                        ______________________ Create Account number (Saving,Loan,Checking) ______________________
    @staticmethod
    def get_random_account():
        prefix = random.randint(10, 99)
        number = random.randint(1e9, 1e10 - 1)
        check = int((prefix * 1e10) + number) % 97
        return f"{prefix:0>2d}-{number:0>10d}-{check:0>2d}"
    def Create_Account_No(self):
        while True:
            account = self.get_random_account()
            if account not in self.Account_No:
                self.Account_No.append(account)
                return account

#                        ______________________ Create Account (Saving,Loan,Checking) ______________________
    @abstractmethod
    def Create_Accounts(self):
        pass

#                        ______________________ Check Account (Saving,Loan,Checking) ______________________
    @abstractmethod
    def Check_Account_No(self,account_no):
        pass

#                        ______________________ Login (Saving,Loan,Checking) ______________________________
    @abstractmethod
    def Login(self,account_no):
       pass

#                        ______________________ Withdraw Amount(Saving,Loan,Checking) ______________________
    @abstractmethod
    def With_Draw(self,amount):
        pass

#                        ______________________ Deposit Amount (Saving,Loan,Checking) ______________________
    @abstractmethod
    def Deposit(self,amount):
        pass

#                        ______________________ BAlance Enquiry _____________________________________________
    def BalanceEnquiry(self):
        return f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nBalance:{self.balance}"

# ___________________________________________________________ Saving Account Class ___________________________________________________________

class Saving_Account(Account):

    def __init__(self,custmr):
        self.Client = custmr
        super().__init__()

#                        ______________________ SignUp For Saving Class _____________________________________
    def Create_Accounts(self):
        account_no = self.Create_Account_No()
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[1]
            dict[account_no] = ["0","Saving"]
            file[1] = dict
            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                f.write(str(file))
        CTkMessagebox(message = f"Your Account number is: {account_no}",title = "Account Number ")

#                        ______________________ Check AccountNo for Saving Class ___________________________
    def Check_Account_No(self,account_no):
        with open(f"users/{self.Client.User_Name}.txt") as check:
            check = eval(check.read())
            check=check[1]
            if account_no in check:
                return True
            else:
                CTkMessagebox(message="Invalid Account Number", title="Error", icon="cancel")

#                        ______________________ LogIn for Saving Class _____________________________________
    def Login(self,account_no):
        self.Account_no = account_no
        return self.Check_Account_No(account_no)

#                        ______________________ Deposit for Saving Class ___________________________________
    def Deposit(self,amount):
        if amount.isdigit():
            self.amount = int(amount)
            with open(f"users/{self.Client.User_Name}.txt") as file:
                file = eval(file.read())
                dict = file[1]
                dict_ = dict.get(self.Account_no)
                Item = dict_[0]
                if Item == '0':
                    self.Interest = self.amount * 0.2 * 1                  # 1 shows that for one year interest
                    self.balance = int(self.Interest) + self.amount
                else:
                    self.Interest = self.amount * 0.2 * 1                   # 1 shows that for one year interest
                    self.balance = int(Item)+int(self.Interest)+self.amount
                dict[self.Account_no] = [str(self.balance),"saving"]
                file[1] = dict
                file[4]["Saving"].append([str(self.Account_no),"deposit",str(self.amount),str(date_time.date())])
                with open(f"users/{self.Client.User_Name}.txt","w") as f:
                    f.write(str(file))
            msg=CTkMessagebox(message="Your Amount is Successfully Deposit", title="Deposit", icon="check",option_1="continue")
            if msg.get() == "continue":
                CTkMessagebox( message=f"{super().BalanceEnquiry()}\nDeposit Amount:{self.amount}\nInterest:{self.Interest}\nAccount No:{self.Account_no}", title="Deposit info", icon="check")
        else:
            CTkMessagebox(message="Invalid Amount",title="Error",icon="cancel")

#                        ______________________ WithDraw for Saving Class ___________________________________
    def With_Draw(self,amount):
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[1]
            dict_ = dict.get(self.Account_no)
            Item= int(dict_[0])
        if amount.isdigit() and int(amount)<=Item:
            self.balance = Item-int(amount)
            dict[self.Account_no] = [str(self.balance),"saving"]
            file[1] = dict
            file[4]["Saving"].append([str(self.Account_no), "WithDraw", str(amount), str(date_time.date())])
            with open(f"users/{self.Client.User_Name}.txt","w") as f:
                    f.write(str(file))
            msg = CTkMessagebox(message="Your Amount has been Successfully WithDrawn", title="Deposit", icon="check",
                                option_1="continue")
            if msg.get() == "continue":
                CTkMessagebox( message = f"{super().BalanceEnquiry()}\nWith Draw:{amount}\nAccount No:{self.Account_no}", title = "Withdraw info", icon="check" )
        else:
            CTkMessagebox(message="Invalid Amount", title="Error")

#                        ______________________ Current Balance for Saving Class ____________________________
    def BalanceEnquiry(self):
        with open(f"users/{self.Client.User_Name}.txt") as f:
            f = eval(f.read())
            list = f[1][self.Account_no]
            return list[0]

# ___________________________________________________________ Checking Account Class ___________________________________________________________

class Checking_Account(Account):

    def __init__(self,custmr):
        self.Client = custmr
        super().__init__()

#                        ______________________ SignUp for Checking Class __________________________________
    def Create_Accounts(self):
        account_no = self.Create_Account_No()
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[2]
            dict[account_no] = ["0","checking"]
            file[2] = dict
            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                f.write(str(file))
        CTkMessagebox(message=f"Your Account number is: {account_no}", title="Account Number ")

#                        ______________________ Check AccountNo for Checking Class __________________________
    def Check_Account_No(self,account_no):
        with open(f"users/{self.Client.User_Name}.txt") as check:
            check = eval(check.read())
            check=check[2]
            if account_no in check:
                return True
            else:
                CTkMessagebox(message="Invalid Account Number", title="Error", icon="cancel")

#                        ______________________ LogIn for Checking Class ____________________________________
    def Login(self, account_no):
        self.Account_no=account_no
        return self.Check_Account_No(account_no)

#                        ______________________ WithDraw for Checking Class _________________________________
    def With_Draw(self,amount):
        self.WithDraw = int(amount)
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[2]
            dict_ = dict.get(self.Account_no)
            self.balance = int(dict_[0])
            self.credit_limit = -10000
        if self.WithDraw <= self.balance + abs(self.credit_limit):
                self.balance -= self.WithDraw
                dict[self.Account_no] = [str(self.balance), "checking"]
                file[2] = dict
                file[4]["Checking"].append([str(self.Account_no), "WithDraw", str(amount), str(date_time.date())])
                with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                    f.write(str(file))
                msg = CTkMessagebox(message="Your Amount has been Successfully WithDrawn", title="Deposit",
                                    icon="check", option_1="continue")
                if msg.get() == "continue":
                    CTkMessagebox(
                        message=f"{super().BalanceEnquiry()}\nWith Draw:{self.WithDraw}\nAccount No:{self.Account_no}",
                        title="Withdraw info", icon="check")
        else:
            CTkMessagebox(message="Credit Limit has been Exceeded", title="Error")

#                        ______________________ Deposit for Checking Class _________________________________
    def Deposit(self,amount):
        if amount.isdigit():
            self.amount = int(amount)
            with open(f"users/{self.Client.User_Name}.txt") as file:
                file = eval(file.read())
                dict = file[2]
                dict_= dict.get(self.Account_no)
                Item = dict_[0]
                if Item == "0":
                    self.balance = self.amount
                    dict[self.Account_no] = [str(self.amount),"checking"]
                else:
                    self.balance = int(Item)+ self.amount
                    dict[self.Account_no] = [str(self.balance),"checking"]
                file[2] = dict
                file[4]["Checking"].append([str(self.Account_no), "Deposit", str(self.amount), str(date_time.date())])
                with open(f"users/{self.Client.User_Name}.txt","w") as f:
                    f.write(str(file))
            msg = CTkMessagebox(message="Your Amount is Successfully Deposit", title="Deposit", icon="check",
                                option_1="continue")
            if msg.get() == "continue":
                CTkMessagebox( message = f"{super().BalanceEnquiry()}\nDeposit Amount:{self.amount}\nAccount Number:{self.Account_no}",title = "Deposit Info",icon = "check")
        else:
            CTkMessagebox(message="Invalid Amount", title="Error", icon="cancel")

#                        ______________________ Current Balance for Checking Class ___________________________
    def BalanceEnquiry(self):
        with open(f"users/{self.Client.User_Name}.txt") as f:
            f = eval(f.read())
            list = f[2][self.Account_no]
            return list[0]

# ___________________________________________________________ Loan Account Class ___________________________________________________________

class Loan_Account(Account):

    def __init__(self,custmr):
        self.Client = custmr
        super().__init__()

#                        ______________________ SigUp for Loan Class ________________________________________
    def Create_Accounts(self):
        account_no = self.Create_Account_No()
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[3]
            dict[account_no] = ["0","Loan","",""]
            file[3] = dict
            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                f.write(str(file))
        CTkMessagebox(message=f"Your Account number is: {account_no}", title="Account Number ")

#                        ______________________ Check Account for Laon Class ________________________________
    def Check_Account_No(self,account_no):
        with open(f"users/{self.Client.User_Name}.txt") as check:
            check = eval(check.read())
            check = check[3]
            if account_no in check:
                return True
            else:
                CTkMessagebox(message="Invalid Account Number", title="Error", icon="cancel")

#                        ______________________  LogIn for Laon Class _______________________________________
    def Login(self,account_no):
        self.Account_no = account_no
        return self.Check_Account_No(account_no)
#                        ________________________ Debit Limit for Loan Class ________________________________
    def Debit_limit(self,amount,year, month, day):
            self.Principle_Amount = int(amount)
            if self.Principle_Amount < 5000:
                CTkMessagebox(message="Minimum Amount for getting loan is 5000 ", title="Error", icon="cancel")
                return True
            elif 50000 >= self.Principle_Amount >= 5000:
                self.interest =  int(self.Principle_Amount / 10)
                self.balance = int(self.Principle_Amount + self.interest)
            elif self.Principle_Amount >50000:
                self.interest = int( self.Principle_Amount / 5)
                self.balance = int(self.Principle_Amount + self.interest)
            with open(f"users/{self.Client.User_Name}.txt") as file:
                file = eval(file.read())
                dict = file[3]
                dict_ = dict.get(self.Account_no)
                Item = dict_[0]
                if Item == '0':
                    dict[self.Account_no] = [str(self.balance),"loan",f"{self.Loan_Duration.year}-{self.Loan_Duration.month}-{self.Loan_Duration.day}",""]
                else:
                    dict[self.Account_no] = [str(self.balance+int(Item)),"loan",f"{self.Loan_Duration.year}-{self.Loan_Duration.month}-{self.Loan_Duration.day}",""]
                file[3] = dict
                file[4]["Loan"].append([str(self.Account_no), "WithDraw", str(amount), str(date_time.date())])
            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                    f.write(str(file))
            msg = CTkMessagebox(message="Loan Granted", title="Loan", icon="check",
                                option_1="continue")
            if msg.get() == "continue":
                CTkMessagebox(message=f"{super().BalanceEnquiry()}\nPrincipal Amount:{self.Principle_Amount}\nInterest:{self.interest}\nLoan Duration Time:{year}-{month}-{day} "
                                      f"\nAccount Number:{self.Account_no}", title="Deposit Info", icon="check")

#                        ______________________ Loan Duration for Laon Class _________________________________
    def With_Draw(self,year,month,day,amount):
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[3]
            dict_ = dict.get(self.Account_no)
            Time = dict_[2]
        months = {"1":31,"2":28,"3":31,'4':30,'5':31,'6':30,'7':31,'8':31, "9":30, "10":31,"11":30,"12":31 }  # Dictionary to months to check Day ( 30 or 31)
        if year.isdigit() and month.isdigit() and day.isdigit() and amount.isdigit():
            if  date_time.year < int(year) <= date_time.year+1:
                if 0 < int(month) <= int(12):
                    if 0 <= int(day) <= months.get(month):
                        self.Loan_Duration = datetime.datetime(int(year), int(month),int(day))
                        if  Time != "":
                            CTkMessagebox(message="Please !! Pay the loan First", title="Error", icon="warning")
                        else:
                            self.Debit_limit(amount,year, month, day)
                    else:
                        CTkMessagebox(message="Invalid Day.", title="Error", icon="warning")
                else:
                    CTkMessagebox(message="Invalid Month.", title="Error",icon="warning")
            elif  date_time.year == int(year) <= date_time.year+1:
                if int(date_time.month) <= int(month) <= int(12):
                    if 0 <= int(day) <= months.get(month):
                        self.Loan_Duration = datetime.datetime(int(year), int(month),int(day))
                        if  Time != "":
                            CTkMessagebox(message="Please !! Pay the loan First", title="Error", icon="warning")
                        else:
                            self.Debit_limit(amount,year, month, day)
                    else:
                        CTkMessagebox(message="Invalid Day.", title="Error", icon="warning")
                else:
                    CTkMessagebox(message="Invalid Month.", title="Error",icon="warning")
            else:
                CTkMessagebox(message="Invalid year.", title="Error", icon="warning")
        else:
            CTkMessagebox(message="Invalid Entries", title="Error", icon="warning")

#                        ______________________ Deposit for Laon Class ______________________________________
    def Deposit(self,amount):
        if amount.isdigit():
                self.amount = int(amount)
                with open(f"users/{self.Client.User_Name}.txt") as file:
                    file = eval(file.read())
                    dict = file[3]
                    dict_ = dict.get(self.Account_no)
                    principle_amount = float(dict_[0])
                    date = dict_[2]
                if date != "":
                    date =date.split("-")
                    date = [ int(i) for i in date]
                    date = datetime.datetime(date[0],date[1],date[2])
                    if date.date() < date_time.date():
                            if self.amount == principle_amount:
                                dict_[0] = "0"
                                dict_[2] = ''
                                dict_[3] = 'Deposited'
                                dict[self.Account_no] = dict_
                                file[3] = dict
                                file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                                with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                    f.write(str(file))
                                CTkMessagebox(message=f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrincipal Amount:0 Rs/="
                                            f"\nAccount Number:{self.Account_no}", title="Deposit Info", icon="check")
                            elif self.amount < (principle_amount):
                                self.balance = (principle_amount) - self.amount
                                dict_[0] = str(self.balance)
                                dict_[3]="Deposited"
                                dict[self.Account_no] = dict_
                                file[3] = dict
                                file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                                with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                    f.write(str(file))
                                CTkMessagebox(message = f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrincipal Amount:{self.balance}"
                                            f"\nAccount Number:{self.Account_no}\nLoan Duration Time:{date.date()}", title="Deposit Info", icon="check")
                            elif self.amount > (principle_amount):
                                amount_left = self.amount- (principle_amount)
                                dict_[0] = "0"
                                dict_[2] = ''
                                dict[self.Account_no] = dict_
                                file[3] = dict
                                file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                                with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                    f.write(str(file))
                                CTkMessagebox(message=f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrinciple amount: 0 Rs/=\n\
                                The extra amount {amount_left}Rs has been returned\nAccount no: {self.Account_no}", title="Loan Deposit Info", icon="check")
                    elif date.date() >= date_time.date():
                        if  self.amount == (principle_amount):
                            self.balance = 0
                            dict_[0] = str(self.balance)
                            dict_[2]= ''
                            dict[self.Account_no] = dict_
                            file[3] = dict
                            file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                f.write(str(file))
                            CTkMessagebox( message=f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrincipal Amount:0 Rs/="
                                        f"\nAccount Number:{self.Account_no}",title="Deposit Info", icon="check")
                        elif self.amount < (principle_amount):
                            self.balance = principle_amount-self.amount
                            dict_[0] = str(self.balance)
                            dict[self.Account_no] = dict_
                            file[3] = dict
                            file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                f.write(str(file))
                            CTkMessagebox(message=f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrincipal Amount:{self.balance}"
                                        f"\nAccount Number:{self.Account_no}\nLoan Duration Time:{date.date()}",
                                title="Deposit Info", icon="check")
                        elif self.amount > (principle_amount):
                            amount_left= self.amount-principle_amount
                            dict_[0] = "0"
                            dict_[2] = ''
                            dict[self.Account_no] = dict_
                            file[3] = dict
                            file[4]["Loan"].append([str(self.Account_no), "Deposit", str(amount), str(date_time.date())])
                            with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                                f.write(str(file))
                            CTkMessagebox(message=f"Date:{date_time.date()}\nTime:{date_time.strftime('%H:%M:%S')}\nDeposit:{self.amount}\nPrinciple amount: 0 Rs/=\n\
                                                        The extra amount {amount_left}Rs has been returned\nAccount no:{self.Account_no}",title="Loan Deposit Info", icon="check")
                else:
                    CTkMessagebox(message="Please !! Take loan and then Deposit", title="Error", icon="cancel")
        else:
            CTkMessagebox(message="Invalid Amount", title="Error", icon="cancel")

#                        ______________________ Current Balance for Laon Class _______________________________
    def BalanceEnquiry(self):
        with open(f"users/{self.Client.User_Name}.txt") as file:
            file = eval(file.read())
            dict = file[3]
            dict_ = dict.get(self.Account_no)      # list of any Account number belong to Loan
            principle_amount = float(dict_[0])     # Get principal amount if present in list
            date = dict_[2]                        # Get loan duration date if present in list
            if date != "":
                date = date.split("-")
                date = [int(i) for i in date]
                date = datetime.datetime(date[0], date[1], date[2])
                if dict_[3] == "Deposited":
                    pass
                elif dict_[3]!="Deposited":
                    if date.date() < date_time.date():
                        principle_amount *= 1.2    # penalty for the customer incase he/she does not repay loan on time.
                        dict_[3] = "Deposited"
                dict_[0] = str(principle_amount)
                dict[self.Account_no] = dict_
                file[3] = dict
                with open(f"users/{self.Client.User_Name}.txt", "w") as f:
                    f.write(str(file))
                return str(principle_amount), str(date.date())
            else:
                return "0 Rs","No loan!"

# ___________________________________________________________ Customer Class ___________________________________________________________
class Customer:

#                        ______________________  Main SignUp for Customer ___________________________________
    def Sign_UP(self,firstname,lastname,username,password):
        self.first_Name = firstname
        self.last_Name = lastname
        self.User_Name = username
        self.password = password
        Users_list = []
        if self.first_Name != '' and self.last_Name != '' and self.User_Name != '' and self.password != '':
            for i in os.listdir("users/"):
                Users_list.append(i)
            if f"{self.User_Name}.txt" not in Users_list:
                with open (f"users/{self.User_Name}.txt","w") as record:
                    list = [{str(self.User_Name):str(self.password)},{},{},{},{"Saving":[],"Checking":[],"Loan":[]}]
                    record.write(str(list))
                CTkMessagebox(message="Your account has been created!", title="Account Created", icon="check")
            else:
                CTkMessagebox(message="Please! Enter Unique Username", title="Error", icon="warning")
        else:
            CTkMessagebox(message="Empty Entries", title="Error", icon="warning")

#                        ______________________  Main LogIN for Customer ____________________________________
    def LogIn(self, username, pswd):
        self.User_Name = username
        self.password = pswd
        if self.User_Name !='' and self.password !='':
            try:
                with open(f"users/{self.User_Name}.txt","r") as check:
                    check = eval(check.read())
                    check = check[0]
                    for dict in check:
                        if check[dict] == self.password:
                            return True
                        else:
                            CTkMessagebox(title="Error", message="Incorrect password", icon="cancel")

            except:
                CTkMessagebox(title="Error", message="Incorrect username", icon="cancel")
        else:
            CTkMessagebox(message="Empty Entries", title="Error", icon="warning")

#                        ______________________  Forgot Password for Customer ________________________________
    def Forgot_Password(self,username, new_pswd, conf_pswd):
        self.User_Name = username
        if self.User_Name != '' and new_pswd !='' and conf_pswd != '':
            try:
                with open(f"users/{self.User_Name}.txt") as f:
                    if new_pswd == conf_pswd:
                        f_data = f.read()
                        f__ = eval(f_data)
                        f_dict = f__[0]
                        f_dict[username] = conf_pswd
                        f__[0] = f_dict
                        with open(f"users/{self.User_Name}.txt", "w") as f_:
                            f_.write(str(f__))
                            CTkMessagebox(title="Reset Password", message="Password has been reset", icon="info")
                    else:
                        CTkMessagebox(title="Error", message="Incorrect password", icon="cancel")
            except:
                CTkMessagebox(title="Error", message="Incorrect username", icon="cancel")
        else:
            CTkMessagebox(message="Empty Entries", title="Error", icon="warning")


# ______________________________________________________ Administrator Class ______________________________________________________

class Administrator:

#                        ______________________  Main LogIN for Admin ____________________________________
    def Log_In(self, id, pswd):
        self.Admin_ID = id
        self.Admin_pswd = pswd
        with open("admin.txt",'r') as file:
            file = eval(file.read())
            if self.Admin_ID == file[0]:
                if self.Admin_pswd == file[1]:
                    return True
                else:
                    CTkMessagebox(title="Error", message="Invalid Password", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="Invalid User Name", icon="cancel")

#                        ______________________  Chamge Password for Admin ____________________________________
    def Change_pswd(self, Admin_ID, old_pswd, new_pswd):
        with open("admin.txt") as file:
            f = eval(file.read())

            Admin_ID = Admin_ID
            old_pswd = old_pswd
            new_pswd = new_pswd

            if Admin_ID == f[0]:
                if old_pswd == f[1]:
                    if new_pswd != '':
                        if old_pswd != new_pswd:
                            f[1] = str(new_pswd)
                            with open("admin.txt", "w") as file:
                                file.write(f"{str(f)}")
                                CTkMessagebox(title="Admin password", message="Admin password has been changed.",
                                              icon="info")
                        else:
                            CTkMessagebox(title="Error", message="New and Old password cannot be same.",
                                          icon="cancel")
                    else:
                        CTkMessagebox(title="Error", message="New password field cannot be left empty.",
                                      icon="cancel")
                else:
                    CTkMessagebox(title="Error", message="Invalid Password", icon="cancel")
            else:
                CTkMessagebox(title="Error", message="Invalid Admin Username", icon="cancel")

#                        ______________________ To show bank info to admin__________________________________
    def Bank_info(self):
        files = os.listdir("users/")
        return files