class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        return sum([ord(c) for c in key]) % self.size

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for pair in self.data[hash]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f'\'{key}\' not found')

    def set(self, key, value):
        hash = self._hash(key)

        key_value = [key, value]

        if self.data[hash]:
            for pair in self.data[hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.data[hash].append(key_value)
            return True
        else:
            self.data[hash] = [key_value]
            return True

    def remove(self, key):
        hash = self._hash(key)

        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    self.data[hash].pop(i)
                    if len(self.data[hash]) == 0:
                        self.data[hash] = None
                    return True
        raise KeyError(f'\'{key}\' not found')


if __name__ == '__main__':
    pass
