import csv


# Creates Package Class to store attributes for each packages information
class Package:
    def __init__(self, id_package, address_delivery, city_delivery, state_delivery, zip_code_delivery,
                 dead_line_delivery, weight_package, status_delivery, special_notes_delivery=None):
        self.id_package = id_package
        self.address_delivery = address_delivery
        self.city_delivery = city_delivery
        self.state_delivery = state_delivery
        self.zip_code_delivery = zip_code_delivery
        self.dead_line_delivery = dead_line_delivery
        self.weight_package = weight_package
        self.special_notes_delivery = special_notes_delivery
        self.package_status = status_delivery
        self.time_delivery = None
        self.time_loaded = None
        self.truck_number = None

    # Updates a package instance time once loaded attribute
    def update_time_loaded(self, time_loaded):
        self.time_loaded = time_loaded

    # Updates a package instance delivery time attribute
    def delivery_time_report(self, updated_time_delivery):
        self.time_delivery = updated_time_delivery

    # Updates a package instance status attribute
    def update_status(self, updated_status):
        self.package_status = updated_status

    # Updates a package instance address and zip code attribute
    def update_address(self, updated_address, update_zip_code):
        self.address_delivery = updated_address
        self.zip_code_delivery = update_zip_code

    # Updates a package instance status and delivery time to "En Route"
    def en_route_report(self):
        self.package_status = "En Route"
        self.time_delivery = "N/A"

    # Updates a package instance status and delivery time to "At Hub"
    def hub_report(self):
        self.package_status = "At Hub"
        self.time_delivery = "N/A"

    # Updates a package instance truck number attribute
    def assign_truck_number(self, truck_number):
        self.truck_number = truck_number

    # Method to look up a single package instance using the package ID in a hash table instance to print package data
    def package_look_up(self, package_id_value, input_hash_table):
        the_package = input_hash_table.package_search(package_id_value)

        if the_package:
            return (f"Package ID# - {self.id_package} | Address - {self.address_delivery}, {self.city_delivery}, "
                    f"{self.state_delivery} {self.zip_code_delivery} | Delivery DeadLine - {self.dead_line_delivery}"
                    f" | Weight (kg) - {self.weight_package} | Delivery Status - {self.package_status} | Truck Number "
                    f"{self.truck_number}")
        else:
            return f"Package with ID# {package_id_value} not found."

    # Static Method that loads, bundles and assigns CVS file data and inserts them into the hash table instance
    @staticmethod
    def package_data_loading(import_csv_package_path, import_hash_table):
        with open(import_csv_package_path, encoding='utf-8-sig') as wgups_package_csv:
            package_data = csv.reader(wgups_package_csv)
            for data in range(8):
                next(package_data)
            for data in package_data:
                id_package = int(data[0])
                address_delivery = data[1]
                city_delivery = data[2]
                state_delivery = data[3]
                zip_code_delivery = data[4]
                dead_line_delivery = data[5]
                weight_package = data[6]
                note_delivery = data[7]
                status_delivery = 'At The hub'
                packaged_data = Package(id_package, address_delivery, city_delivery, state_delivery,
                                        zip_code_delivery, dead_line_delivery, weight_package, status_delivery,
                                        note_delivery)

                import_hash_table.insertion_key_value(package_id_input=id_package, packaged_data_input=packaged_data)
