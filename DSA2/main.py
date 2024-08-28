#Student ID: 010843872

import csv
import datetime
import time
from datetime import datetime, timedelta
from PackageData import PackageData
from Truck import Truck
from hashtable2 import hashtable

# truck.time += datetime.timedelta(hours=next_address / 18)

myHash = hashtable()


#This function stores each row inside of the Distance Data csv into a 2d list for later use

def loadDistanceData(filename):
    distanceList = []
    with open(filename, 'r') as deliverydata:
        reader = csv.reader(deliverydata, delimiter=',')
        data = [row for row in reader]

        # arr = list(map(str.split, deliverydata))
    return data




#This variable is used to reference the 2d list created in the loadDistanceData csv
distanceValues = loadDistanceData("WGUPS Distance Data.csv")



#This function stores the addresses inside of the Addresses.csv file into a list for later use
def loadAddresses(filename):
    distanceList = []
    with open(filename, 'r') as package_data:
        reader = csv.reader(package_data, delimiter=',')
        lines = [i.strip() for i in package_data]
        for data in reader:
            actual_data = [item.strip() for item in data]
            distanceList.append(data)
        return lines

#Variable to reference the address list created
addresses = (loadAddresses("Addresses.csv"))


#This function finds the index of the param address
def findAddressIndex(address):
    for i in range(len(addresses)):
        if addresses[i] == address:
            return i


#print(findAddressIndex("177 W Price Ave"))

#This function takes two addresses and finds the distance between them
def getDistanceFromAddresses(current, next_address):
    current_index = findAddressIndex(current)
    next_index = findAddressIndex(next_address)
    try:
        # print(current_index)
        # print(current)
        # print(next_index)
        # print(next_address)
        value = distanceValues[current_index][next_index]
        return value
    except IndexError:
        # if(distanceValues[current_index][next_index]==None):
        return distanceValues[next_index][current_index]


#print(getDistanceFromAddresses("4001 South 700 East", "1330 2100 S"))

#This function creates a package object for each row inside of the Package File csv. Then it stores it inside of the hashtable

def loadPackageData(fileName):
    with open(fileName) as packages:
        data = csv.reader(packages, delimiter=',')
        next(data)
        for d in data:
            ids = int(d[0])
            address = d[1]
            city = d[2]
            state = d[3]
            zipcode = d[4]
            deadline = d[5]
            weight = d[6]
            #print(ids,address)
            package = PackageData(ids, address, deadline, city, zipcode, state, "At Hub", weight)
            #print(address)
            myHash.add(ids, package)

#Used to store the packages into the hash table
loadPackageData("WGUPS Package File.csv")

# These lines of code creates truck objects and intializes the time they leave as well as current location
truck1_time = timedelta(hours=8, minutes=0)
truck1 = Truck(1, '4001 South 700 East', truck1_time,truck1_time)
truck1.time_of_depart = timedelta(hours=8, minutes=0)
time_of_depart = "09:05"
add_time = 0
hours, minutes = map(int, time_of_depart.split(":"))
#print(myHash.get_package_address_by_id(1))
truck2_time = timedelta(hours=9, minutes=5)
truck3_time = timedelta(hours=10, minutes=20)
truck2 = Truck(2, '4001 South 700 East', truck2_time,truck2_time)
truck3 = Truck(3, '4001 South 700 East', truck3_time,truck3_time)
print(getDistanceFromAddresses("4001 South 700 East", myHash.get_package_address_by_id(32)))

