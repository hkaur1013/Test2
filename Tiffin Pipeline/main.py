import os
import sys
import time
from datetime import timedelta
from datetime import date
import mysql.connector
from tabulate import tabulate
import datetime
import requests

import googlemaps
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

    port="3306"
)
if mydb.is_connected():
    print("you are connected to ", mydb.server_host, " on port number ", mydb
    , "on Database ",
          mydb.database)
    print("My Sql Server info :", mydb.get_server_info())

mycursor = mydb.cursor()


def user_input():
    global serial_no, customer_name, customer_address, start_date, payment, package, comments
    table_selection = input("Press Enter for Regular :: Enter T for oncall Tiffin ")
    if table_selection == "":
        table_name = "tiffin_service"
    else:
        table_name = "on_call_tiffin_service"
    mycursor.execute("Select count(*) FROM sql9602732.{}".format(table_name))
    myresult = mycursor.fetchall()[0][0]
    serial_no = myresult+1
    print("Serial Number Assigned :{}".format(serial_no))
    customer_name = input("Enter Customer Name (varchar)")
    customer_address = input("Enter Customer Address ")
    start_date = input("Enter Start Date (‘1000-01-01’ to ‘9999-12-31’):")
    payment = input("Enter Payment (int)")
    package = input("Enter Package Details like Roties and Subji and Additions ::")
    comments = input("Enter Additional Comments")


def display_all():
    table_name="tiffin_Service"
    for i in range(2):
        mycursor.execute("Select * from sql9602732.{} order by Customer_Address".format(table_name))
        myresult = mycursor.fetchall()
        head = mycursor.column_names
        print(tabulate(myresult, headers=head))
        table_name="on_call_tiffin_service"


def enter_info(serial_no, customer_name, customer_address, start_date, payment, package, comments):
    table_selection=input("Press Enter for Regular :: Enter T for oncall Tiffin ")
    if table_selection=="" :
        table_name="tiffin_service"
    else:
        table_name="on_call_tiffin_service"

    query = "INSERT INTO sql9602732.{} (`Serial_No`, `Customer_Name`, `Customer_Address`, `Start_Date`,`Payment`, `Package`, `Comments`)  VALUES (\"{}\", \"{}\",  \"{}\" , \"{}\",\"{}\", \"{}\", \"{}\" )".format(
        table_name,serial_no, customer_name, customer_address, start_date, payment, package, comments)
    print(query)
    check = input("Press Enter if Query Data is ok ")
    if check == "":
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Data doesnt look fine exiting Program ..")


def update_info():
    table_selection = input("Press Enter for Regular :: Enter T for oncall Tiffin ")
    if table_selection == "":
        table_name = "tiffin_service"
    else:
        table_name = "on_call_tiffin_service"
    mycursor.execute("Select * FROM sql9602732.{}".format(table_name))
    myresult = mycursor.column_names
    mycursor.fetchall()
    print((myresult))
    column_name = input("Enter Column name (use above output for Reference) which will affect ")
    dataupdate = input("Enter data which will replace current data  : ")
    serial_number = input("Enter the Serial number of row which needs updation ")
    query = "update sql9602732.{} set {}='{}' where Serial_No ={}".format(table_name,column_name, dataupdate,
                                                                                       serial_number)
    print(query)
    check = input("Press Enter if Query Data is ok ")
    if check == "":
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")
    else:
        print("Data doesnt look fine exiting Program ..")


def menu_exit():
    print("Request is Complete \n")
    time.sleep(0.5)
    select2 = input("Do you wanna make another Request ( Hit Enter for Yes type N for No ) :")
    if (select2 == ""):
        print("Continue using Program ", end="")
        count = 0
        while (count < 10):
            count = count + 1
            time.sleep(0.1)
            print(".", end="")
        print("\n")
    else:
        print("'Program is now exiting'", end=" ")
        # Python program to illustrate
        # while loop
        count = 0
        while (count < 10):
            count = count + 1
            time.sleep(0.1)
            print(".", end="")
        sys.exit()

