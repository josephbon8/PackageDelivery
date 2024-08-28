class hashtable:
    def __init__(self):
        self.size = 16
        self.map = [None] * self.size

    def _get_hash(self, key):
       return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
    def get_package_attributes_by_id(self, package_id):
        index=self._get_hash(package_id)
        if self.map[index] is not None:
            for package in self.map[index]:
                    #if package.ids== package_id:
                packObj=package[1]
                return (f" Address: {packObj.address}, Deadline: {packObj.deadline}, City: {packObj.city}, Zipcode: {packObj.zipcode}, Weight: {packObj.weight}, Status: {packObj.status}")

    def get_package_address_by_id(self, package_id):
        index = self._get_hash(package_id)
        if self.map[index] is not None:
            for package in self.map[index]:
                # if package.ids== package_id:
                packObj = package[1]
                return packObj.address

    def get_package_by_id(self, package_id):
        index=self._get_hash(package_id)
        if self.map[index] is not None:
            for package in self.map[index]:
                    if package[0] == package_id:
                         packObj=package[1]
                         return packObj
        return None

    def print(self):
        print("----Packages----")
        for index, bucket in enumerate(self.map):
            if bucket is not None:
                for key, package in bucket:
                    print(f"Package ID: {package.ids}, Package City: {package.city}, Package Weight: {package.weight}")