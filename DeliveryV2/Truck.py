from Address import Address
from datetime import timedelta

# Creates a Truck Class to store attributes for each truck instance
class Truck:
    def __init__(self, truck_number, route_start_time):
        self.truck_number = truck_number
        self.truck_mph = 18
        self.truck_mileage = 0
        self.truck_location_status = '4001 South 700 East'
        self.truck_route_start_time = route_start_time
        self.truck_present_time = route_start_time
        self.truck_total_packages = []
        self.truck_remaining_packages = []
        self.truck_hub = '4001 South 700 East'

    # Method to add a package to a truck instance for total packages and remaining packages attributes
    def truck_add_packages(self, add_package_data):
        self.truck_total_packages.append(add_package_data)
        self.truck_remaining_packages.append(add_package_data)

    # Method to remove a package from a truck instances remaining packages attribute list
    def truck_remove_packages(self, remove_package_data):
        self.truck_remaining_packages.remove(remove_package_data)

    # Method to update a truck instance present time attribute
    def truck_update_time(self, checkin_time):
        self.truck_present_time = checkin_time

    # Method to update a truck instance present time(conversion/addition), location, and mileage(addition) attributes
    def truck_update_info(self, updated_present_time, updated_location_status, updated_mileage):
        hours = updated_present_time.seconds // 3600
        minutes = (updated_present_time.seconds % 3600) // 60
        self.truck_present_time += timedelta(hours=hours, minutes=minutes)
        self.truck_location_status = updated_location_status
        self.truck_mileage += updated_mileage

    # Method to load packages from hash table instance and assign truck number and add package to truck 1 instance
    def truck_1_package_loading(self, truck_number,  package_hash_table):
        load_package_que = [1, 13, 14, 15, 16, 19, 20, 29, 30, 33, 34, 35, 37, 39, 40]
        for package_id in load_package_que:
            package_to_add = package_hash_table.package_search(package_id)
            if package_to_add is not None:
                package_to_add.assign_truck_number(truck_number)
                self.truck_add_packages(package_to_add)
            else:
                print(f"Package with ID {package_id} was unable to load.")

    # Method to load packages from hash table instance and assign truck number and add package to truck 2 instance
    def truck_2_package_loading(self, truck_number, package_hash_table):
        load_package_que = [3, 18, 31, 36, 38]
        for package_id in load_package_que:
            package_to_add = package_hash_table.package_search(package_id)
            if package_to_add is not None:
                package_to_add.assign_truck_number(truck_number)
                self.truck_add_packages(package_to_add)
            else:
                print(f"Package with ID {package_id} was unable to load.")

    # Method to load packages from hash table instance and assign truck number and add delayed packages to truck 2
    def load_delayed_packages(self, truck_number, package_hash_table):
        load_package_que = [6, 25,  28, 32]
        for package_id in load_package_que:
            package_to_add = package_hash_table.package_search(package_id)
            if package_to_add is not None:
                package_to_add.assign_truck_number(truck_number)
                self.truck_add_packages(package_to_add)
            else:
                print(f"Package with ID {package_id} was unable to load.")

    # Method to load packages from hash table instance and assign truck number and add package to truck 3 instance
    def truck_3_package_loading(self, truck_number, package_hash_table):
        load_package_que = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]
        for package_id in load_package_que:
            package_to_add = package_hash_table.package_search(package_id)
            if package_to_add is not None:
                package_to_add.assign_truck_number(truck_number)
                self.truck_add_packages(package_to_add)
            else:
                print(f"Package with ID {package_id} was unable to load.")

    # Static Method to Deliver Packages for each truck instance using Nearest Neighbor Algorithm Theory
    @staticmethod
    def deliver_packages(delivery_truck, daily_address_list, daily_distance_matrix):
        while delivery_truck.truck_remaining_packages:
            nearest_distance = 71
            nearest_package = None
            # Iterates over packages in truck instance remaining packages and compares distances to find next package
            for package in delivery_truck.truck_remaining_packages:
                distance = Address.distance_between(daily_address_list, daily_distance_matrix,
                                                    delivery_truck.truck_location_status, package.address_delivery)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_package = package

            # Updates truck instance time traveled /location/distance attributes
            time_traveled = nearest_distance / delivery_truck.truck_mph
            delivery_truck.truck_update_info(timedelta(hours=time_traveled), nearest_package.address_delivery,
                                             nearest_distance)
            nearest_package.delivery_time_report(delivery_truck.truck_present_time)
            delivery_truck.truck_remove_packages(nearest_package)

        # Once all packages have been delivered, directs truck instance to return to hub and update attributes
        distance_to_hub = Address.distance_between(daily_address_list, daily_distance_matrix,
                                                   delivery_truck.truck_location_status, delivery_truck.truck_hub)
        time_traveled = distance_to_hub / delivery_truck.truck_mph
        delivery_truck.truck_update_info(timedelta(hours=time_traveled), delivery_truck.truck_hub, distance_to_hub)

    # Method to print truck instance information for Truck Number/Start Time/Present Time/Location/Mileage/Package Lists
    def truck_timed_checkin(self, checkin_time):
        self.truck_update_time(checkin_time)
        loaded_package_ids = [str(package.id_package) for package in self.truck_total_packages]
        loaded_packages_str = ", ".join(loaded_package_ids)
        remaining_package_ids = [str(package.id_package) for package in self.truck_remaining_packages]
        remaining_packages_str = ", ".join(remaining_package_ids)
        return f'''
        Truck Status Information
        Truck Number - {self.truck_number}
        Truck Start Time - {self.truck_present_time}
        Present Time  - {self.truck_present_time} 
        Truck Location - {self.truck_location_status}
        Truck Mileage - {self.truck_mileage}
        Total Loaded Packages - {loaded_packages_str}
        Remaining Loaded Packages - {remaining_packages_str}
        '''
