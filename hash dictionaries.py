'''Projekt slowniki'''


class MetodaLancuchowa:
    '''Słownik z metoda tablicy list'''

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        'Funkcja hashowania'
        return hash(key) % self.size  # zapewnia index w granicach tablicy

    def insert(self, key):
        'Funkcja wstawienia'
        index = self.hash_function(key)
        for entry in self.table[index]:
            if entry == key:
                return
        self.table[index].append(key)

    def find(self, key):
        '''Funkcja znalezienia elementu'''
        index = self.hash_function(key)
        for entry in self.table[index]:
            if entry == key:
                return index
        # Klucz nie istnieje
        return None

    def delete(self, key):
        '''Funkcja usuwania elementu'''
        index = self.hash_function(key)
        for _ in self.table[index]:
            if _ == key:
                self.table[index].remove(key)
                return
        raise KeyError(f"Klucz '{key}' nieznaleziony.")
    
    def get_content(self):
        return self.table


class SlownikLiniowy:
    '''Slownik z metoda adresowania liniowego'''

    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        '''Funkcja hashowanie'''
        return hash(key) % self.size

    def insert(self, key):
        '''Funkcja wstawiajaca'''
        if self.count == self.size:
            raise ValueError("Tabela jest pełna.")

        index = self.hash_function(key)

        while self.table[index] is not None and self.table[index] != "deleted":
            if self.table[index] == key:
                return
            index = (index + 1) % self.size

        self.table[index] = key
        self.count += 1

    def find(self, key):
        '''Funkcja szukajaca'''
        index = self.hash_function(key)
        # Zapisujemy oryginalny indeks dla warunku zakończenia przeszukiwania
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return F'Key {key} found on index {index}'
            index = (index + 1) % self.size

            # Dodajemy warunek zakończenia przeszukiwania, aby uniknąć nieskończonej pętli
            if index == original_index:
                print("Klucza nie znaleziono")
                break

        return None

    def delete(self, key):
        '''Funkcja usuwanie'''
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = "deleted"
                self.count -= 1
                return
            index = (index + 1) % self.size

        raise KeyError(f"Klucz '{key}' nieznaleziony.")


# Przykład użycia slownika liniowego
slownik_liniowy = SlownikLiniowy(size=10)

slownik_liniowy.insert(10)
slownik_liniowy.insert(67)
slownik_liniowy.insert(43)
slownik_liniowy.insert(27)
slownik_liniowy.insert(18)
slownik_liniowy.insert(58)
slownik_liniowy.insert(59)
slownik_liniowy.insert(60)
slownik_liniowy.insert(61)
slownik_liniowy.insert(62)
# slownik_liniowy.insert(999) #Tabela jest pełna

print("Slownik liniowy:", slownik_liniowy.table)
print("Find '59':", slownik_liniowy.find(59))
# print("Find '4':", slownik_liniowy.find(4))  # Spowoduje KeyError


slownik_liniowy.delete(10)

print("HashTable:", slownik_liniowy.table)

slownik_liniowy.insert(15)
# slownik_liniowy.insert(10)

print("HashTable:", slownik_liniowy.table)
print('Slownik liniowy szukanie:', slownik_liniowy.find(1))
# problem szukania polega na tym ze w przypadku pelnej tablicy slownik szuka w nieskonczonosc

# Przykład metoda lancuchowa
###############################################################################################
# slownik_lancuchowy = MetodaLancuchowa(size=10)

# slownik_lancuchowy.insert(5)
# slownik_lancuchowy.insert(1)
# slownik_lancuchowy.insert(13)
# slownik_lancuchowy.insert(43)
# slownik_lancuchowy.insert(47)
# slownik_lancuchowy.insert(57)
# slownik_lancuchowy.insert(67)
# slownik_lancuchowy.insert(177)


# print(slownik_lancuchowy.get_content())
# print("Wartość dla klucza 1:", slownik_lancuchowy.find(1))
# print("Wartość dla klucza 13:", slownik_lancuchowy.find(13))
# print("Wartość dla klucza 43:", slownik_lancuchowy.find(43))
# print("Wartość dla klucza 67:", slownik_lancuchowy.find(67))
# print("Wartość dla klucza 16:", slownik_lancuchowy.find(16))

# print("Usuwam 13")
# slownik_lancuchowy.delete(13)
# print("Wartość dla 13 po usunięciu:", slownik_lancuchowy.find(13))
# print(slownik_lancuchowy.get_content())
# slownik_lancuchowy.delete(13) #KeyError

