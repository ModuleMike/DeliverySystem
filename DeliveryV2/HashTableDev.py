# Creates hash table dev class to store the hash table instance and attributes
class HashTableDev:
    def __init__(self):
        self.dev_table_size = 40
        self.dev_hash_table = []
        for _ in range(self.dev_table_size):
            self.dev_hash_table.append([])

    # Creates an iterable path to the hash table
    def __iter__(self):
        for package_list in self.dev_hash_table:
            for package_key_value in package_list:
                yield package_key_value[1]

    # Method to determine a hash table key based off of a package key value input
    def developed_hash_table_key(self, package_key_value):
        return package_key_value % self.dev_table_size

    # Method to insert a value into the hash table and assign its paired key
    def insertion_key_value(self, package_id_input, packaged_data_input):
        inserted_key_value = self.developed_hash_table_key(package_id_input)
        package_list = self.dev_hash_table[inserted_key_value]
        for package_index in range(len(package_list)):
            ref_key, _ = package_list[package_index]
            if ref_key == package_id_input:
                package_list[package_index] = (package_id_input, packaged_data_input)
                return True
        package_list.append((package_id_input, packaged_data_input))
        return True

    # Method to search a hash table instance by key value input and return its value pair
    def package_search(self, package_key):
        package_hash_bucket = hash(package_key) % len(self.dev_hash_table)
        package_hash_bucket_list = self.dev_hash_table[package_hash_bucket]
        for package_key_value in package_hash_bucket_list:
            if package_key_value[0] == package_key:
                return package_key_value[1]

        return None

    # Method to remove a key from the hash table
    def package_remove(self, key):
        package_hash_bucket = hash(key) % len(self.dev_hash_table)
        package_hash_bucket_list = self.dev_hash_table[package_hash_bucket]
        if key in package_hash_bucket_list:
            package_hash_bucket_list.remove(key)