def update_Temp_Tiffin_Active() :
    print("Welcome to date updation wizard :")
    mycursor.execute("Select * from sql9602732.on_call_tiffin_service")
    result = mycursor.fetchall()
    head = mycursor.column_names
    print(tabulate(result, headers=head))
    table_name="on_call_tiffin_service"

    mycursor.execute("Select * FROM sql9602732.{}".format(table_name))
    myresult = mycursor.column_names
    mycursor.fetchall()
    print((myresult))
    column_name = "Today_Active"

    dataupdate = input("Enter data which will replace current data  : Enter 1 for Active and 0 for not_Active :")

    serial_number = input("Enter the Serial number of row which needs updation ")
    query = "update sql9602732.{} set {}='{}' where Serial_No ={}".format(table_name,column_name, dataupdate,
                                                                                       serial_number)
    query2 = "update sql9602732.{} set Last_Active_ON_date='{}' where Serial_No ={}".format(table_name, date.today(),
                                                                                       serial_number)
    print(query)
    print("\n")
    check = input("Press Enter if Query Data is ok ")
    if check == "":
        mycursor.execute(query)
        mydb.commit()
        mycursor.execute(query2)
        mydb.commit()
        print("record updated.")
    else:
        print("Data doesnt look fine exiting Program ..")


def update_db_dates():
    print("This will work on only Regular Tiffins.\n")
    mycursor.execute("Select count(*) from sql9602732.Tiffin_Service")
    result = mycursor.fetchall()[0][0]
    print("Number of Rows in table ", result)
    for x in range(result):
        print(x + 1)
        Ser_no = x + 1
        mycursor.execute("Select Start_Date FROM sql9602732.Tiffin_Service where Serial_No={}".format(Ser_no))
        myresult = mycursor.fetchall()[0][0]
        date_1 = myresult
        while (date.today() - timedelta(days=28)) > (date_1):
            date_1 = date_1 + timedelta(days=28)
            print(date_1)
            date_1 = weekend_Correctness(date_1)
        print("Start Date of tiffin ", myresult)

        serial_number = Ser_no
        column_name = "Current_Cycle_StartDate"
        dataupdate = date_1.strftime("%Y-%m-%d")
        print("Curent Cycle Start Date  ", date_1.strftime("%Y-%m-%d"))
        query = "update sql9602732.Tiffin_Service  set {}='{}' where Serial_No ={}".format(column_name, dataupdate,
                                                                                           serial_number)
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")

        print(" Now working on Current Cycle End Date ")
        serial_number = Ser_no
        column_name = "Current_Cycle_EndDate"
        dataupdate = date_1 + timedelta(days=28)
        print("Curent Cycle Start Date  ", date_1.strftime("%Y-%m-%d"))
        query = "update sql9602732.Tiffin_Service  set {}='{}' where Serial_No ={}".format(column_name, dataupdate,
                                                                                           serial_number)
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")


def update_Payment_Column():
    mycursor.execute("Select count(*) from sql9602732.Tiffin_Service")
    result = mycursor.fetchall()[0][0]
    print("Number of Rows in table ", result)
    for x in range(result):
        print(x + 1)
        Ser_no = x + 1
        mycursor.execute("Select Customer_Name FROM sql9602732.Tiffin_Service where Serial_No={}".format(Ser_no))
        myresult = mycursor.fetchall()[0][0]
        serial_number = Ser_no
        column_name = "Current_Cycle_Payment"
        dataupdate = input("did you receive payment from  " + myresult + "  (Enter 1 or 0 only )")
        query = "update sql9602732.Tiffin_Service  set {}='{}' where Serial_No ={}".format(column_name, dataupdate,
                                                                                           serial_number)
        mycursor.execute(query)
        mydb.commit()
        print("record updated.")


def weekend_Correctness(date_1):
    weekno = date_1.weekday()
    if weekno < 5:
        print("Weekday")
    elif weekno < 7:
        date_1 = date_1 + timedelta(days=2)
        print("Weekend: Saturday Adding 2 days")
    elif weekno < 8:
        date_1 = date_1 + timedelta(days=1)
        print("Weekend: Sunday Adding 1 days")
    return date_1


