class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        hash_index = self._hash(key)
        for item in self.map[hash_index]:
            if item[0] == key:
                item[1] = value
                return
        self.map[hash_index].append([key, value])
    
    def get(self, key):
        hash_index = self._hash(key)
        for item in self.map[hash_index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)
    
    def delete(self, key):
        hash_index = self._hash(key)
        for i, item in enumerate(self.map[hash_index]):
            if item[0] == key:
                del self.map[hash_index][i]
                return
        raise KeyError(key)

# Usage example
my_map = HashMap()
my_map.put("name", "Alice")
my_map.put("age", 30)
print(my_map.get("name"))  # Output: Alice
my_map.delete("age")
try:
    my_map.get("age")
except KeyError:
    print("Age not found")  # This will be printed