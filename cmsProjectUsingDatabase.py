#    Customer Management System

# business logic layer code start here
import pymysql


class Customer:
    con = pymysql.connect(host="localhost", user="root", password="Akash@786", database="cus")

    def __init__(self):
        self.id = 0
        self.name = ""
        self.address = ""
        self.mob = ""
      

    def addCustomer(self):
        mycursor = Customer.con.cursor()
        strQuery = "insert into customer values(%s,%s,%s,%s)"
        mycursor.execute(strQuery, (self.id, self.name, self.address, self.mob))
        Customer.con.commit()

    def searchCustomer(self, id):
        mycursor = Customer.con.cursor()
        strQuery = "select * from customer where id=%s"
        rowAffected = mycursor.execute(strQuery, (id,))
        if (rowAffected != 0):
            row = mycursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mob = row[3]
        else:
            raise Exception("Id not Found")

    def deleteCustomer(self, id):
        mycursor = Customer.con.cursor()
        strQuery = "delete from customer where id=%s"
        rowAffeted = mycursor.execute(strQuery, (id,))
        if (rowAffeted != 0):
            Customer.con.commit()
        else:
            raise Exception("Id not found")

    def modifyCustomer(self):
        mycursor = Customer.con.cursor()
        strQuery = "update customer set name=%s,address=%s,mob=%s where id=%s"
        rowAffected = mycursor.execute(strQuery, (self.name, self.address, self.mob,self.id))
        if (rowAffected != 0):
            Customer.con.commit()
        else:
            raise Exception("Id not found")

    def showAllCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "select * from customer"
        myCursor.execute(strQuery)

        for row in myCursor.fetchall():
            print("Id :", row[0], "Name :", row[1], "Address :", row[2], "Mobile no :", row[3])


# business logic layer code End here


# Presentation layer code start here

while (True):

    print("-----------Menu------------\n")
    print(
        "1) Add Customer\n2) Search Customer\n3) Delete Customer\n4) Modify Customer\n5) Show All Customer\n0) Exit\n")
    ch = input("Enter Your Choice : ")

    if (ch == "1"):
        # code for addCustomer
        try:
            cus = Customer()
            cus.id = int(input("Enter Id : "))
            cus.name = input("Enter name : ")
            cus.address = input("Enter Address : ")
            cus.mob = input("Enter Mobile Number : ")
            cus.addCustomer()
            print("Customer Added Sucessfully\n")

        except Exception as e:
            print(e)


    elif (ch == "2"):
        # code for searchCustomer

        try:
            cus = Customer()
            id = int(input("Enter Id : "))
            cus.searchCustomer(id)
            print("Id =", cus.id, "Name =", cus.name, "Address =", cus.address, "Mobile =", cus.mob)

        except Exception as ex:
            print(ex)

    elif (ch == "3"):
        # code for delete Customer
        try:
            cus = Customer()
            id = int(input("Enter Id : "))
            cus.deleteCustomer(id)
            print("Customer Deleted Successfully")

        except Exception as ex:
            print(ex)

    elif (ch == "4"):
        try:
            cus = Customer()
            cus.id = int(input("Enter ID : "))
            cus.name = input("Enter Name : ")
            cus.address = input("Enter Address : ")
            cus.mob = input("Enter Mobile No : ")
            cus.modifyCustomer()
            print("Customer Modified Successfully")

        except Exception as ex:
            print(ex)

    elif (ch == "5"):
        cus = Customer()
        cus.showAllCustomer()

    elif (ch == "0"):
        break

# Presentation layer code End here
