import tkinter
from Classes import *


root = CTk()
set_appearance_mode("dark")
set_default_color_theme("green")
w = 850
h = 600
root.geometry(f"{w}x{h}")
root.title("EZ Banking")
customer1 = Customer()


#_______________________checks user credentials-------------------------
def check(username,pwd, frame):
    global customer1
    if customer1.LogIn(username,pwd):
        login(frame)


#   ________________________sign up for new users_______________

def create_acc(window,username, pwd, firstName, lastName):
    global customer1
    customer1.Sign_UP(firstName, lastName, username, pwd)

# __________________ sign for bank accounts________________________

def sav_ch_ln_sigup(acc):
    global customer1
    if acc == "saving":
        s2 = Saving_Account(customer1)
        s2.Create_Accounts()
    elif acc == "checking":
        c2 = Checking_Account(customer1)
        c2.Create_Accounts()
    elif acc == "loan":
        l2 = Loan_Account(customer1)
        l2.Create_Accounts()
        print(acc)

# ______________________________ saving acc deposit__________________

def sav_deposit(saving_acc, acc_no, *windows):
    for i in windows:
        i.destroy()
    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.25, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1, height=37, placeholder_text="Enter amount")
    amount_entry.place(relwidth = 0.5,relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: saving_acc.Deposit(amount_entry.get()))
    submit_button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Saving Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no,"saving", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# ______________________________ saving acc withdraw__________________

def sav_withdraw(saving_acc, acc_no, *windows):
    for i in windows:
        i.destroy()
    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.25, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1, height=35, placeholder_text="Enter amount")
    amount_entry.place(relwidth = 0.5,relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: saving_acc.With_Draw(amount_entry.get()))
    submit_button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Saving Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no, "saving", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# ______________________________ loan acc withdraw(loan)__________________

def ln_withdraw(loan_acc, acc_no, *windows):
    for i in windows:
        i.destroy()

    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.21, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1,height=35, placeholder_text="Enter amount")
    amount_entry.place(relwidth = 0.5,relx=0.5, rely=0.27, anchor=tkinter.CENTER)

    day_label = CTkLabel(frame1, text="Return Day:", font=CTkFont(size=15))
    day_label.place(relx=0.25, rely=0.37, anchor=tkinter.W)

    day_entry = CTkEntry(frame1, height=35, placeholder_text="Enter Day(1,2,3...)")
    day_entry.place(relwidth = 0.5, relx=0.5, rely=0.43, anchor=tkinter.CENTER)

    month_label = CTkLabel(frame1, text="Return Month:", font=CTkFont(size=15))
    month_label.place(relx=0.25, rely=0.53, anchor=tkinter.W)

    month_entry = CTkEntry(frame1, height=35, placeholder_text="Enter Month(9,10,12,..)")
    month_entry.place(relwidth = 0.5,relx=0.5, rely=0.59, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Return Year:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.69, anchor=tkinter.W)

    year_entry = CTkEntry(frame1, height=35, placeholder_text="Enter Year(2023,2022,...)")
    year_entry.place(relwidth = 0.5,relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: loan_acc.With_Draw(year_entry.get(), month_entry.get(), day_entry.get(), amount_entry.get()) )
    submit_button.place(relx=0.5, rely=0.85, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Loan Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no, "loan", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# ______________________________ loan acc deposit__________________

def ln_deposit(loan_acc, acc_no, *windows):
    for i in windows:
        i.destroy()
    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.25, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1, height=37, placeholder_text="Enter amount")
    amount_entry.place(relwidth=0.5, relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: loan_acc.Deposit(amount_entry.get()))
    submit_button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Loan Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no, "loan", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


# ______________________________ checking acc withdraw__________________

def ch_withdraw(checking_acc, acc_no, *windows):

    for i in windows:
        i.destroy()

    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.25, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1, height=37, placeholder_text="Enter amount")
    amount_entry.place(relwidth=0.5, relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: checking_acc.With_Draw(amount_entry.get()) )
    submit_button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Checking Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no, "checking", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


# ______________________________ checking acc deposit__________________