def print_Addresses():
    mycursor.execute("Select Customer_Name from tiffin_service where is_active=1 ;")
    Name_Result = mycursor.fetchall()

    mycursor.execute("Select Customer_Address from tiffin_service where is_active=1 ;")
    myresult = mycursor.fetchall()

    mycursor.execute("Select Package from tiffin_service where is_active=1 ;")
    package_result = mycursor.fetchall()

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
        file.close()
        file = open("demofile.txt", "r")
        print(file.read())
        os.startfile("demofile.txt", "print")
        file.close()
        time.sleep(0.5)



def print_Addresses_on_Weekend():
    mycursor.execute("Select Customer_Name from tiffin_service where Active_On_weekend=1 ;")
    Name_Result = mycursor.fetchall()

    mycursor.execute("Select Customer_Address from tiffin_service where Active_On_weekend=1 ;")
    myresult = mycursor.fetchall()

    mycursor.execute("Select Package from tiffin_service where Active_On_weekend=1 ;")
    package_result = mycursor.fetchall()

    mycursor.execute("Select count(*) from sql9602732.Tiffin_Service where Active_On_weekend=1")
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
        file.close()
        file = open("demofile.txt", "r")
        print(file.read())
        os.startfile("demofile.txt", "print")
        file.close()
        time.sleep(0.5)


def upcoming_payments():
    mycursor.execute(
        "Select Customer_Name,Customer_Phone_Number ,Current_Cycle_StartDate,Current_Cycle_EndDate,Payment from sql9602732.Tiffin_Service")
    myresult = mycursor.fetchall()
    head = mycursor.column_names
    # displaytable
    print(tabulate(myresult, headers=head, tablefmt="grid"))

    mycursor.execute("Select sum(Payment) from sql9602732.Tiffin_Service  where Current_Cycle_Payment=0")
    myresult = mycursor.fetchall()[0][0]
    print("Total Revenue Needs to Collect is {} Dollars".format(myresult))


def packages_of_Roties(self):
    Eight = 0
    Ten = 0
    Six = 0
    Four = 0
    Twelve = 0
    mycursor.execute("Select count(*) from sql9602732.tiffin_Service Where is_active=1")
    result = mycursor.fetchall()[0][0]
    print("Number of Rows in table ", result)
    for x in range(result):
        Ser_no = x + 1
        mycursor.execute("Select left(Package,2) FROM sql9602732.Tiffin_Service where Serial_No={}".format(Ser_no))
        myresult = mycursor.fetchall()[0][0]
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
        mycursor.execute("Select left(Package,1) FROM sql9602732.Tiffin_Service where Serial_No={}".format(Ser_no))
        myresult = mycursor.fetchall()[0][0]
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


def menu(self):
    x = [["Press 1 for Displaying Current Data in Db"],
         ["Press 2 to add new Customers "],
         ["Press 3 for updating existing Record"],
         ["Press 4 to check upcoming payment collections "],
         ["Press 5 to check connection with Db & Auto Populate dates "],
         ["Press 6 to Print all the addresses "],
         ["Press 7 to Print Packages of Roties that needs to make "],
         ["Press 8 for update payment Received ( Current_Cycle_Pay ) "],
         ["Press 9 to Update Longitude/Latitude Data "],
         ["Press 10 to Print Weekend Tiffin "],
         ["Press 11 to Temp Tiffin activation "],

         ["Press 12 to exit the program "]]
    print(tabulate(x, tablefmt="grid"))
    print('\033[1m' + "--------------------------------------------------\n")
    Selection_from_Menu(self)


