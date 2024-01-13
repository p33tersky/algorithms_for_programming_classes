
def substringTwoDimentionalTab(S1, S2): #tworzenie tablicy
    rows = len(S2) + 1
    cols = len(S1) + 1
    tab = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if S2[i-1] == S1[j-1]:
                tab[i][j] = tab[i-1][j-1] + 1
            else:
                tab[i][j] = max(tab[i][j-1], tab[i-1][j])
    return tab



def printTable(S1, S2, tab):  #drukowanie tablicy wraz z wyrazami jako kolumna/wiersz 
                              #(nieznacząca metoda jeśli chodzi o algorytm, 
                              # ale znacząca jeśli chodzi o wyświetlenie i potwierdzenie, że kod działa)
    cols = len(S1)
    rows = len(S2)
    print(" "*4, end='')
    for sign in S1:
        print(sign, end=' ')
    print()
    for i in range(rows+1):
        if(i == 0):
            print(" ", end=' ')
        if(i!=0):
            print(S2[i-1], end=' ')
        for j in range(cols+1):
            print(tab[i][j], end=' ')
            if j == cols:
                print()


def returnLongestSubstringHavingGivenTable(S1, S2, tab): #zwracanie najdłuższego wspólnego podciągu mając już tablicę
    substring = ""
    i = len(S1)
    j = len(S2)
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            substring +=S1[i-1]
            i -=1
            j -=1
        else:
            if tab[j][i-1] >= tab[j-1][i]:  
                i -=1
            else:
                j-=1
    return substring[::-1]


def display(S1,S2): #złożenie wszystkiego co wyżej
    cols = len(S1)
    rows = len(S2)
    tab = substringTwoDimentionalTab(S1,S2)
    printTable(S1,S2,tab)
    print("Najdłuższy wspólny podciąg ma ", tab[rows][cols], " znaków")
    print("Najdłuższy wspólny podciąg: ", returnLongestSubstringHavingGivenTable(S1,S2,tab))       


display("WĄTRÓBKA", "WRÓŻKA")
# display("POLITECHNIKA", "TOALETA")
# display("ANAKONDA", "AKORDEON")
# display("ABDCADCABCDACCDABC","DCAACCBABDCD")
# display("BEZKRWISTOOJCZYŹNIANY", "PNEUMATYCZNO-HYDRAULICZNY")





