class HashTable:
    MAX_PER_LIST = 5

    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_func(self, key):
        return key % self.size

    def insert(self, element):
        key = self.hash_func(element)
        self.data[key].append(element)
        self.num_elements += 1

        # Rozszerzenie tablicy w razie potrzeby
        if self.num_elements > self.size * self.MAX_PER_LIST:
            self._resize(2 * self.size)

    def delete(self, element):
        key = self.hash_func(element)
        if element in self.data[key]:
            for i, el in enumerate(self.data[key]):
                if el == element:
                    del self.data[key][i]
                    self.num_elements -= 1
                    break  # Przerwij pętlę po usunięciu pierwszego elementu

        # Zmniejszenie tablicy w razie potrzeby
            if self.size > 1 and 4 * self.num_elements < self.size * self.MAX_PER_LIST:
                self._resize(self.size // 2)



    def find(self, element):
        key = self.hash_func(element)
        return element in self.data[key]

    def _resize(self, new_size):
        new_data = [[] for _ in range(new_size)]
        for sublist in self.data:
            for element in sublist:
                new_key = self.hash_func(element)
                if new_key < new_size:
                    new_data[new_key].append(element)
        self.data = new_data
        self.size = new_size


# Przykład użycia
hash_table = HashTable(10)

hash_table.insert(24)
hash_table.insert(121)
hash_table.insert(119)
hash_table.insert(52)
hash_table.insert(87)
hash_table.insert(166)
hash_table.insert(2)
hash_table.insert(103)
hash_table.insert(9)
hash_table.insert(54)
hash_table.insert(115)
hash_table.insert(85)
hash_table.insert(187)
hash_table.insert(34)
hash_table.insert(198)
hash_table.insert(72)
hash_table.insert(139)
hash_table.insert(6)
hash_table.insert(141)
hash_table.insert(42)
hash_table.insert(101)
hash_table.insert(178)
hash_table.insert(68)
hash_table.insert(32)
hash_table.insert(183)
hash_table.insert(79)
hash_table.insert(157)
hash_table.insert(95)
hash_table.insert(12)
hash_table.insert(63)
hash_table.insert(149)
hash_table.insert(160)
hash_table.insert(44)
hash_table.insert(125)
hash_table.insert(23)
hash_table.insert(171)
hash_table.insert(56)
hash_table.insert(192)
hash_table.insert(107)
hash_table.insert(76)
hash_table.insert(133)
hash_table.insert(4)
hash_table.insert(114)
hash_table.insert(27)
hash_table.insert(195)
hash_table.insert(92)
hash_table.insert(38)
hash_table.insert(158)
hash_table.insert(71)
hash_table.insert(147)

print(hash_table.data)

print(hash_table.find(139))
print(hash_table.find(79))
hash_table.delete(139)
hash_table.delete(79)
print(hash_table.data)
print(hash_table.find(139))
print(hash_table.find(79))



