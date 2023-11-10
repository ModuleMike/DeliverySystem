from datetime import timedelta


# Creates Menu class to produce the outputs for the user interface
class Menu:

    # Static Method that shows the information of all packages and requests a user to input a time to check for
    @staticmethod
    def status_of_all_packages_given_time(the_hash_table, requested_time=None):
        if requested_time is None:
            requested_time = Menu.time_input_checker("Enter A Time To Check On All Trucks (hh:mm): ")
        for key_index in range(1, 41):
            Menu.package_report(key_index, requested_time, the_hash_table)

    # Static Method to show a single package information and requests a package ID # and input time to check for
    @staticmethod
    def status_of_single_package_given_time(the_hash_table):
        package_key = Menu.get_valid_number("Enter A Package ID # (1-40): ", 40)
        requested_time = Menu.time_input_checker("Enter A Time To Check (hh:mm): ")
        Menu.package_report(package_key, requested_time, the_hash_table)

    # Static Method to show all package information at EOD and total mileage for trucks 1/2/3
    @staticmethod
    def total_truck_mileage(truck_1, truck_2, truck_3, the_hash_table):
        print("\nStatus Of All Deliveries At End of Day\n")
        Menu.status_of_all_packages_given_time(the_hash_table, timedelta(hours=12, minutes=45))
        total_mileage = truck_1.truck_mileage + truck_2.truck_mileage + truck_3.truck_mileage
        print(f"\nTotal Truck Mileage For Truck 1, 2 & 3 - {total_mileage} Miles")

    # Static Method that checks a users input to see if it is in hh:mm format and if not prompts to re-enter a time
    @staticmethod
    def time_input_checker(prompt):
        while True:
            check_time_input = input(prompt)
            try:
                input_time_parts = check_time_input.split(":")
                if len(input_time_parts) != 2:
                    raise ValueError  # If there are not exactly two parts separated by ':', raise ValueError
                input_hours = int(input_time_parts[0])
                input_minutes = int(input_time_parts[1])
                if 0 <= input_hours < 24 and 0 <= input_minutes < 60:
                    return timedelta(hours=input_hours, minutes=input_minutes)
                else:
                    raise ValueError  # If hours or minutes are out of range, raise ValueError
            except ValueError:
                Menu.invalid()

    # Static Method to check if a user input is ia valid integer within the range and if not prompts for another number
    @staticmethod
    def get_valid_number(prompt, max_number):
        while True:
            try:
                user_input = input(prompt)
                if 0 < int(user_input) < max_number:
                    number = int(user_input)
                    return number
                else:
                    raise ValueError
            except ValueError:
                Menu.invalid()

    # Static Method to format time into hh:mm
    @staticmethod
    def format_time(time_input):
        output_time = str(time_input).split(':')[:2]
        output_time = ':'.join(output_time)
        return output_time

    # Static Method that returns a message for an invalid input
    @staticmethod
    def invalid():
        return "Invalid option. Please enter a number in the range."

    # Static Method to report package info and compares it to inputted time providing the correct status/print out
    @staticmethod
    def package_report(package_id, time_requested, the_hash_table):
        check_package = the_hash_table.package_search(package_id)
        second_shift = timedelta(hours=9, minutes=6)
        third_shift = timedelta(hours=10, minutes=21)
        second_shift_packages = (3, 6, 18, 25, 28, 31, 32, 36, 38)
        third_shift_packages = (8, 9, 10, 11, 23, 12, 17, 22, 24)
        update_address = timedelta(hours=10, minutes=20)

        if package_id == 9 and time_requested < update_address:
            check_package.update_address("300 State St", "84103")
        elif package_id == 9 and time_requested > update_address:
            check_package.update_address("410 S State St", "84111")

        if ((check_package.time_delivery is None) or
                (package_id in second_shift_packages and time_requested < second_shift) or
                (package_id in third_shift_packages and time_requested < third_shift)):
            check_package.update_status("At The Hub")
            print(f"{check_package.package_look_up(package_id, the_hash_table)} | Deliver Time - N/A")
        elif check_package.time_delivery > time_requested:
            check_package.update_status("En Route")
            print(f"{check_package.package_look_up(package_id, the_hash_table)} | Deliver Time - N/A")
        else:
            check_package.update_status("Delivered")
            print(f"{check_package.package_look_up(package_id, the_hash_table)} | Deliver Time - "
                  f"{Menu.format_time(check_package.time_delivery)}")

    # Static Method to check truck package information based on a users requested time of check in
    @staticmethod
    def truck_report(the_hash_table):
        requested_time = Menu.time_input_checker("Enter A Time To Check On All Trucks (hh:mm): ")
        truck_one = (1, 13, 14, 15, 16, 19, 20, 29, 30, 33, 34, 35, 37, 39, 40)
        truck_two = (3, 6, 18, 25, 28, 31, 32, 36, 38)
        truck_three = (8, 9, 10, 11, 23, 12, 17, 22, 24)

        for key_index in truck_one:
            Menu.package_report(key_index, requested_time, the_hash_table)

        for key_index in truck_two:
            Menu.package_report(key_index, requested_time, the_hash_table)

        for key_index in truck_three:
            Menu.package_report(key_index, requested_time, the_hash_table)