def ch_deposit(checking_acc, acc_no, *windows):
    for i in windows:
        i.destroy()
    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

    amount_label = CTkLabel(frame1, text="Amount:", font=CTkFont(size=15))
    amount_label.place(relx=0.25, rely=0.25, anchor=tkinter.W)

    amount_entry = CTkEntry(frame1, height=37, placeholder_text="Enter amount")
    amount_entry.place(relwidth=0.5, relx=0.5, rely=0.34, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame1, text="Submit", width=250, height=37, command=lambda: checking_acc.Deposit(amount_entry.get()))
    submit_button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

    frame0 = CTkFrame(root, corner_radius=20)
    frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

    Accountname_label = CTkLabel(frame0, text="Checking Account\nDashboard", font=CTkFont(weight="bold", size=20))
    Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                            command=lambda: acc_check(acc_no, "checking", frame1, frame0))
    back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                            command=lambda: back("home", frame1,
                                                 frame0))  # utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#----------------------- provides user with withdraw and deposit interface-----------------------

def acc_check(account_no, acc_name, *windows):
    global customer1
    if acc_name == "saving":
        s1 = Saving_Account(customer1)
        if s1.Login(account_no):
            for i in windows:
                i.destroy()

            frame1 = CTkFrame(root, corner_radius=20)
            frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

            frame2 = CTkFrame(frame1, corner_radius=20, border_width=1)
            frame2.place(relheight=0.25, relwidth=0.9, relx=0.5, rely=0.3, anchor=tkinter.CENTER)

            frame0 = CTkFrame(root, corner_radius=20)
            frame0.place(relheight = 0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor = tkinter.CENTER)

            Accountname_label = CTkLabel(frame0,text ="Saving Account\nDashboard", font = CTkFont(weight="bold", size=20))
            Accountname_label.place(relx=0.5, rely=0.1, anchor = tkinter.CENTER)

            back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                                    command=lambda: back(acc_name, frame1,frame0))
            back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

            home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                                    command=lambda: back("home", frame1,
                                                         frame0))  # utlizes the same back() function in order to go back to homepage
            home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

            balance = s1.BalanceEnquiry()

            label = CTkLabel(frame2,text =f"Your current balance is {balance}", font = CTkFont(weight="bold", size=20))
            label.place(relx=0.5, rely=0.3, anchor = tkinter.CENTER)

            Deposit_button = CTkButton(frame1, text = "Deposit", font=CTkFont(size=18, family="timesnewroman"),command = lambda: sav_deposit(s1, account_no, frame1,frame0))
            Deposit_button.place(relwidth = 0.35,relheight = 0.1,relx=0.5, rely=0.6, anchor = tkinter.CENTER)

            Withdraw_button = CTkButton(frame1, text="Withdraw",font=CTkFont(size=18, family="timesnewroman"), command = lambda: sav_withdraw(s1, account_no, frame1, frame0))
            Withdraw_button.place(relwidth = 0.35,relheight = 0.1,relx=0.5, rely=0.8, anchor = tkinter.CENTER)

    elif acc_name == "checking":
        c1 = Checking_Account(customer1)
        if c1.Login(account_no):
            for i in windows:
                i.destroy()


            frame1 = CTkFrame(root, corner_radius=20)
            frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

            frame2 = CTkFrame(frame1, corner_radius=20,  border_width=1)
            frame2.place(relheight=0.25, relwidth=0.9, relx=0.5, rely=0.3, anchor=tkinter.CENTER)

            frame0 = CTkFrame(root, corner_radius=20)
            frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

            Accountname_label = CTkLabel(frame0, text="Checking Account\nDashboard",
                                         font=CTkFont(weight="bold", size=20))
            Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

            balance = str(c1.BalanceEnquiry())

            label = CTkLabel(frame2, text=f"Your current balance is "+ balance, font=CTkFont(size=20,weight="bold"))
            label.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

            deposit_button = CTkButton(frame1, text="Deposit", font=CTkFont(size=18, family="timesnewroman"),command=lambda: ch_deposit(c1, account_no,frame1, frame0))
            deposit_button.place(relwidth = 0.35,relheight = 0.1,relx=0.5, rely=0.6, anchor = tkinter.CENTER)

            withdraw_button = CTkButton(frame1, text="Withdraw", font=CTkFont(size=18, family="timesnewroman"),command=lambda: ch_withdraw(c1, account_no,frame1, frame0))
            withdraw_button.place(relwidth = 0.35,relheight = 0.1,relx=0.5, rely=0.8, anchor = tkinter.CENTER)

            back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                                    command=lambda: back(acc_name, frame1, frame0))
            back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

            home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                                    command=lambda: back("home", frame1,
                                                         frame0))  # utlizes the same back() function in order to go back to homepage
            home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    elif acc_name == "loan":
            l1 = Loan_Account(customer1)
            if l1.Login(account_no):
                for i in windows:
                    i.destroy()


                frame1 = CTkFrame(root, corner_radius=20)       # main frame on right
                frame1.place(relheight=0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor=tkinter.CENTER)

                frame2 = CTkFrame(frame1, corner_radius=20, border_width=1) #for displaying balance
                frame2.place(relheight=0.25, relwidth=0.9, relx=0.5, rely=0.3, anchor=tkinter.CENTER)

                frame0 = CTkFrame(root, corner_radius=20)
                frame0.place(relheight=0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor=tkinter.CENTER)

                loan_info_frame = CTkFrame(frame0, corner_radius = 15, border_width=1 )
                loan_info_frame.place(relwidth = 0.95, relheight = 0.35, relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

                Accountname_label = CTkLabel(frame0, text="Loan Account\nDashboard",
                                             font=CTkFont(weight="bold", size=20))
                Accountname_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

                balance = l1.BalanceEnquiry()      # will have a tuple containing the principle amount and deadline

                label = CTkLabel(frame2, text=f"Your current loan is " + balance[0],
                                 font=CTkFont(size=20, weight="bold"))
                label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                deposit_button = CTkButton(frame1, text="Deposit", font=CTkFont(size=18, family="timesnewroman"),
                                           command=lambda: ln_deposit(l1, account_no,frame1,frame0))
                deposit_button.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.6, anchor=tkinter.CENTER)

                withdraw_button = CTkButton(frame1, text="Loan", font=CTkFont(size=18, family="timesnewroman"),
                                            command=lambda: ln_withdraw(l1, account_no,frame1,frame0))
                withdraw_button.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.8, anchor=tkinter.CENTER)


                loan_info_label = CTkLabel(loan_info_frame, text = f"No loan less than 5000\nwill be granted!\n\n\nDeadline for loan:<{balance[1]}>",font=CTkFont(weight="bold", size=15), bg_color=loan_info_frame._fg_color)
                loan_info_label.place(relx = 0.5,rely = 0.45, anchor = tkinter.CENTER)

                back_button = CTkButton(frame0, text="Back", corner_radius=25, height=40,
                                        command=lambda: back(acc_name, frame1, frame2, frame0))
                back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

                home_button = CTkButton(frame0, text="Home", corner_radius=25, height=40,
                                        command=lambda: back("home", frame1,
                                                             frame2,
                                                             frame0))  # utlizes the same back() function in order to go back to homepage
                home_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


