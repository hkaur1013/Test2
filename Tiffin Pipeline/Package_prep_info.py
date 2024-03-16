####
import os
import sys
import time
from datetime import timedelta
from datetime import date
import mysql.connector
from tabulate import tabulate
import datetime
from datetime import datetime
import requests
import googlemaps
serial_no = 0
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

    port="3306"
)
if mydb.is_connected():
    print("you are connected to ", mydb.server_host, " on port number ", mydb
    , "on Database ",
          mydb.database)
    print("My Sql Server info :", mydb.get_server_info())

mycursor = mydb.cursor()


def packages_of_Roties():
    Eight = 0
    Ten = 0
    Six = 0
    Four = 0
    Twelve = 0
    Five = 0
    mycursor.execute("Select count(*) from sql9602732.tiffin_Service Where is_active=1")
    result = mycursor.fetchall()[0][0]
    print("Number of Rows in table ", result)
    mycursor.execute("Select left(Package,2) FROM sql9602732.Tiffin_Service where  is_active=1")
    for x in range(result):
        Ser_no = x + 1
#        mycursor.execute("Select left(Package,2) FROM sql9602732.Tiffin_Service where  is_active=1")
        myresult = mycursor.fetchall()[x][0]
        if myresult == "8":
            Eight = Eight + 1
        if myresult == "4":
            Four = Four + 1
        if myresult == "10":
            Ten = Ten + 1
        if myresult == "6":
            Six = Six + 1
        if myresult == "12":
            Twelve = Twelve + 1
        if myresult == "5":
            Five == Five +1


    mycursor.execute("Select left(Package,1) FROM sql9602732.Tiffin_Service where  is_active=1")
    for x in range(result):
        myresult = mycursor.fetchall()[x][0]
        if myresult == "8":
            Eight = Eight + 1
        if myresult == "4":
            Four = Four + 1
        if myresult == "10":
            Ten = Ten + 1
        if myresult == "6":
            Six = Six + 1
        if myresult == "12":
            Twelve = Twelve + 1
        if myresult == "5":
            Five == Five +1

    print("----------------------------- \n")
    if(Twelve>0):
        print("Twelve Packages {}  \n".format(Twelve))
    if (Ten>0):
        print("Ten Packages {}  \n".format(Ten))
    if (Eight>0):
        print("Eight Packages {} \n ".format(Eight))
    if (Six>0):
        print("Six Packages {} \n".format(Six))

    if (Five>0):
        print("Five Packages {} \n".format(Five))
    if (Four>0):
        print("Four Packages {} \n".format(Four))

    if os.path.exists("roties.txt"):
        os.remove("roties.txt")
    file = open("roties.txt", "x")
    file.write("TIKKA TIMEZ Roties \n")
    file.write("-------------------\n")
    if Twelve>0:
        file.write("Twelve Packages {}  \n".format(Twelve))
    if (Ten>0):
        file.write("Ten Packages {}  \n".format(Ten))
    if (Eight>0):
        file.write("Eight Packages {}  \n".format(Eight))
    if (Six>0):
        file.write("Six Packages {}  \n".format(Six))
    if (Five>0):
        file.write("Five Packages {}  \n".format(Five))



    if (Four>0):
        file.write("Four Packages {}  \n".format(Four))

    file.write("--------------------\n")

    file.close()
    file = open("roties.txt", "r")
    print(file.read())
    os.startfile("roties.txt", "print")


def packages_of_Roties_weekend():
    Eight = 0
    Ten = 0
    Six = 0
    Four = 0
    Twelve = 0
    mycursor.execute("Select count(*) from sql9602732.tiffin_Service Where  is_active=1")
    result = mycursor.fetchall()[0][0]
    print("Number of Rows in table ", result)
    for x in range(result):
        mycursor.execute("Select left(Package,2) FROM sql9602732.Tiffin_Service where is_active=1 ")
        myresult = mycursor.fetchall()[x][0]
        print (myresult)
        if myresult == "8":
            Eight = Eight + 1
        if myresult == "4":
            Four = Four + 1
        if myresult == "10":
            Ten = Ten + 1
        if myresult == "6":
            Six = Six + 1
        if myresult == "12":
            Twelve = Twelve + 1
        mycursor.execute("Select left(Package,1) FROM sql9602732.Tiffin_Service where is_active=1 ")
        myresult = mycursor.fetchall()[x][0]
        if myresult == "8":
            Eight = Eight + 1
        if myresult == "4":
            Four = Four + 1
        if myresult == "10":
            Ten = Ten + 1
        if myresult == "6":
            Six = Six + 1
        if myresult == "12":
            Twelve = Twelve + 1
    print("----------------------------- \n")
    print("Twelve Packages {}  \n".format(Twelve))
    print("Ten Packages {}  \n".format(Ten))
    print("Eight Packages {} \n ".format(Eight))
    print("Six Packages {} \n".format(Six))
    print("Four Packages {} \n".format(Four))

    if os.path.exists("roties.txt"):
        os.remove("roties.txt")
    file = open("roties.txt", "x")
    file.write("TIKKA TIMEZ Roties \n")
    file.write("-------------------\n")
    file.write("Twelve Packages {}  \n".format(Twelve))
    file.write("Ten Packages {}  \n".format(Ten))
    file.write("Eight Packages {}  \n".format(Eight))
    file.write("Six Packages {}  \n".format(Six))
    file.write("Four Packages {}  \n".format(Four))
    file.write("--------------------\n")

    file.close()
    file = open("roties.txt", "r")
    print(file.read())
    os.startfile("roties.txt", "print")
def update_active_for_weekday():
    print ("Current Execution time " )
    print   (datetime.now())
    if datetime.today().weekday() == 3 or datetime.today().weekday() == 4:
        print ("Today is "+ datetime.today().strftime('%A'))
        print ("Hence , Disabling Tiffins with weekday disable flag active : ")
        mycursor.execute("Select * from sql9602732.Tiffin_Service where weekday_disable_flag=1")
        mycursor.fetchall()[0][0]
        query = "update sql9602732.Tiffin_Service  set is_active=0 where weekday_disable_flag=1"
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")
    else:
        query = "update sql9602732.Tiffin_Service  set is_active=1 where weekday_disable_flag=1"
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")

#update_active_for_weekday()
#if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
#     packages_of_Roties_weekend()
#else:

packages_of_Roties()

#packages_of_Roties_weekend()