def Selection_from_Menu(self):
    Selection = input('\033[1m' + "Enter your Selection here  :: ")
    if Selection == "1":
        display_all()
        menu_exit()

    if Selection == "2":
        user_input()
        enter_info(serial_no, customer_name, customer_address, start_date, payment, package, comments)
        menu_exit()

    if Selection == "3":
        update_info()
        menu_exit()
    if Selection == "4":
        upcoming_payments()
        menu_exit()

    if Selection == "5":
        if mydb.is_connected():
            print("you are Connected to DB with connection ID of ", mydb.connection_id)
        update_db_dates()
        menu_exit()
    if Selection == "6":
        print_Addresses()

    if Selection == "7":
        print("Packages Needs to be made today : ")
        packages_of_Roties(self)

    if Selection == "8":
        print("Welcome to Payment updation  Wizard  : ")
        update_Payment_Column()
    if Selection == "9":
        print("Welcome to Long/Lats updation  Wizard  : ")
        update_Long_Lats_data()

    if Selection == "10":
        print_Addresses_on_Weekend()

    if Selection == "11":
        update_Temp_Tiffin_Active()
    if Selection == "12":
        print("Program is now exiting ", end=" ")
        # Python program to illustrate
        # while loop
        count = 0
        while count < 10:
            count = count + 1
            time.sleep(0.5)
            print(".", end="")
        sys.exit()
    if (Selection != "1") and (
            Selection != "2") \
            and Selection != "3" \
            and Selection != "4" \
            and Selection != "5" \
            and Selection != "6" \
            and Selection != "7" \
            and Selection != "8" \
            and Selection != "9" \
            and Selection != "10" \
            and Selection!="11":
        print(Selection, ' Is a Wrong Entry')


def update_Long_Lats_data():
    table_selection = input("Press Enter for Regular :: Enter T for oncall Tiffin ")
    if table_selection == "":
        table_name = "tiffin_service"
    else:
        table_name = "on_call_tiffin_service"

    gmaps = googlemaps.Client(key='AIzaSyCsKWGrRnvlKXHlfbhz30TagYg7AFE0mfA')
    api_key = "AIzaSyCsKWGrRnvlKXHlfbhz30TagYg7AFE0mfA"
    Restaurant_address="75 Dundas St. N Cambridge"
    Start_Point = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(Restaurant_address, api_key))
    Start_Point_dict = Start_Point.json()
    latitude_Address = Start_Point_dict['results'][0]['geometry']['location']['lat']
    longitude_Address = Start_Point_dict['results'][0]['geometry']['location']['lng']
    reverse_geocode_result_Start_Point = gmaps.reverse_geocode((latitude_Address, longitude_Address))
    Start_Address=reverse_geocode_result_Start_Point[0]['formatted_address']
    print(reverse_geocode_result_Start_Point[0]['formatted_address'])
    # Geocoding an address
    mycursor.execute("Select count(*) from sql9602732.{}".format(table_name))
    result = mycursor.fetchall()[0][0]
    mycursor.execute("Select Customer_Address from sql9602732.{}".format(table_name))
    Address_result = mycursor.fetchall()
    for x in range(result):
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(Address_result[x][0], api_key))
        api_response_dict = api_response.json()
        print(".")
        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            mycursor.execute("update sql9602732.{} set Longitude={},Latitude={} where Serial_No={}".format(table_name,longitude,latitude,x+1))
            mydb.commit()
            reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
            print(reverse_geocode_result[0]['formatted_address'])
            addressvalidation_result = gmaps.addressvalidation((reverse_geocode_result[0]['formatted_address']))
            print(addressvalidation_result['result']['verdict']['addressComplete'])



            # directions_result = gmaps.directions(Start_Address,
            #                                       reverse_geocode_result[0]['formatted_address'],
            #                                       departure_time=datetime.time)
            # print(directions_result)

    print("Data Updation Completed.")
    # # Look up an address with reverse geocoding

    #
    # # Request directions via public transit
    # now = datetime.now()
    # directions_result = gmaps.directions("Sydney Town Hall",
    #                                      "Parramatta, NSW",
    #                                      mode="transit",
    #                                      departure_time=now)
    #
    # # Validate an address with address validation
    # addressvalidation_result = gmaps.addressvalidation(['1600 Amphitheatre Pk'],
    #                                                    regionCode='US',
    #                                                    locality='Mountain View',
    #                                                    enableUspsCass=True)
    #


# while loop
count = 0
while (count < 1):
    menu(self="")