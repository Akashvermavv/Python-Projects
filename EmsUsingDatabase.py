#                Employee Management System

# Bl Start from Here

import pymysql

class EMP:
    con = pymysql.connect(host="localhost", user="root", password="Akash@786", database="ems")

    @staticmethod
    def getTypebyId(id):    #for Getting type of Id
        mycursor = EMP.con.cursor()
        query = "select * from employee where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            for row in mycursor.fetchall():
                if (row[0] == id):
                    return row[2]
        else:
            raise Exception("Id Not Found")

    @staticmethod
    def getObjectbyId(id):  # for Runtime Polymorphism
        mycursor = EMP.con.cursor()
        query = "select * from employee where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            for row in mycursor.fetchall():
                if (row[0] == id):
                    if (row[2] == "Dir"):
                        return Dir()
                    elif (row[2] == "Mgr"):
                        return Mgr()
                    elif (row[2] == "TT"):
                        return TT()
        else:
            raise Exception("Id Not Found")

    def __init__(self):
        self.id = 0
        self.name = ""
        self.type = ""

    def showAllEmployees(self):
        mycursor = EMP.con.cursor()
        mycursor.execute("select employee.id,employee.name,employee.type,dir.share,dir.dirspecial"
                         " from employee inner join dir on employee.id=dir.id")
        for row in mycursor.fetchall():
            print(row)

    def add(self):
        mycursor = EMP.con.cursor()
        query = "insert into employee(id,name,type) values(%s,%s,%s)"
        rowAffected = mycursor.execute(query, (((str(self.id)).title()).strip(), ((self.name).title()).strip(), ((self.type).title()).strip()))
        if (rowAffected != 0):
            EMP.con.commit()

    def search(self, id):
        mycursor = EMP.con.cursor()
        query = "select * from employee where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            row = mycursor.fetchone()
            self.name = row[1]
            self.type = row[2]
        else:
            raise Exception("Id Not Found")

    def delete(self, id):
        mycursor = EMP.con.cursor()
        query = "delete from employee where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            EMP.con.commit()
        else:
            raise Exception("Id Not Found")

    def modify(self, id):
        mycursor = EMP.con.cursor()
        query = "update employee set name=%s where id=%s"
        rowAffected = mycursor.execute(query, (self.name, id))
        if (rowAffected != 0):
            EMP.con.commit()
        else:
            raise Exception("Id Not Found")

class Dir(EMP):
    def __init__(self):
        self.share = 0
        self.dirSpecial = ""
        super().__init__()

    def __str__(self):
        return "Name: " + self.name + " Share: " + str(self.share) + " dirSpecial: " + self.dirSpecial

    def add(self):

        mycursor = EMP.con.cursor()
        query = "insert into dir(id,share,dirspecial) values(%s,%s,%s)"
        rowAffected = mycursor.execute(query, (((str(self.id)).title()).strip(), ((str(self.share)).title()).strip(), ((self.dirSpecial).title()).strip()))
        if (rowAffected != 0):
            EMP.con.commit()
        super().add()

    def search(self, id):
        mycursor = EMP.con.cursor()
        query = "select * from dir where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            row = mycursor.fetchone()
            self.share = row[1]
            self.dirSpecial = row[2]
            super().search(id)
        else:
            raise Exception("Id Not Found")

    def delete(self, id):
        mycursor = EMP.con.cursor()
        query = "delete from dir where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            super().delete(id)
        else:
            raise Exception("Id Not Found")

    def modify(self, id):
        mycursor = EMP.con.cursor()
        query = "update dir set share=%s,dirspecial=%s where id=%s"
        rowAffected = mycursor.execute(query, (self.share, self.dirSpecial, id))
        if (rowAffected != 0):
            EMP.con.commit()
            super().modify(id)
        else:
            raise Exception("Id Not Found")

class Mgr(EMP):
    def __init__(self):
        self.incentive = 0
        self.mgrSpecial = ""
        super().__init__()

    def __str__(self):
        return "Id: " + str(self.id) + " Name: " + self.name + " Incentive: " + str(
            self.incentive) + " mgrSpecial: " + self.mgrSpecial

    def add(self):
        mycursor = EMP.con.cursor()
        query = "insert into mgr(id,incentive,mgrspecial) values(%s,%s,%s)"
        rowAffected = mycursor.execute(query, (((str(self.id)).title()).strip(), ((str(self.incentive)).title()).strip(), ((self.mgrSpecial).title()).strip()))
        if (rowAffected != 0):
            EMP.con.commit()
        super().add()

    def search(self, id):
        mycursor = EMP.con.cursor()
        query = "select * from mgr where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            row = mycursor.fetchone()
            self.incentive = row[1]
            self.mgrSpecial = row[2]
            super().search(id)
        else:
            raise Exception("Id Not Found")

    def delete(self, id):
        mycursor = EMP.con.cursor()
        query = "delete from mgr where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            super().delete(id)
        else:
            raise Exception("Id Not Found")

    def modify(self, id):
        mycursor = EMP.con.cursor()
        query = "update mgr set incentive=%s,mgrspecial=%s where id=%s"
        rowAffected = mycursor.execute(query, (self.incentive, self.mgrSpecial, id))
        if (rowAffected != 0):
            EMP.con.commit()
            super().modify(id)
        else:
            raise Exception("Id Not Found")

