# Banking system


# Business Logic Layer start From here

line = "-------------"


class BankingSystem:
    accountNumber = 1000
    listbank = []

    def __init__(self):
        self.acc = 0
        self.password = ""
        self.name = ""
        self.gender = ""
        self.totalBalance = 0
        self.condition = ""

    def generateAccountNumber(self):
        BankingSystem.accountNumber += 1
        self.condition = int(BankingSystem.accountNumber)

    def depositMoney(self, account, temp):
        for i in range(len(BankingSystem.listbank)):
            if (account == BankingSystem.listbank[i].acc):
                self.totalBalance += temp

    def forgotPassword(self, number, pas):
        for i in range(len(BankingSystem.listbank)):
            if (number == BankingSystem.listbank[i].acc):
                BankingSystem.listbank[i].password = pas
                self.condition = "forgotPasswordTrue"

    def withdrawlMoney(self, account, temp):
        for i in range(len(BankingSystem.listbank)):
            if (account == BankingSystem.listbank[i].acc):
                if (self.totalBalance >= temp):
                    self.totalBalance -= temp
                    self.condition = "withdrawlTrue"

    def checkAmount(self, account, amount):
        for i in range(len(BankingSystem.listbank)):
            if (account == BankingSystem.listbank[i].acc):
                if (BankingSystem.listbank[i].totalBalance >= amount):
                    self.condition = "checkAmountTrue"

    def deductMoney(self, account, amount):
        for i in range(len(BankingSystem.listbank)):
            if (account == BankingSystem.listbank[i].acc):
                BankingSystem.listbank[i].totalBalance -= amount
                self.totalBalance = BankingSystem.listbank[i].totalBalance
                self.condition = "deductMoneyTrue"

    def addMoney(self, acc1, amount):
        for i in range(len(BankingSystem.listbank)):
            if (acc1 == BankingSystem.listbank[i].acc):
                BankingSystem.listbank[i].totalBalance += amount
                self.totalBalance = BankingSystem.listbank[i].totalBalance
                self.condition = "addMoneyTrue"
                return
            else:
                self.condition = "addMoneyFalse"

    def transferMoney(self, ac, amount):
        for i in range(len(BankingSystem.listbank)):
            if (ac == BankingSystem.listbank[i].acc):
                self.totalBalance += amount
                return True

    def login(self, acc, pas):
        for i in range(len(BankingSystem.listbank)):
            if (acc == BankingSystem.listbank[i].acc and pas == BankingSystem.listbank[i].password):
                self.name = BankingSystem.listbank[i].name
                self.gender = BankingSystem.listbank[i].gender
                self.acc = BankingSystem.listbank[i].acc
                self.totalBalance = BankingSystem.listbank[i].totalBalance
                self.condition = "loginTrue"

    def signUp(self):
        BankingSystem.listbank.append(self)

    def checkAccountNumber(self, number):
        for i in range(len(BankingSystem.listbank)):
            if (number == BankingSystem.listbank[i].acc):
                self.condition = "checkAccountNumberTrue"
                return
            else:
                self.condition = "checkAccountNumberFalse"


# Business Logic Layer End here





