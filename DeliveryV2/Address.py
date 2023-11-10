import csv


# Creates an Address class to compare and input address and distance data
class Address:

    # Static Method that takes a CVS file and returns address data from the file
    @staticmethod
    def address_data_load(input_cvs_file_path):
        with open(input_cvs_file_path, encoding='utf-8-sig') as address_cvs_file:
            read_csv = csv.reader(address_cvs_file)
            loaded_address_data = [row_value[1] for row_value in read_csv]
        return loaded_address_data

    # Static Method that imports CVS address distance data and creates a matrix while creating the reciprocal values
    @staticmethod
    def address_data_loading(import_csv_address_path):
        with open(import_csv_address_path, encoding='utf-8-sig') as address_cvs_file:
            total_address = sum(1 for row in address_cvs_file)

        distance_matrix = []
        for index_1 in range(total_address):
            row = []
            for index_2 in range(total_address):
                row.append(0)
            distance_matrix.append(row)

        # Iterates through missing cells in the matrix and inputs the reciprocal values
        with open(import_csv_address_path, encoding='utf-8-sig') as address_cvs_file:
            csv_reader = csv.reader(address_cvs_file, delimiter=',')
            for index_1, row in enumerate(csv_reader):
                for index_2, missing_data in enumerate(row):
                    if missing_data:
                        distance_matrix[index_1][index_2] = float(missing_data)
                        distance_matrix[index_2][index_1] = float(missing_data)
        return distance_matrix

    # Static Method that compares the distance between two given addresses and returns the distance matrix value
    @staticmethod
    def distance_between(address_list, distance_matrix, start_address, end_address):
        index1 = address_list.index(start_address)
        index2 = address_list.index(end_address)
        return distance_matrix[index1][index2]