#Manualing adding the packages to truck1
truck1.packages.append(myHash.get_package_by_id(1))
truck1.packages.append(myHash.get_package_by_id(15))
truck1.packages.append(myHash.get_package_by_id(13))
truck1.packages.append(myHash.get_package_by_id(16))
truck1.packages.append(myHash.get_package_by_id(14))
truck1.packages.append(myHash.get_package_by_id(20))
truck1.packages.append(myHash.get_package_by_id(27))
truck1.packages.append(myHash.get_package_by_id(29))
truck1.packages.append(myHash.get_package_by_id(30))
truck1.packages.append(myHash.get_package_by_id(31))
truck1.packages.append(myHash.get_package_by_id(33))
truck1.packages.append(myHash.get_package_by_id(34))
truck1.packages.append(myHash.get_package_by_id(19))
truck1.packages.append(myHash.get_package_by_id(21))
truck1.packages.append(myHash.get_package_by_id(32))
truck1.packages.append(myHash.get_package_by_id(40))

truck2.packages.append(myHash.get_package_by_id(3))
truck2.packages.append(myHash.get_package_by_id(6))
truck2.packages.append(myHash.get_package_by_id(25))
truck2.packages.append(myHash.get_package_by_id(28))
truck2.packages.append(myHash.get_package_by_id(36))
truck2.packages.append(myHash.get_package_by_id(40))
truck2.packages.append(myHash.get_package_by_id(18))
truck2.packages.append(myHash.get_package_by_id(35))
truck2.packages.append(myHash.get_package_by_id(39))
truck2.packages.append(myHash.get_package_by_id(5))
truck2.packages.append(myHash.get_package_by_id(37))
truck2.packages.append(myHash.get_package_by_id(38))

print("---------------")
print(myHash.get(1))
# truck2 packages not arriving until 9:05:6,25,28,32
truck3.packages.append(myHash.get_package_by_id(9))
truck3.packages.append(myHash.get_package_by_id(2))
truck3.packages.append(myHash.get_package_by_id(4))
truck3.packages.append(myHash.get_package_by_id(7))
truck3.packages.append(myHash.get_package_by_id(8))
truck3.packages.append(myHash.get_package_by_id(10))
truck3.packages.append(myHash.get_package_by_id(11))
truck3.packages.append(myHash.get_package_by_id(12))
truck3.packages.append(myHash.get_package_by_id(17))
truck3.packages.append(myHash.get_package_by_id(22))
truck3.packages.append(myHash.get_package_by_id(23))
truck3.packages.append(myHash.get_package_by_id(24))
truck3.packages.append(myHash.get_package_by_id(26))






# print(undelivered_packages)




#The below are added methods I didn't use but may be useful
def get_status_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.status


def get_address_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.address


# dictionary string address is key, index of address is value
def get_deadline_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.deadline


def get_weight_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.weight


def get_city_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.city


def get_zipcode_of_package_by_id(id):
    package = myHash.get_package_by_id(id)
    return package.zipcode


print("---Check Address---")
print(getDistanceFromAddresses("4001 South 700 East", myHash.get_package_address_by_id(1)))


#These variables are not used
status_hub = "At Hub"
status_en_route = "en route"
status_delivered = "Delivered at: "

truck1_miles = 0

global_time=timedelta(hours=8,minutes=0)

truck1_time=timedelta(hours=8,minutes=0)
truck2_time=timedelta(hours=9,minutes=10)
truck3_time=timedelta(hours=10,minutes=20)
total_miles=0

#This recursive function takes a truck as a parameter and initializes the shortest distance and next location
#If packages are 0 then the truck returns to WGU, if the ID is 3 then it returns and adds the mileage for that truck
def deliver_package(truck):


    current_address = truck.location
    shortest_distance = 0
    next_location = " "
    next_index=0
    package_index = 0
    if len(truck.packages) == 0 and truck.ID==3:
        shortest_distance = getDistanceFromAddresses(truck.location, "4001 South 700 East")
        truck.location = "4001 South 700 East"
        truck.miles = truck.miles+ float(shortest_distance)
        _time = float(shortest_distance)
        final_time=truck.truck_current_time+timedelta(hours=_time / 18)
        print("Truck "+str(truck.ID) + " has returned to Hub at " +str(final_time) )
        return float(truck.miles)
    if len(truck.packages)==0:
        shortest_distance = getDistanceFromAddresses(truck.location, "4001 South 700 East")
        truck.location = "4001 South 700 East"
        truck.location="4001 South 700 East"
        _time = float(shortest_distance)
        final_time = truck.truck_current_time + timedelta(hours=_time / 18)
        print("Truck "+str(truck.ID) + " has returned to Hub at " +str(final_time) )
        return float(truck.miles)
    if truck.ID==3:
        package=myHash.get_package_by_id(9)
        package.address="410 S State St"
        package.zipcode="84111"
        print(package)
    # This loop sets the time the packages left the HUB
    for package in truck.packages:
        package.time_left_hub=truck.time_of_depart
        package.truck_id=truck.ID
        #print(package.time_left_hub)

