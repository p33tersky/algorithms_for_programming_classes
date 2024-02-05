# Należy zaimplementować dwa algorytmy wyszukiwania wzorca w tekście: naiwny oraz Sunday’a.
# Dodatkowo należy opanować (ze zrozumieniem) teorię dotyczącą tych algorytmów (zasady działania, złożoności obliczeniowe czasowe i pamięciowe).

# Dane do wykresu przedstawiającego zależność od |W| można spreparować następującym algorytmem:
# Używając alfabetu A (np. A={a, …, z}), wylosuj wzorzec W o zadanej długości (np. 5 znaków).
# Utwórz pusty tekst T.
# Dodaj na koniec T jeden znak wylosowany z A.
# Zmierz liczbę porównań znaków wykonanych przy wyszukiwaniu wszystkich wystąpień W w T przez algorytm naiwny.
#   Zapisz długość T (x=|T|) oraz zmierzoną liczbę porównań (y). 
#   Te dwie liczby (x, y) stanowią pojedynczy punkt do wykresu dla algorytmu naiwnego.
#   To samo wykonaj dla algorytmu Sunday’a i innych (jeśli zaimplementowano) 
#   by otrzymać po jednym punkcie pomiarowym dla każdego z tych algorytmów.
# Wrócić do punktu 3, chyba że tekst T jest zbyt długi (np. |T| > 10000).

import string
import random 
import matplotlib.pyplot as plt
import string
import random 
import matplotlib.pyplot as plt

naiveCounter = 0
def naiveCount():
    global naiveCounter
    naiveCounter+=1

sundayCounter = 0
def sundayCount():
    global sundayCounter
    sundayCounter+=1

def matches_at(T, p, W, isNaive):
    for i in range(len(W)):
        if isNaive:
            naiveCount()
        else:
            sundayCount()
        if W[i] != T[p+i]:
            return False
    return True


def naiveAlg(T,W):
    for p in range(len(T)-len(W)+1):
        matches_at(T,p,W, True)
        
def signsDict(W):
    lastp = dict()
    for i, char in enumerate(W):
        lastp[char] = i
    return lastp
    

def sundayAlg(T,W):
    p=0
    lasZsDict = signsDict(W)
    while p < len(T)-len(W)+1:
        matches_at(T,p,W,False)
        if p+len(W) < len(T):
            z = T[p+len(W)]
            lastZInW = lasZsDict.get(z,-1)
            if lastZInW == -1:
                p+=len(W)+1
            else:
                p+=len(W)-lastZInW
        else: break

A = list(string.ascii_lowercase)
W = 'akcja'
T = ''
for j in range(len(W)):
        T+=random.choice(A)

Xn = []
Yn = []
Xs = []
Ys = []

for i in range(1000):
    naiveAlg(T,W)
    sundayAlg(T,W)
    Xn.append(len(T))
    Yn.append(naiveCounter)
    Xs.append(len(T))
    Ys.append(sundayCounter)
    naiveCounter = 0
    sundayCounter = 0
    T+=random.choice(A)

plt.plot(Xn, Yn)
plt.plot(Xs,Ys)
plt.show()



       


 




