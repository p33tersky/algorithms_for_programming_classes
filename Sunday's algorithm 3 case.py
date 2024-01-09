# Należy zaimplementować dwa algorytmy wyszukiwania wzorca w tekście: naiwny oraz Sunday’a.
# Dodatkowo należy opanować (ze zrozumieniem) teorię dotyczącą tych algorytmów (zasady działania, złożoności obliczeniowe czasowe i pamięciowe).

# Dane do wykresu przedstawiającego zależność od |A| można spreparować następującym algorytmem:
# Dla kolejnych wielkości alfabetu |A| od 1 do 20 (jako A można użyć kilku pierwszych liter spośród a, …, z):
# Używając alfabetu A o wielkości |A|, wylosuj tekst T (np. o długości 10000) i wzorzec W (np. o długości 10).
# Zmierz liczbę porównań znaków wykonanych przy wyszukiwaniu wszystkich wystąpień W w T przez algorytm naiwny.
# Zapisz wielkość A (x=|A|) oraz zmierzoną liczbę porównań (y). 
# Te dwie liczby (x, y) stanowią pojedynczy punkt do wykresu dla algorytmu naiwnego.
# To samo wykonaj dla algorytmu Sunday’a i innych (jeśli zaimplementowano) by otrzymać po jednym punkcie pomiarowym
# dla każdego z tych algorytmów.

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

ascii = list(string.ascii_lowercase)


Xn = []
Yn = []
Xs = []
Ys = []

for i in range(20):
    A=''
    T=''
    W=''
    for j in range(i+1):
        A+=ascii[j]
    
    for j in range(1000):
        T+=random.choice(A)
    
    for j in range(10):
        W+=random.choice(A)

    naiveAlg(T,W)
    sundayAlg(T,W)
    Xn.append(i)
    Yn.append(naiveCounter)
    Xs.append(i)
    Ys.append(sundayCounter)
    naiveCounter = 0
    sundayCounter = 0
    

plt.plot(Xn, Yn)
plt.plot(Xs,Ys)
plt.show()



       


 