#Sets the shortest
    for i in range(len(truck.packages)):
        next_index = i + 1
        next_distance = float(getDistanceFromAddresses(truck.location, truck.packages[i].get_address()))
        if i == 0 and len(truck.packages) > 0:
            shortest_distance =float (getDistanceFromAddresses(truck.location, truck.packages[i].get_address()))
            next_location = truck.packages[i].get_address()



        elif ( (i >= 1) and (len(truck.packages) > 0 ) and (next_index < len(truck.packages)) and (shortest_distance> next_distance)) :
            #current_distance = getDistanceFromAddresses(truck.location, truck.packages[i].get_address())

            #if current_distance < shortest_distance:
                #shortest_distance = current_distance
                shortest_distance=next_distance
                next_location = truck.packages[i].get_address()

                print(shortest_distance, truck.location, next_location)
            # print(shortest_distance)
        # print(truck.packages[i].get_address())

        # truck.time_of_depart += addTimeForDelivery(shortest_distance) can't add until next address is certain
        # truck_time_delta_temp=timedelta(seconds=truck.time_of_depart)

    truck.location = next_location
    _time = float(shortest_distance)
    truck.truck_current_time = truck.truck_current_time+timedelta(hours=_time / 18)
    #problem is time is reset each time a package is delivered, time must persist
   # time_added = truck.time_of_depart + timedelta(hours=_time / 18)
    packages_to_remove=[]
    for package in truck.packages:
        if package.get_address() == next_location:
            print(truck.packages)
            print(package.ids)
            packages_to_remove.append(package)
            package.delivery_time=truck.truck_current_time
            package.status= "Delivered at: "+str(package.delivery_time) +"by Truck: " + str(truck.ID)
            #truck.packages.remove(package)

    for package in packages_to_remove:
        truck.packages.remove(package)

    packages_to_remove.clear()



    

    actual_miles = float(shortest_distance)
    # print(shortest_distance)
    truck.miles = truck.miles+actual_miles
    # print(len(truck.packages))
    #print("-------------------")
    print(truck.miles)

    if len(truck.packages) >= 0:
        deliver_package(truck)



#total_miles=deliver_package(truck1)+ deliver_package(truck2)+ deliver_package(truck3)
print("-------------")
#print(total_miles)



truck2.packages.append(myHash.get_package_by_id(3))

# myHash.print()


#   shortest_distance > getDistanceFromAddresses(truck.location,truck.packages[i].get_address)

#No need for back to main menu options
deliver_package(truck1)
deliver_package(truck2)
deliver_package(truck3)

print(myHash.get_package_address_by_id(9))
total_miles_all=truck1.miles+truck2.miles+truck3.miles
#print("-------")
#print(total_miles_all)