# presentation layer Start From here
while (True):

    try:
        print("\n", line, "Welcome To Akash Banking system | Main Menu Page |", line, sep="")
        print("\n1) Login For Existing Customer\n2) Open a New Account\n3) About Us\n4) Forgot Password\n5) Exit\n",
              sep="")

        ch = input("Enter Your Choice : ")
        ch=int(ch)

        if (ch == 1):

            bs = BankingSystem()
            print("\n", line, "Welcome To Akash Banking System | Login Page |", line, sep="")
            print()
            account = int(input("Enter your Account Number : "))
            pas = input("Enter Password : ")
            bs.login(account, pas)

            if (bs.condition == "loginTrue"):
                while (True):
                    try:
                        print("\n", line, "Akash Banking System |Welcome ", bs.name, line, sep="")
                        print()
                        print(
                            "1) Deposit Money\n2) Withdraw Money\n3) Transfer Money\n4) Show My Account Details\n5) LogOut",
                            sep="")
                        print()
                        choice = input("Enter your Choice : ")
                        choice=int(choice)
                        if (choice == 1):
                            temp = float(input("Enter Amount To be Deposit : "))
                            bs.depositMoney(account, temp)
                            print("Amount Deposit Successfully, Now Available Balance in Your Account is Rs ",
                                  bs.totalBalance)

                        elif (choice == 2):
                            temp = float(input("Enter Amount to Withdrawl : "))
                            bs.withdrawlMoney(account, temp)
                            if (bs.condition == "withdrawlTrue"):
                                print("Amount Withdrawl Successfully, Now Available Balance in Your Account is Rs ",
                                      bs.totalBalance)
                            elif (bs.condition != "withdrawlTrue"):
                                print("Your Account Does not Have Sufficient Balance For Complete this transaction")

                        elif (choice == 3):
                            amount = float(input("Enter the Amount For Transfer : "))
                            bs.checkAmount(account, amount)
                            if (bs.condition == "checkAmountTrue"):
                                acc1 = int(input("Enter the Account Number to Transfer the Money : "))
                                bs.addMoney(acc1, amount)
                                if (bs.condition == "addMoneyTrue"):
                                    bs.deductMoney(account, amount)
                                    if (bs.condition == "deductMoneyTrue"):
                                        print(line, "Amount Transfer Successfuly", line)
                                        print(line, "Now Available Balance in Your Account is Rs ", bs.totalBalance)
                                    elif (bs.condition == "deductMoneyFalse"):
                                        print("Account Number Does not Match Please Try Again")
                                elif (bs.condition == "addMoneyFalse"):
                                    print("You Have Entered Invalid Account Number Please Try again")

                            else:
                                print("You Have Insufficient Balance for Complete this Transaction")






                        elif (choice == 4):
                            print("\nAccount Number : ", bs.acc, "\nAccount Holder's Name : ", bs.name, "\nGender : ",
                                  bs.gender, "\nAvailable Balance in Your Account is Rs ", bs.totalBalance, sep="")


                        elif (choice == 5):
                            print("You Logged Out Successfully")
                            break
                    except ValueError:
                        print("Please Enter Numeric Number")
                    except Exception as e:
                        print(e)



            elif (bs.condition != "loginTrue"):
                print("Account Number or Password doesnot Match Please Try again")
                input("Enter Any Key to goto Previous Menu")


        elif (ch == 2):
            bs = BankingSystem()
            print("\n", line, "Welcome To Akash Banking System | SignUp Page |", line, sep="")
            print()
            bs.generateAccountNumber()

            print("Your Generated Account Number is : ", bs.condition)
            bs.acc = bs.condition
            name = input("Enter your Full Name : ")
            name = name.strip()
            bs.name = name.title()
            gender = input("Enter your Gender[M/F] : ")
            gender = gender.strip()
            bs.gender = gender.title()
            while (True):
                password = input("Enter Your Password(min 8 char) : ")
                if (len(password) < 8):
                    print("Please Enter Password of Minimum 8 Characters")
                elif (len(password) >= 8):
                    bs.password = password
                    break

            while (True):
                try:
                    bs.totalBalance = float(input("Enter the Amount for Deposit : "))
                    break

                except Exception:
                    print("Please Enter Amount in Digit Only")






            bs.signUp()
            print("\n", line, "Account Created Successfully", line, sep="")
            print("\n", line, "ThankYou For Using Our Service", line, sep="")
            print(line, "Your Account Number is ", bs.acc, " and Your Password is ", bs.password,
                  " and Available Balance in Your Account is ",
                  bs.totalBalance, line, sep="")
            print(line, "Please Note That Carefully", line, "\n", sep="")
            input("Enter Any Key to goto Previous Menu")

        elif (ch == 3):
            print("\n", line, "Welcome To Akash Banking System | About Us Page |", line, sep="", end="")
            print()
            print("\nAkash Banking System v1.2.0.8")
            print("Develop By Akash Verma")
            input("\nEnter Any Key to goto Previous Menu")

        elif (ch == 4):
            bs = BankingSystem()
            number = int(input("Enter Your Account Number : "))
            bs.checkAccountNumber(number)
            if (bs.condition == "checkAccountNumberTrue"):
                while (True):
                    pas = input("Enter Your New Password : ")
                    pas1 = input("ReEnter New Password : ")
                    if (pas == pas1):
                        bs.forgotPassword(number, pas)
                        if (bs.condition == "forgotPasswordTrue"):
                            print("New Password Generated Successfully")
                        else:
                            print("Some Error Occur Please Try Again")
                        break
                    else:
                        print("Password and Confirm Password Does not Match Please Re-enter Password")
            elif (bs.condition == "checkAccountNumberFalse"):
                print("Invalid Account Number Please Try again")



        elif (ch == 5):
            break

    except ValueError:
        print("Please Enter Numeric Number")

    except Exception as e:
        print(e)

input("\nEnter Any Key to goto Previous Menu")


# presentation layer End here
