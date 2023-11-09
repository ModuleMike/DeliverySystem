class HashTableDev:
    def __init__(self):
        self.dev_table_size = 40
        self.dev_hash_table = []
        for _ in range(self.dev_table_size):
            self.dev_hash_table.append([])

    def __iter__(self):
        for package_list in self.dev_hash_table:
            for package_key_value in package_list:
                yield package_key_value[1]

    def developed_hash_table_key(self, package_key_value):
        return package_key_value % self.dev_table_size

    def insertion_key_value(self, package_id_input, packaged_data_input):
        inserted_key_value = self.developed_hash_table_key(package_id_input)
        package_list = self.dev_hash_table[inserted_key_value]
        for package_index in range(len(package_list)):
            ref_key, _ = package_list[package_index]
            if ref_key == package_id_input:
                package_list[package_index] = (package_id_input, packaged_data_input)
                return True
        # Insert a new key-value pair
        package_list.append((package_id_input, packaged_data_input))
        return True

    def package_search(self, package_key):
        package_hash_bucket = hash(package_key) % len(self.dev_hash_table)
        package_hash_bucket_list = self.dev_hash_table[package_hash_bucket]
        # search key in bucket
        for package_key_value in package_hash_bucket_list:
            if package_key_value[0] == package_key:
                return package_key_value[1]  # Return the package data (second element)

        return None

    def package_remove(self, key):
        package_hash_bucket = hash(key) % len(self.dev_hash_table)
        package_hash_bucket_list = self.dev_hash_table[package_hash_bucket]
        if key in package_hash_bucket_list:
            package_hash_bucket_list.remove(key)