#___________________new customer signup interface_________________________

def signup(window = None):
    if window != None:
        window.destroy()
    frame = CTkFrame(root, width = 340, height = 460, corner_radius=20, border_width=1)
    frame.place(relx=0.5,rely=0.5, anchor = tkinter.CENTER)

    heading = CTkLabel(master=frame, text="Sign Up", font = CTkFont(family="timesnewroman", size=20, weight = "bold"))
    heading.place(relx=0.5,rely=0.1, anchor = tkinter.N)

    FirstName_label = CTkLabel(frame, text="First Name")
    FirstName_label.place(relx=0.1, rely=0.2, anchor=tkinter.NW)
    FirstName_entry = CTkEntry(frame, width=250, height=35, placeholder_text="Enter your First Name")
    FirstName_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    LastName_label = CTkLabel(frame, text="Last Name")
    LastName_label.place(relx=0.1, rely=0.35, anchor = tkinter.NW)
    LastName_entry = CTkEntry(frame, width=250, height=35, placeholder_text="Enter Your Last Name")
    LastName_entry.place(relx=0.5,rely=0.45,anchor = tkinter.CENTER)

    UserName_label = CTkLabel(frame, text="User Name")
    UserName_label.place(relx=0.1, rely=0.5, anchor=tkinter.NW)
    UserName_entry = CTkEntry(frame, width=250, height=35, placeholder_text="Enter User Name")
    UserName_entry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    password_label = CTkLabel(frame, text="Password")
    password_label.place(relx=0.1, rely=0.65, anchor = tkinter.NW)
    password_entry = CTkEntry(frame, width=250, height=35, placeholder_text="Enter password")
    password_entry.place(relx=0.5,rely=0.75,anchor = tkinter.CENTER)


    signup_button = CTkButton(frame, text="Sign up", height = 37,width=250, command= lambda: create_acc(frame, UserName_entry.get(), password_entry.get(), FirstName_entry.get(), LastName_entry.get()))
    signup_button.place(relx=0.5,rely=0.85, anchor = tkinter.CENTER)

    back_button = CTkButton(frame, text="Back",corner_radius=25,  height = 35, command= lambda:back("home", frame), fg_color=frame._fg_color, border_width=1,border_color="white")  
    back_button.place(relx=0.5,rely=0.95, anchor = tkinter.CENTER)


