from datetime import timedelta
from ConsoleIO import Menu
from Truck import Truck
from HashTableDev import HashTableDev
from Packages import Package
from Address import Address


hash_table_of_packages = HashTableDev()
Package.package_data_loading("WGUPS_CSV_DATA/WGUPS_Package_File_CSV.csv", hash_table_of_packages)
daily_address_list = Address.address_data_load("WGUPS_CSV_DATA/WGUPS_Address_CSV.csv")
daily_distance_matrix = Address.address_data_loading("WGUPS_CSV_DATA/WGUPS_Distance_CSV.csv")

first_shift = (timedelta(hours=8, minutes=0))
second_shift = (timedelta(hours=9, minutes=6))
third_shift = (timedelta(hours=10, minutes=21))

truck_1 = Truck(1, first_shift)
truck_1.truck_1_package_loading(hash_table_of_packages)


truck_2 = Truck(2, second_shift,)
truck_2.truck_2_package_loading(hash_table_of_packages)
truck_2.load_delayed_packages(hash_table_of_packages)

truck_3 = Truck(3, third_shift)
truck_3.truck_3_package_loading(hash_table_of_packages)

Truck.deliver_packages(truck_1, daily_address_list, daily_distance_matrix)
Truck.deliver_packages(truck_2, daily_address_list, daily_distance_matrix)
Truck.deliver_packages(truck_3, daily_address_list, daily_distance_matrix)

while True:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - ")
    print("- - - - - - - - - - - Welcome To WGUPS Routing Program - - - - - - - - - - - ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - ")
    print("\nMain Menu\n")
    print("(1) : Track A Single Package At A Given Time")
    print("(2) : Track All Packages At A Given Time")
    print("(3) : Check All Trucks Packages At A Given Time")
    print("(4) : Check All Trucks Total Mileage")
    print("(5) : Exit")

    user_select = input("\nEnter Menu Option (1-5): ")
    if user_select == "1":
        Menu.status_of_single_package_given_time(hash_table_of_packages)
    elif user_select == "2":
        Menu.status_of_all_packages_given_time(hash_table_of_packages)
    elif user_select == "3":
        truck_checkin_time = Menu.time_input_checker("Enter A Time To Check On All Trucks (hh:mm): ")
        print(f"{truck_1.truck_timed_checkin(truck_checkin_time)}\n{truck_2.truck_timed_checkin(truck_checkin_time)}\n"
              f"{truck_3.truck_timed_checkin(truck_checkin_time)}")
    elif user_select == "4":
        Menu.total_truck_mileage(truck_1, truck_2, truck_3)
    elif user_select == "5":
        break
    input("\nPress Enter To Continue...\n")
