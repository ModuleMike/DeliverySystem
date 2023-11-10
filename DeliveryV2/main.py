# Michael Lubomski ID# 010654521

from datetime import timedelta
from ConsoleIO import Menu
from Truck import Truck
from HashTableDev import HashTableDev
from Packages import Package
from Address import Address

# Calls an instance of HashTableDev to store Packages
hash_table_of_packages = HashTableDev()

# Takes the CVS file path of supporting package data information and imports them into the hash table instance
Package.package_data_loading("WGUPS_CSV_DATA/WGUPS_Package_File_CSV.csv", hash_table_of_packages)

# Takes the CVS file path of address information and imports it to create an address list
daily_address_list = Address.address_data_load("WGUPS_CSV_DATA/WGUPS_Address_CSV.csv")

# Takes the CVS file path of distance information and imports it while creating a distance matrix
daily_distance_matrix = Address.address_data_loading("WGUPS_CSV_DATA/WGUPS_Distance_CSV.csv")

# Sets the starting times for the three shifts trucks are scheduled to depart from the hub
first_shift = (timedelta(hours=8, minutes=0))
second_shift = (timedelta(hours=9, minutes=6))
third_shift = (timedelta(hours=10, minutes=21))

# Creates an instance of truck for truck 1 and loads the assigned packages into the truck 1 instance
truck_1 = Truck(1, first_shift)
truck_1.truck_1_package_loading(1, hash_table_of_packages)

# Creates an instance of truck for truck 2 and loads the assigned packages into the truck 2 instance
truck_2 = Truck(2, second_shift,)
truck_2.truck_2_package_loading(2, hash_table_of_packages)
truck_2.load_delayed_packages(2, hash_table_of_packages)

# Creates an instance of truck for truck 3 and loads the assigned packages into the truck 3 instance
truck_3 = Truck(3, third_shift)
truck_3.truck_3_package_loading(3, hash_table_of_packages)

# Calls the deliver_packages method for truck 1/2/3 to deliver packages using the address list and distance matrix
Truck.deliver_packages(truck_1, daily_address_list, daily_distance_matrix)
Truck.deliver_packages(truck_2, daily_address_list, daily_distance_matrix)
Truck.deliver_packages(truck_3, daily_address_list, daily_distance_matrix)

# This is the application that runs the user interface and allows users to select options which call methods to report
# the desired selection until they decide to exit the application
while True:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - ")
    print("- - - - - - - - - - - Welcome To WGUPS Routing Program - - - - - - - - - - - ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - ")
    print("\nMain Menu\n")
    print("(1) : Track A Single Package At A Given Time")
    print("(2) : Track All Packages At A Given Time")
    print("(3) : Track All Packages & Total Mileage At End Of Day")
    print("(4) : Exit")

    user_select = input("\nEnter Menu Option (1-4): ")
    if user_select == "1":
        Menu.status_of_single_package_given_time(hash_table_of_packages)
    elif user_select == "2":
        Menu.status_of_all_packages_given_time(hash_table_of_packages)
    elif user_select == "3":
        Menu.total_truck_mileage(truck_1, truck_2, truck_3, hash_table_of_packages)
    elif user_select == "4":
        break
    input("\nPress Enter To Continue...\n")