#___________________new customer's password_________________________
def submit_new_pswd(username,newpswd,confirmpswd):
    global customer1
    customer1.Forgot_Password(username,newpswd,confirmpswd)

#___________________interface for resetting customer's pwd_________________________
def reset_pwd(window):
    window.destroy()
    frame = CTkFrame(root, width = 330, height = 430, corner_radius=20, border_width=1)
    frame.place(relx=0.5,rely=0.5, anchor = tkinter.CENTER)

    label0 = CTkLabel(master=frame, text="Reset Password", font = CTkFont(family="timesnewroman", size=20, weight = "bold"))
    label0.place(relx=0.5,rely=0.1, anchor = tkinter.N)

    label1 = CTkLabel(frame, text="Username")
    label1.place(relx=0.1, rely=0.24, anchor = tkinter.NW)
    entry1 = CTkEntry(frame, width=250, height=35, placeholder_text="Enter username")
    entry1.place(relx=0.5,rely=0.34,anchor = tkinter.CENTER)

    label2 = CTkLabel(frame, text="New Password")
    label2.place(relx=0.1, rely=0.4, anchor = tkinter.NW)
    entry2 = CTkEntry(frame, width=250, height=35, placeholder_text="Enter new password")
    entry2.place(relx=0.5,rely=0.5,anchor = tkinter.CENTER)

    label3 = CTkLabel(frame, text="Confirm new password")
    label3.place(relx=0.1, rely=0.6, anchor = tkinter.NW)
    entry3 = CTkEntry(frame, width=250, height=35, placeholder_text="Enter new password")
    entry3.place(relx=0.5,rely=0.7,anchor = tkinter.CENTER)

    submit_button = CTkButton(frame, text="Submit",corner_radius=25,  height = 37,width=250,command=lambda :(submit_new_pswd(entry1.get(),entry2.get(),entry3.get())))
    submit_button.place(relx=0.5,rely=0.84, anchor = tkinter.CENTER)

    back_button = CTkButton(frame, text="Back",corner_radius=25,  height = 35, command= lambda:back("home", frame), fg_color=frame._fg_color, border_width=1,border_color="white")  
    back_button.place(relx=0.5,rely=0.95, anchor = tkinter.CENTER)

#___________________customer's home page_________________________

def home(window = None):
    if window != None:
        window.destroy()
    frame = CTkFrame(root, width = 350, height = 450, corner_radius=20, border_width=1)
    frame.place(relx=0.5,rely=0.5, anchor = tkinter.CENTER)
    label0 = CTkLabel(master=frame, text="WELCOME", font = CTkFont(family="timesnewroman", size=20, weight = "bold"))
    label0.place(relx=0.5,rely=0.1, anchor = tkinter.N)

    label1 = CTkLabel(frame, text="Username")
    label1.place(relx=0.2, rely=0.27, anchor = tkinter.CENTER)
    entry1 = CTkEntry(frame, width=250, height=35, placeholder_text="Enter username")
    entry1.place(relx=0.5,rely=0.34,anchor = tkinter.CENTER)

    label2 = CTkLabel(frame, text="Password")
    label2.place(relx=0.2, rely=0.43, anchor = tkinter.CENTER)
    entry2 = CTkEntry(frame, width=250, height=35, placeholder_text="Enter password", show="*")
    entry2.place(relx=0.5,rely=0.5,anchor = tkinter.CENTER)

    button1= CTkButton(frame, text="Forgot password?", fg_color=frame._fg_color, command=lambda :reset_pwd(frame))
    button1.place(relx=0.75,rely=0.56, anchor= tkinter.N)

    button1 = CTkButton(frame, text = "Login", width=250, height=37, command = lambda:check(entry1.get(),entry2.get(), frame))
    button1.place(relx=0.5,rely=0.65, anchor = tkinter.N)

    label4 = CTkLabel(frame, text="New user?", font = CTkFont(size=12))
    label4.place(relx=0.2, rely=0.75, anchor = tkinter.N)

    button2 = CTkButton(frame, text = "Sign up", width = 250, height=37, command = lambda:signup(frame))
    button2.place(relx=0.5,rely=0.8, anchor = tkinter.N)

    exit_button = CTkButton(frame, text="Exit", command = lambda:root.destroy(), width=50, fg_color=frame._fg_color, border_color="white", border_width=1, hover_color="red")
    exit_button.place(relx=0.68,rely=0.96, anchor=tkinter.CENTER)

    back_button = CTkButton(frame, text="Back", command=lambda: back("mainmenu", frame), width=50, fg_color=frame._fg_color,
                            border_color="white", border_width=1, hover_color="green")
    back_button.place(relx=0.3, rely=0.96, anchor=tkinter.CENTER)

