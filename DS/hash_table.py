class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % self.MAX

    def print(self):
        print(self.arr)

    def __setitem__(self, key, value):
        hashed = self.get_hash(key=key)
        found = False
        for idx, elem in enumerate(self.arr[hashed]):
            if (len(elem) == 2) and (elem[0] == key):
                self.arr[hashed][idx] = (key, value)
                found = True

        if not found:
            self.arr[hashed].append((key, value))

    def __getitem__(self, key):
        hashed = self.get_hash(key=key)
        for pair in self.arr[hashed]:
            if pair[0] == key:
                return pair[1]

    def __delitem__(self, key):
        hashed = self.get_hash(key=key)
        for idx, pair in enumerate(self.arr[hashed]):
            if pair[0] == key:
                del self.arr[hashed][idx]
                return
