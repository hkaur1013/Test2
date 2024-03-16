import os
import time
import mysql.connector
import datetime
from datetime import datetime

serial_no = 1
customer_name = ""
customer_address = ""
start_date = ""
payment = 1
package = ""
comments = ""
global date_1
mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="sql9602732",
            password="Gmsshn!43",
            port="3306")
if mydb.is_connected():
            print("you are connected to ", mydb.server_host, " on port number ", mydb, "on Database ", mydb.database)
            print("My Sql Server info :", mydb.get_server_info())
            mycursor = mydb.cursor()

class MyClass:
    def print_Addresses():
        mycursor.execute("Select Customer_Name from tiffin_service where is_active=1 ;")
        Name_Result = mycursor.fetchall()

        mycursor.execute("Select Customer_Address from tiffin_service where is_active=1 ;")
        myresult = mycursor.fetchall()

        mycursor.execute("Select Package from tiffin_service where is_active=1 ;")
        package_result = mycursor.fetchall()

        mycursor.execute("Select Current_Cycle_EndDate from tiffin_service where is_active=1 ;")
        Current_CycleEndDate = mycursor.fetchall()

        mycursor.execute("Select count(*) from sql9602732.Tiffin_Service where is_active=1")
        result = mycursor.fetchall()[0][0]
        print("Number of Rows in table ", result)
        for x in range(result):
            if os.path.exists("demofile.txt"):
                os.remove("demofile.txt")
            file = open("demofile.txt", "x")
            file.write(Name_Result[x][0] + "\n")
            file.write("-----------------\n")
            file.write(myresult[x][0])
            file.write("\n")
            file.write("-----------------\n")
            file.write(package_result[x][0])
            file.write("\n")
            file.write("-----------------\n")
            file.write(Current_CycleEndDate[x][0].strftime("%B %d, %Y"))
            file.write("\n")
            file.write("-----------------\n")
            file.close()
            file = open("demofile.txt", "r")
            print(file.read())
            os.startfile("demofile.txt", "print")
            file.close()
            time.sleep(1)

    ## below job is being used in update_tiffinFlags.py file
    def update_active_as_per_day_flag():
        print("Current Execution time ")
        mycursor.execute("update sql9602732.Tiffin_Service  set is_active=0 ;")
        print(datetime.now())
        print("Loop Starts now")
        if datetime.today().weekday() == 0:
            print("Today is " + datetime.today().strftime('%A'))
            print("Hence , Disabling Tiffins with weekday disable flag active : ")
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Monday=1 and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Monday=1 and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")

        elif datetime.today().weekday() == 1:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Tuesday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Tuesday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")
        elif datetime.today().weekday() == 2:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Wednesday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Wednesday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")
        elif datetime.today().weekday() == 3:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Thursday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Thursday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")
        elif datetime.today().weekday() == 4:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Friday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Friday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")

        elif datetime.today().weekday() == 5:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Saturday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Saturday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated.")
        elif datetime.today().weekday() == 6:
            print("Today is " + datetime.today().strftime('%A'))
            mycursor.execute("Select * from sql9602732.Tiffin_Service where Sunday=1  and is_active_master=1")
            mycursor.fetchall()[0][0]
            query = "update sql9602732.Tiffin_Service  set is_active=1 where Sunday=1  and is_active_master=1"
            mycursor.execute(query)
            mydb.commit()
            print("record updated." + "Sunday")


MyClass.update_active_as_per_day_flag()
MyClass.print_Addresses()