##___________________provides interface for selecting different accounts i.e saving, checking etc_________________________

def login( *windows ):
    if windows != None:
        for i in windows:
            i.destroy()
    frame = CTkFrame(root, width = 350, height = 450, corner_radius=20, border_width=1)
    frame.place(relx=0.5,rely=0.5, anchor = tkinter.CENTER)

    label0 = CTkLabel(master=frame, text="Hi! choose an account", font = CTkFont(family="timesnewroman", size=20, weight = "bold"))
    label0.place(relx=0.5,rely=0.1, anchor = tkinter.CENTER)

    acc = CTkLabel(master=frame, text="Choose an account:", font = CTkFont(size=17))
    acc.place(relx=0.5,rely=0.3, anchor= tkinter.CENTER)

    button1= CTkButton(frame, text="Loan account", width=300, height=50, font = CTkFont(size=17), command= lambda : account("loan", frame))
    button1.place(relx=0.5,rely=0.4, anchor= tkinter.CENTER)

    button2= CTkButton(frame, text="Saving account",width=300, height=50, font = CTkFont(size=17),command= lambda : account("saving",frame))
    button2.place(relx=0.5,rely=0.6, anchor= tkinter.CENTER)

    button3= CTkButton(frame, text="Checking account",width=300, height=50, font = CTkFont(size=17), command= lambda : account("checking",frame))
    button3.place(relx=0.5,rely=0.8, anchor= tkinter.CENTER)

    back_button = CTkButton(frame, text="Back",corner_radius=25, height = 35, command= lambda:back("home", frame))
    back_button.place(relx=0.5,rely=0.95, anchor = tkinter.CENTER)

#--------------------------provides internal interface for saving, checking and loan accounts__________

def account(acc, window= None):
    if window != None:
        window.destroy()
    frame1 = CTkFrame(root, corner_radius=20)
    frame1.place(relheight = 0.94, relwidth=0.3, relx=0.17, rely=0.5, anchor = tkinter.CENTER)

    frame2 = CTkFrame(root, corner_radius=20)
    frame2.place(relheight = 0.94, relwidth=0.6, relx=0.67, rely=0.5, anchor = tkinter.CENTER)
    
    if acc == "loan":
        account_name = "Loan Account\nDashboard"
    elif acc == "saving":
        account_name = "Saving Account\nDashboard"
    elif acc == "checking":
        account_name = "Checking Account\nDashboard"
    account_heading = CTkLabel(frame1, text=account_name, font = CTkFont(size=20,weight="bold") )
    account_heading.place(relx=0.5, rely=0.1, anchor= tkinter.CENTER)

    accountNo_label = CTkLabel(frame2, text="Account Number:", font=CTkFont(size = 15))
    accountNo_entry = CTkEntry(frame2, placeholder_text="Enter account no.", width = 220, height = 37)

    accountNo_label.place(relx=0.27, rely=0.23, anchor = tkinter.W)
    accountNo_entry.place(relx = 0.5, rely= 0.3, anchor = tkinter.CENTER)

    submit_button = CTkButton(frame2, text = "Submit",command=lambda :acc_check(accountNo_entry.get(),acc, frame1, frame2))
    submit_button.place(relx = 0.5, rely =0.4, anchor = tkinter.CENTER)

    signup_label = CTkLabel(frame2, text = f"Dont have a {acc} account\nor want more? Sign up now")
    signup_label.place(relx=0.5, rely=0.75, anchor = tkinter.CENTER)

    signup_button = CTkButton(frame2, text = "SignUp", command= lambda : sav_ch_ln_sigup(acc))
    signup_button.place(relx = 0.5, rely = 0.85, anchor = tkinter.CENTER)


    back_button = CTkButton(frame1, text="Back",corner_radius=25, height = 40, command= lambda:(login(frame1, frame2)))
    back_button.place(relx=0.5,rely=0.8, anchor = tkinter.CENTER)

    home_button = CTkButton(frame1, text="Home",corner_radius=25,  height = 40, command= lambda:back("home", frame1, frame2))  #utlizes the same back() function in order to go back to homepage
    home_button.place(relx=0.5,rely=0.9, anchor = tkinter.CENTER)


