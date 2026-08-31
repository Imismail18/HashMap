"""
Structure of comments:
Function description.
Time complexity O()
"""

class HashMap:
    # Initializes an empty hash map with specified capacity and bucket array.
    # Time Complexity: O(capacity)
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # Returns the number of key-value pairs currently in the hash map.
    # Time Complexity: O(1)
    def __len__(self):
        return self.size

    # Checks if a key exists in the hash map. Returns True if key exists, False otherwise.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def __contains__(self, item):
        index = self._hash_function(item)
        bucket = self.buckets[index]

        
        return any(k == item or v == item for k, v in bucket)

    # Returns a string representation of the hash map showing all key-value pairs.
    # Time Complexity: O(n) - where n is the total number of entries
    def __repr__(self):
        return str(self.items())

    # Inserts or updates a key-value pair in the hash map.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else: 
            bucket.append((key, value))  
            self.size += 1

    # Retrieves the value associated with a key. Raises KeyError if key not found.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key: return v
        raise KeyError("Key not found!")

    # Removes a key-value pair from the hash map. Raises KeyError if key not found.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break

        else:
            raise KeyError("Key not found!")

    # Returns a list of all keys in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # Returns a list of all values in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # Returns a list of all key-value pairs (tuples) in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # Computes the hash value for a given key to determine bucket index.
    # Time Complexity: O(k) - where k is the length of the key string
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = ((hash_result * 31) + ord(c)) % self.capacity
        return hash_result

    # Searches for one or multiple keys in the hash map.
    # Time Complexity: O(n) - where n is the number of keys to search
    def search(self, *keys):
        if not keys: return False
        
        results = {}
        results = {key: key in self for key in keys}
        
        return results if len(keys) > 1 else results[keys[0]]

    #Checks if the hash map is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self):
        return self.size == 0

    




if __name__ == "__main__":
    import uuid
    import matplotlib.pyplot as plt

    HM = HashMap(100)

    for _ in range(5000):
        HM.put(uuid.uuid4(), "some_value")

    x =[]
    y = []

    for i, bucket in enumerate(HM.buckets):
        x.append(i)
        y.append(len(bucket))

    plt.bar(x, y)
    plt.show()

    HM.put("name", ["Ismail", "Ishaq", "Mohmed", "Farida"])
    HM.put("age", [20, 19, 70, 55])
    HM.put("email", ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"])
    HM.put("degree", ["CyberSecurty", "null", "null", "null"])
    HM.put("ID", [155715, 155716, 155717, 155718])

    print(len(HM))
    print("Ismail" in HM)
    print(HM)
    print(HM.get("ID"))

    HM.remove("ID")

    print(HM.keys())
    print(HM.values())
    print(HM.items())
    print(HM.search("name", "age", "degree"))
    print(HM.is_empty())

    print(HM.buckets)