class TT(EMP):
    def __init__(self):
        self.salary = 0
        self.ttSpecial = ""
        super().__init__()

    def __str__(self):
        return "Id: " + str(self.id) + " Name: " + self.name + " Salary: " + str(
            self.salary) + " TTSpecial: " + self.ttSpecial

    def add(self):
        mycursor = EMP.con.cursor()
        query = "insert into tt(id,salary,ttspecial) values(%s,%s,%s)"
        rowAffected = mycursor.execute(query, (((str(self.id)).title()).strip(), ((str(self.salary)).title()).strip(), ((self.ttSpecial).title()).strip()))
        if (rowAffected != 0):
            EMP.con.commit()
        super().add()

    def search(self, id):
        mycursor = EMP.con.cursor()
        query = "select * from tt where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            row = mycursor.fetchone()
            self.salary = row[1]
            self.ttSpecial = row[2]
            super().search(id)
        else:
            raise Exception("Id Not Found")

    def delete(self, id):
        mycursor = EMP.con.cursor()
        query = "delete from tt where id=%s"
        rowAffected = mycursor.execute(query, (id,))
        if (rowAffected != 0):
            super().delete(id)
        else:
            raise Exception("Id Not Found")

    def modify(self, id):
        mycursor = EMP.con.cursor()
        query = "update tt set salary=%s,ttspecial=%s where id=%s"
        rowAffected = mycursor.execute(query, (self.salary, self.ttSpecial, id))
        if (rowAffected != 0):
            EMP.con.commit()
            super().modify(id)
        else:
            raise Exception("Id Not Found")


# Bl End Here


# pl Start from Here

while (True):
    print(
        "\n1) Add Employee\n2) Search Employee\n3) Delete Employee\n4)Modify Employee\n5) Show All Employees\n0)Exit\n")
    ch = input("Enter Your Choice : ")
    if (ch == "1"):
        while (True):
            print("\n1) Add Director\n2) Add Manager\n3) Add Technical Trainer\n0) Exit")
            ch1 = input("Enter Your Choice : ")
            if (ch1 == "1"):
                try:
                    obdir = Dir()
                    obdir.type = "Dir"
                    obdir.id = int(input("Enter Id : "))
                    obdir.name = input("Enter Name : ")
                    obdir.share = int(input("Enter Share : "))
                    obdir.dirSpecial = input("Enter DirSpecial : ")
                    obdir.add()
                    print("Director Added Successfully")

                except Exception as ex:
                    print(ex)

            elif (ch1 == "2"):
                try:
                    obmgr = Mgr()
                    obmgr.type = "Mgr"
                    obmgr.id = int(input("Enter Id : "))
                    obmgr.name = input("Enter Name : ")
                    obmgr.incentive = int(input("Enter Incentive : "))
                    obmgr.mgrSpecial = input("Enter mgrSpecial : ")
                    obmgr.add()
                    print("Manager Added Successfully")
                except Exception as ex:
                    print(ex)

            elif (ch1 == "3"):
                try:
                    obtt = TT()
                    obtt.type = "TT"
                    obtt.id = int(input("Enter Id : "))
                    obtt.name = input("Enter Name : ")
                    obtt.salary = int(input("Enter Salary : "))
                    obtt.ttSpecial = input("Enter ttSpecial : ")
                    obtt.add()
                    print("Trainer Added Successfully")
                except Exception as ex:
                    print(ex)

            elif (ch1 == "0"):
                break

    elif (ch == "2"):
        try:
            id = int(input("Enter Id : "))
            obj = EMP.getObjectbyId(id)
            obj.search(id)
            print(obj)
        except Exception as ex:
            print(ex)

    elif (ch == "3"):
        try:
            id = int(input("Enter Id : "))
            obj = EMP.getObjectbyId(id)
            obj.delete(id)
            print("Employee Deleted successfully")
        except Exception as ex:
            print(ex)

    elif (ch == "4"):
        try:
            id = int(input("Enter Id : "))
            obj = EMP.getTypebyId(id)
            if (obj == "Dir"):
                obdir = Dir()
                obdir.name = input("Enter name : ")
                obdir.share = int(input("Enter share : "))
                obdir.dirSpecial = input("Enter DirSpecial : ")
                obdir.modify(id)

            elif (obj == "Mgr"):
                obmgr = Mgr()
                obmgr.name = input("Enter name : ")
                obmgr.incentive = int(input("Enter Incentive : "))
                obmgr.mgrSpecial = input("Enter MgrSpecial : ")
                obmgr.modify(id)

            elif (obj == "Tt"):
                obtt = TT()
                obtt.name = input("Enter name : ")
                obtt.salary = int(input("Enter Salary : "))
                obtt.ttSpecial = input("Enter TTSpecial : ")
                obtt.modify(id)
            print("Employee Modified successfully")
        except Exception as ex:
            print(ex)

    elif (ch == "5"):
        try:
            em = EMP()
            em.showAllEmployees()
        except Exception as ex:
            print(ex)

    else:
        break
    input("Press Any Key To Continue")

# pl End here