def Main_menu():
    frame = CTkFrame(root, width=350, height=450, corner_radius=20, border_width=1)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label0 = CTkLabel(master=frame, text="Main Menu", font=CTkFont(family="timesnewroman", size=20, weight="bold"))
    label0.place(relx=0.5, rely=0.1, anchor=tkinter.N)

    customer_button  = CTkButton(frame, text = "Customer", width=250, height=45, command = lambda : home(frame))
    customer_button.place(relx=0.5,rely=0.4, anchor = tkinter.N)

    admin_button = CTkButton(frame, text="Admin", width=250, height=45, command = lambda: admin(frame))
    admin_button.place(relx=0.5, rely=0.6, anchor=tkinter.N)

    exit_button = CTkButton(frame, text="Exit", command=lambda: root.destroy(), width=100, fg_color=frame._fg_color,
                            border_color="white", border_width=1, hover_color="red")
    exit_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

#__________________Contains all the necessary interface and functions for admin_____________

def admin(window = None):

    a1 = Administrator()
    def admin_interface(admin_username, pin, window):

        if a1.Log_In(admin_username, pin):
            window.destroy()
            frame1 = CTkFrame(root, width=340, height=430, corner_radius=20, border_width=1)
            frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            heading = CTkLabel(master=frame1, text="Admin Interface",
                               font=CTkFont(family="timesnewroman", size=20, weight="bold"))
            heading.place(relx=0.5, rely=0.1, anchor=tkinter.N)

            bankInfo_button = CTkButton(frame1, text="Bank Info",  width=250, height=45,
                                    command= lambda: bank_info(frame1), border_width=1, border_color="white")
            bankInfo_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

            tran_his_button = CTkButton(frame1, text="Transaction History", width=250, height=45,
                                        command=lambda: tran_his(frame1), border_width=1, border_color="white")
            tran_his_button.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

            back_button = CTkButton(frame1, text="Back", corner_radius=25, height=35,
                                    command=lambda: back("admin", frame1),
                                    fg_color=frame1._fg_color, border_width=1, border_color="white")
            back_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

            exit_button = CTkButton(frame1, text="Exit", command= lambda : root.destroy(), corner_radius=25, height=35,
                                    fg_color=frame1._fg_color,
                                    border_color="white", border_width=1, hover_color="red")
            exit_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    def tran_his(window):
        window.destroy()
        users = a1.Bank_info()

        main_frame = CTkFrame(root, corner_radius=20, border_width=1)
        main_frame.place(relwidth=0.95, relheight=0.95, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        heading = CTkLabel(master=main_frame, text="Transaction History",
                           font=CTkFont(family="timesnewroman", size=20, weight="bold"))
        heading.place(relx=0.5, rely=0.05, anchor=tkinter.N)

        frame = CTkScrollableFrame(main_frame)
        frame.place(relwidth = 0.8, relheight=0.8, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        username_label = CTkLabel(frame, text="Username", corner_radius=17, fg_color="#5a8d6c",
                                  font=CTkFont(weight="bold", size=20))
        username_label.grid(column=0, row=0, ipadx=5, ipady=5)

        accountno_label = CTkLabel(frame, text="Account No", corner_radius=17, fg_color="#5a8d6c",
                                   font=CTkFont(weight="bold", size=20))
        accountno_label.grid(column=1, row=0, ipadx=5, ipady=5)

        accounttype_label = CTkLabel(frame, text="Account type", corner_radius=17, fg_color="#5a8d6c",
                                     font=CTkFont(weight="bold", size=20))
        accounttype_label.grid(column=2, row=0, ipadx=5, ipady=5)

        amount_label = CTkLabel(frame, text="Amount", corner_radius=17, fg_color="#5a8d6c",
                                        font=CTkFont(weight="bold", size=20))
        amount_label.grid(column=3, row=0, ipadx=5, ipady=5)

        tranType_label = CTkLabel(frame, text="Transc. Type", corner_radius=17, fg_color="#5a8d6c",
                                font=CTkFont(weight="bold", size=20))
        tranType_label.grid(column=4, row=0, ipadx=5, ipady=5)

        date_label = CTkLabel(frame, text="Date", corner_radius=17, fg_color="#5a8d6c",
                                font=CTkFont(weight="bold", size=20))
        date_label.grid(column=5, row=0, ipadx=5, ipady=5)

        Row = 1
        for user in users:
            with open(f"users/{user}") as file:
                file = eval(file.read())
                for i in file[0]:
                    username = i
                    username_label = CTkLabel(frame, text=f"{username}", corner_radius=25, fg_color=root._fg_color,
                                              font=CTkFont(weight="bold", size=15))
                    username_label.grid(column=0, row=Row, )
                tran_history = file[4]  # assigns the last dictionary of transaction history to tran_history
                for i in tran_history:
                    account_type = i
                    tran_acc_history = tran_history[i]  # assigns the history(list) of the account(saving,checking etc) tp tran_acc_history
                    for record in tran_acc_history:  # "record" has all the details of a single transaction
                        account_no = record[0]
                        transaction_type = record[1]
                        amount = record[2]
                        date = record[3]
                        accountno_label = CTkLabel(frame, text=f"{account_no}", corner_radius=25,
                                                   fg_color=root._fg_color,
                                                   font=CTkFont(weight="bold", size=15))
                        accountno_label.grid(column=1, row=Row, ipadx=5, ipady=5)

                        accounttype_label = CTkLabel(frame, text=f"{account_type}", corner_radius=25,
                                                     fg_color=root._fg_color,
                                                     font=CTkFont(weight="bold", size=20))
                        accounttype_label.grid(column=2, row=Row, ipadx=5, ipady=5)

                        amount_label = CTkLabel(frame, text=f"{amount}", corner_radius=25,
                                                        fg_color=root._fg_color,
                                                        font=CTkFont(weight="bold", size=20))
                        amount_label.grid(column=3, row=Row, ipadx=5, ipady=5)

                        tranType_label = CTkLabel(frame, text=f"{transaction_type}", corner_radius=17, fg_color=root._fg_color,
                                                  font=CTkFont(weight="bold", size=20))
                        tranType_label.grid(column=4, row=Row, ipadx=5, ipady=5)

                        date_label = CTkLabel(frame, text=f"{date}", corner_radius=17, fg_color=root._fg_color,
                                              font=CTkFont(weight="bold", size=20))
                        date_label.grid(column=5, row=Row, ipadx=5, ipady=5)

                        Row += 1

        back_button = CTkButton(main_frame, text="Back", height=37, width=250,
                                command=lambda: admin_interface(a1.Admin_ID,a1.Admin_pswd,main_frame))
        back_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)
    def bank_info(window):
        window.destroy()

        users = a1.Bank_info()

        main_frame = CTkFrame(root, corner_radius=20, border_width=1)
        main_frame.place(relwidth = 0.95, relheight = 0.95, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        heading = CTkLabel(master=main_frame, text="Bank Info",
                           font=CTkFont(family="timesnewroman", size=20, weight="bold"))
        heading.place(relx=0.5, rely=0.05, anchor=tkinter.N)


        frame = CTkScrollableFrame(main_frame, width = 680)
        frame.place(relheight=0.8, relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        username_label = CTkLabel(frame, text="Username", corner_radius=17, fg_color="#5a8d6c",
                                  font=CTkFont(weight="bold", size=20))
        username_label.grid(column=0, row=0, ipadx=5, ipady=5)

        accountno_label = CTkLabel(frame, text="Account No", corner_radius=17, fg_color="#5a8d6c",
                                   font=CTkFont(weight="bold", size=20))
        accountno_label.grid(column=1, row=0, ipadx=5, ipady=5)

        accounttype_label = CTkLabel(frame, text="Account type", corner_radius=17, fg_color="#5a8d6c",
                                     font=CTkFont(weight="bold", size=20))
        accounttype_label.grid(column=2, row=0, ipadx=5, ipady=5)

        accountbalance_label = CTkLabel(frame, text="Balance", corner_radius=17, fg_color="#5a8d6c",
                                        font=CTkFont(weight="bold", size=20))
        accountbalance_label.grid(column=3, row=0, ipadx=5, ipady=5)

        Row = 1
        for user in users:
            with open(f"users/{user}") as file:
                file = eval(file.read())
                for i in file[0]:
                    username = i
                    file.pop(0)
                    username_label = CTkLabel(frame, text=f"{username}", corner_radius=25, fg_color=root._fg_color,
                                              font=CTkFont(weight="bold", size=15))
                    username_label.grid(column=0, row=Row, )
                    file.pop(3)

                for i in file:
                    for j in i:
                        account_no = j
                        balance = i[j][0]
                        account_type = i[j][1]
                        accountno_label = CTkLabel(frame, text=f"{account_no}", corner_radius=25,
                                                   fg_color=root._fg_color,
                                                   font=CTkFont(weight="bold", size=15))
                        accountno_label.grid(column=1, row=Row, ipadx=5, ipady=5)

                        accounttype_label = CTkLabel(frame, text=f"{account_type}", corner_radius=25,
                                                     fg_color=root._fg_color,
                                                     font=CTkFont(weight="bold", size=20))
                        accounttype_label.grid(column=2, row=Row, ipadx=5, ipady=5)

                        accountbalance_label = CTkLabel(frame, text=f"{balance}", corner_radius=25,
                                                        fg_color=root._fg_color,
                                                        font=CTkFont(weight="bold", size=20))
                        accountbalance_label.grid(column=3, row=Row, ipadx=5, ipady=5)

                        Row += 1

        back_button = CTkButton(main_frame, text="Back", height=37, width = 250,
                                command=lambda: admin_interface(a1.Admin_ID,a1.Admin_pswd,main_frame))
        back_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

    def change_admin_pwd(window):
        window.destroy()
        frame1 = CTkFrame(root, width=340, height=430, corner_radius=20, border_width=1)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        heading = CTkLabel(master=frame1, text="Change Admin Password",
                          font=CTkFont(family="timesnewroman", size=20, weight="bold"))
        heading.place(relx=0.5, rely=0.1, anchor=tkinter.N)

        username_label = CTkLabel(frame1, text="Username")
        username_label.place(relx=0.1, rely=0.24, anchor=tkinter.NW)
        username_entry = CTkEntry(frame1, width=250, height=35, placeholder_text="enter username")
        username_entry.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)
        username_entry.focus_set()

        oldPasswordlabel_label = CTkLabel(frame1, text="Old Password")
        oldPasswordlabel_label.place(relx=0.1, rely=0.4, anchor=tkinter.NW)
        oldPasswordlabel_entry = CTkEntry(frame1, width=250, height=35, placeholder_text="Enter old password")
        oldPasswordlabel_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        newPassword_label = CTkLabel(frame1, text="New password")
        newPassword_label.place(relx=0.1, rely=0.6, anchor=tkinter.NW)
        newPassword_entry = CTkEntry(frame1, width=250, height=35, placeholder_text="Enter new password")
        newPassword_entry.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        submit_button = CTkButton(frame1, text="Submit", corner_radius=25, height=37, width=250,
                                  command=lambda:a1.Change_pswd(username_entry.get(),oldPasswordlabel_entry.get(), newPassword_entry.get()) )
        submit_button.place(relx=0.5, rely=0.84, anchor=tkinter.CENTER)

        back_button = CTkButton(frame1, text="Back", corner_radius=25, height=35, command=lambda: back("admin", frame1),
                                fg_color= frame1._fg_color, border_width=1, border_color="white")
        back_button.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

    if window != None:
        window.destroy()


    frame = CTkFrame(root, width=370, height=450, corner_radius=20, border_width=1, bg_color="transparent")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    admin_label = CTkLabel(master=frame, text="ADMIN", font=CTkFont(family="timesnewroman", size=20, weight="bold"))
    admin_label.place(relx=0.5, rely=0.1, anchor=tkinter.N)

    adminUser_label = CTkLabel(frame, text="Username", font=CTkFont(size=15))
    adminUser_entry = CTkEntry(frame, placeholder_text="Enter Admin Username", width=220, height=37)

    adminUser_label.place(relx=0.19, rely=0.23, anchor=tkinter.W)
    adminUser_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    PIN_label = CTkLabel(frame, text="PIN", font=CTkFont(size=15))
    PIN_entry = CTkEntry(frame, placeholder_text="Enter Admin PIN", width=220, height=37, show = "*")

    fgtPwd_button = CTkButton(frame, text="Change password", fg_color=frame._fg_color, command=lambda: change_admin_pwd(frame))
    fgtPwd_button.place(relx=0.75, rely=0.56, anchor=tkinter.N)

    PIN_label.place(relx=0.23, rely=0.43, anchor=tkinter.CENTER)
    PIN_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    submit_button = CTkButton(frame, text="Submit", width=220, height=45,command=lambda: admin_interface(adminUser_entry.get(), PIN_entry.get(), frame))
    submit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    back_button = CTkButton(frame, text="Back", corner_radius=25, height=35, border_width=2, border_color= "white", fg_color=frame._fg_color, command=lambda: back("mainmenu", frame))
    back_button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

def back(page_name, *windows):
    for i in windows:           # "windows" contains all the frames of previous windows
        i.destroy()         #destroys every frame inorder to go back
    if page_name == "login":
        login()
    elif page_name == "home":
        home()

    elif page_name == "mainmenu":
        Main_menu()

    elif page_name == "admin":
        admin()

    elif page_name == "saving":
        account("saving")

    elif page_name == "loan":
        account("loan")

    elif page_name == "checking":
        account("checking")

Main_menu()

root.mainloop()