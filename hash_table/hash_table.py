class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))
        return index

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        return None

    def __str__(self):
        return str(self.table)
