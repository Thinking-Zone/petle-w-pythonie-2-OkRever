def jest_liczba_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 100  
print("Liczby pierwsze w zakresie od 2 do", n, "to:")
for liczba in range(2, n + 1):
    if jest_liczba_pierwsza(liczba):
        print(liczba)
