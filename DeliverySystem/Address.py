import csv

class Address:
    # ******************** EDIT THIS ************************************************
    @staticmethod
    def address_data_load(input_cvs_file_path):
        with open(input_cvs_file_path, encoding='utf-8-sig') as address_value:
            read_csv = csv.reader(address_value)
            loaded_address = [row_value[1] for row_value in read_csv]
        return loaded_address

    # ******************** EDIT THIS ************************************************

    # ******************** EDIT THIS ************************************************
    @staticmethod
    def address_data_loading(import_csv_address_path):
        with open(import_csv_address_path, encoding='utf-8-sig') as file:
            num_addresses = sum(1 for row in file)

        distance_matrix = []
        for i in range(num_addresses):
            row = []
            for j in range(num_addresses):
                row.append(0)
            distance_matrix.append(row)
        # Create a zero-filled matrix of the right size
        #distance_matrix = [[0] * num_addresses for _ in range(num_addresses)]

        # Fill the matrix with actual distances (making the triangle a square)
        with open(import_csv_address_path, encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for i, row in enumerate(csv_reader):
                for j, value in enumerate(row):
                    if value:  # Only convert non-empty strings
                        distance_matrix[i][j] = float(value)
                        distance_matrix[j][i] = float(value)
        return distance_matrix

# ******************** EDIT THIS ************************************************
    @staticmethod
    def distance_between(from_address, to_address, addresses, distances):
        # Get the indices of the two addresses
        index1 = addresses.index(from_address)
        index2 = addresses.index(to_address)
        # Return the distance between them
        return distances[index1][index2]
# ******************** EDIT THIS ************************************************
