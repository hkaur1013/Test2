####
import os
import sys
import time
from datetime import timedelta
from datetime import date
import mysql.connector
from pathlib import Path
import pypdf
from pypdf import PdfReader
from pypdf import PdfWriter
import PyPDF2
from PyPDF2 import PaperSize

serial_no = 0
customer_name = ""
customer_address = ""
start_date = ""
payment = 1
package = ""
comments = ""
global date_1

mydb = mysql.connector.connect(
    #    host="127.0.0.1",
    host="70.48.31.76",
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
    #   mycursor.execute("Select Roties_package  from sql9602732.tiffin_Service Where is_active=1")
    for x in range(result):
        mycursor.execute("Select Roties_package  from sql9602732.tiffin_Service Where is_active=1")
        myresult = mycursor.fetchall()[x][0]
        print(myresult)
        if myresult == 8:
            Eight = Eight + 1
        if myresult == 4:
            Four = Four + 1
        if myresult == 5:
            Five = Five + 1
        if myresult == 10:
            Ten = Ten + 1
        if myresult == 6:
            Six = Six + 1
        if myresult == 12:
            Twelve = Twelve + 1

    print("----------------------------- \n")

    mycursor.execute("Select  SUM(Roties_package)  from sql9602732.tiffin_Service Where is_active=1")
    TotalRoties = mycursor.fetchall()[0][0]

    mycursor.execute("Select  SUM(Rice_package)  from sql9602732.tiffin_Service Where is_active=1")
    Rice = mycursor.fetchall()[0][0]

    mycursor.execute("Select  SUM(Curry_package)  from sql9602732.tiffin_Service Where is_active=1")
    Curries = mycursor.fetchall()[0][0]

    mycursor.execute("Select  SUM(DrySubji_package)  from sql9602732.tiffin_Service Where is_active=1")
    DrySubji = mycursor.fetchall()[0][0]

    mycursor.execute("Select SUM(Yogurt_package)  from sql9602732.tiffin_Service Where is_active=1")
    Yogurt8oz = mycursor.fetchall()[0][0]

    mycursor.execute("Select SUM(Yogurt_4oz_package)  from sql9602732.tiffin_Service Where is_active=1")
    Yogurt4oz = mycursor.fetchall()[0][0]

    mycursor.execute("Select SUM(Yogurt_4oz_package)  from sql9602732.tiffin_Service Where is_active=1")
    Friday_sweets = mycursor.fetchall()[0][0]

    print(Twelve, Ten, Five, Four, Eight, Six)
    if (Twelve > 0):
        print("Twelve Packages {}  \n".format(Twelve))
    if (Ten > 0):
        print("Ten Packages {}  \n".format(Ten))
    if (Eight > 0):
        print("Eight Packages {} \n ".format(Eight))
    if (Six > 0):
        print("Six Packages {} \n".format(Six))

    if (Five > 0):
        print("Five Packages {} \n".format(Five))
    if (Four > 0):
        print("Four Packages {} \n".format(Four))

    if os.path.exists("roties.txt"):
        os.remove("roties.txt")
    file = open("roties.txt", "x")
    file.write("TIKKA TIMEZ Kitchen Req.\n")
    file.write("-------------------\n")
    today = date.today()
    file.write(today.strftime("%B %d , %Y\n"))
    file.write("-------------------\n")
    if Twelve > 0:
        file.write("Twelve Packages {}  \n".format(Twelve))
    if (Ten > 0):
        file.write("Ten Packages {}  \n".format(Ten))
    if (Eight > 0):
        file.write("Eight Packages {}  \n".format(Eight))
    if (Six > 0):
        file.write("Six Packages {}  \n".format(Six))
    if (Five > 0):
        file.write("Five Packages {}  \n".format(Five))
    if (Four > 0):
        file.write("Four Packages {}  \n".format(Four))

    file.write("--------------------\n")
    if Rice > 0:
        file.write("Total Rice Required   {} \n".format(Rice))
    if DrySubji > 0:
        file.write("Total DrySubji Required   {} \n".format(DrySubji))
    if Curries > 0:
        file.write("Total Curries Required   {} \n".format(Curries))
    if Yogurt8oz > 0:
        file.write("Total Yogurt 8oz Required   {} \n".format(Yogurt8oz))
    if Yogurt4oz > 0:
        file.write("Total Yogurt 4oz Required   {} \n".format(Yogurt4oz))
    if Friday_sweets > 0:
        file.write("Total Friday Sweets Required   {} \n".format(Friday_sweets))
    if TotalRoties > 0:
        file.write("Total Roties Required   {} \n".format(TotalRoties))
    file.write("Estimate Flour usage is {}  Kg. \n".format(TotalRoties * 50 / 1000))
    file.close()
    file = open("roties.txt", "r")
    print(file.read())
    os.startfile("roties.txt", "print")





packages_of_Roties()
