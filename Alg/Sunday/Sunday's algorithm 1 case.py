# Należy zaimplementować dwa algorytmy wyszukiwania wzorca w tekście: naiwny oraz Sunday’a.
# Dodatkowo należy opanować (ze zrozumieniem) teorię dotyczącą tych algorytmów (zasady działania, złożoności obliczeniowe czasowe i pamięciowe).

# Dane do wykresu przedstawiającego zależność od |W| można spreparować następującym algorytmem:
# Używając alfabetu A (np. A={a, …, z}), wylosuj tekst T o zadanej długości (np. 10000 znaków).
# Utwórz pusty wzorzec W.
# Dodaj na koniec W jeden znak wylosowany z A.
# Zmierz liczbę porównań znaków wykonanych przy wyszukiwaniu wszystkich wystąpień W w T przez algorytm naiwny. 
#   Zapisz długość W (x=|W|) oraz zmierzoną liczbę porównań (y). 
#   Te dwie liczby (x, y) stanowią pojedynczy punkt do wykresu dla algorytmu naiwnego. 
#   To samo wykonaj dla algorytmu Sunday’a i innych (jeśli zaimplementowano) by otrzymać po jednym punkcie pomiarowym
# dla każdego z tych algorytmów.
# Wrócić do punktu 3, chyba że wzorzec W jest zbyt długi (np. |W| > 40).

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
        


def sundayAlg(T,W):
    p=0
    wCounter = 0
    while p < len(T)-len(W)+1:
        matches_at(T,p,W,False)
        if p+len(W) < len(T):
            z = T[p+len(W)]
            lastZInW = W.rfind(z)
            if lastZInW == -1:
                p+=len(W)+1
            else:
                p+=len(W)-lastZInW
        else: break
   

W = 'ABCB'
T = 'ABCBCABC'

sundayAlg(T,W)
print(sundayCounter)



       


 