is_exit=True
def user_interface():

    print("Welcome to WGUPS! Trucks have been sent out to complete deliveries. Choose an option")
    print("1. List all package statuses after deliveries complete with total mileage of all trucks")
    print("2. Get Status for a specific package at a specific time")
    print("3. List all package statuses for a specific time")
    print("4. Exit program ")
    while True:
        option = input("Click here: ")
        if option in ('1', '2', '3', '4'):
            break
        else:
            print("You must choose a correct option")

    if option == '1':
        pack_9 = myHash.get_package_by_id(9)
        pack_9.address = "410 S State St"
        pack_9.zipcode = "84111"
        print("PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
        for i in range(1, 41):
            print(myHash.get_package_by_id(i))
        print("Truck 1 traveled " + str(truck1.miles) +"miles")
        print("Truck 2 traveled " + str(truck2.miles) + "miles")
        print("Truck 3 traveled " + str(truck3.miles) + "miles")
        print("Total Miles:" + str(total_miles_all))
        '''
        # next_choice = input("Return to main Page Press any key")
        if next_choice == y or next_choice == Y:
        #user_interface()
        except NameError:
        #user_interface()
        '''

    if option=='2':
      # try:
        option_2=input("Enter a package ID to see that packages Information: ")
        ID_cast=int(option_2)
        at_time=input("Enter a time to see that packages status at that time in HH:MM format (Military Time): ")
        parsed_time = datetime.strptime(at_time, "%H:%M")
        result_time = timedelta(hours=parsed_time.hour, minutes=parsed_time.minute)
        package_9=timedelta(hours=10, minutes=20)

        if ID_cast ==9 and result_time < package_9:
             pack_9=myHash.get_package_by_id(9)
             pack_9.address="300 State St"
             pack_9.zipcode="84103"
             print("PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
             print(myHash.get_package_by_id(ID_cast).get_status(result_time))
        elif ID_cast ==9 and result_time >= package_9:
            pack_9 = myHash.get_package_by_id(9)
            pack_9.address = "410 S State St"
            pack_9.zipcode = "84111"
            print("PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
            print(myHash.get_package_by_id(ID_cast).get_status(result_time))
        if ID_cast>=1 and ID_cast <=40:

            print("PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
            print(myHash.get_package_by_id(ID_cast).get_status(result_time))
        else:
            print("Value must be between 1 and 40")
            #user_interface()
       #except ValueError:
            #print("You must enter a valid package ID from 1 to 40 and a valid time")
            #user_interface()
    if option=='3':
        #try:
            time_input=input("Enter a time in the form of HH:MM to view all package statuses at that time (Military Time): ")
            parsed_time=datetime.strptime(time_input, "%H:%M")
            result_time=timedelta(hours=parsed_time.hour, minutes=parsed_time.minute)
            package_9 = timedelta(hours=10, minutes=20)
            if result_time <package_9:
                pack_9 = myHash.get_package_by_id(9)
                pack_9.address = "300 State St"
                pack_9.zipcode = "84103"
                print(
                    "PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
                for i in range(1, 41):
                  print(myHash.get_package_by_id(i).get_status(result_time) )
                print("Truck 1 traveled " + str(truck1.miles) + "miles")
                print("Truck 2 traveled " + str(truck2.miles) + "miles")
                print("Truck 3 traveled " + str(truck3.miles) + "miles")
                print("Total Miles:" + str(total_miles_all))
                print("Total time traveled by all trucks once done with deliveries= " + str(total_miles_all))
            elif result_time>= package_9:
                pack_9 = myHash.get_package_by_id(9)
                pack_9.address = "410 S State St"
                pack_9.zipcode = "84111"
                print(
                    "PackageID, Address,Deadline, City,  Zip, State, Status , Weight, Time of Depart, Time of Delivery")
                for j in range(1, 41):
                    print(myHash.get_package_by_id(j).get_status(result_time))
                print("Truck 1 traveled " + str(truck1.miles) + "miles")
                print("Truck 2 traveled " + str(truck2.miles) + "miles")
                print("Truck 3 traveled " + str(truck3.miles) + "miles")
                print("Total Miles:" + str(total_miles_all))
                print("Total time traveled by all trucks once done with deliveries= " + str(total_miles_all))
        #except ValueError:
           #print("Enter a time in the valid form")
           #user_interface()

    if option=='4':
        global is_exit
        is_exit=False


while (is_exit):
   user_interface()



