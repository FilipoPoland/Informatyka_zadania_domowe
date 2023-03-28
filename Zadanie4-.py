# przyda sie przy czesci 3
from datetime import datetime

# zadanie 1
# pole trapezu o podanych przez uzytkownika podstawie i wysokosci
# zwracajacy informacje czy jest to liczba calkowita jezeli tak to czy jest parzysta

# zapytanie uzytkownika o zmienne
a = float(input('Podaj podstawę 1 trapezu'))
b = float(input('Podaj podstawę 2 trapezu'))
h = float(input('Podaj wysokość trapezu'))

# obliczenie pola trapezu
t = a * b / 2 * h

# sprawdzenie czy liczba jest calkowita
print(f'Pole trapezu wynosi {t}')
if t % 1 == 0:
    # sprawdzenie parzystosci
    if t % 2 == 0:
        print('Jest to liczba całkowita, parzysta')
    else:
        print('Liczba nie jest parzysta')
# gdy nie jest calkowita
else:
    print('Jest to liczba nicałkowita')

# zadanie 2 zapytaj uzytkownika o imie, nastepnie policz ilosc znkow w podanym imieniu i powiedz
# czy jest podzielna przez 3

# poproszenie uzytkownika o imie
i = input('Podaj swoje imię: ')
# obliczenie dlugosci imienia
g = len(i)

# sprawdzenie podzielnosci przez 3
if g % 3 == 0:
    print('Liczba jest podzielna przez 3.')
else:
    print('Liczba nie jest podzielna przez 3.')

# zadanie 3 zapytaj o imie, wiek, czy mial w tym roku urodziny
# przywitaj go uzywajac tego imienia i zwracajacy poprawna informacje w za ile w ktorym roku bedzie mial` 100 lat

# data osiagniecia 100 sposob aktualny tylko jezeli aktualny rok to 2023

i = input('Podaj swoje imię: ')
w = int(input('Podaj swój wiek: '))
u = input('Jeżeli miałeś/miałaś w tym roku urodziny wprowadz "tak".')

if u == 'tak':
    r100 = 2023 + 100 - w
    print(f'Witaj, {i} w roku {r100} będziesz miał/miała 100 lat.')
else:
    r100 = 2023 + 99 - w
    print(f'Witaj, {i} w roku {r100} będziesz miał/miała 100 lat.')

# to jest z data importowana z ponizszej funkcj


i = input('Podaj swoje imię: ')
w = int(input('Podaj swój wiek: '))
u = input('Jeżeli miałeś/miałaś w tym roku urodziny wprowadz "t".')

if u == 't':
    r100 = datetime.now().year + 100 - w
    print(f'Witaj, {i} w roku {r100} będziesz miał/miała 100 lat.')
else:
    r100 = datetime.now().year + 99 - w
    print(f'Witaj, {i} w roku {r100} będziesz miał/miała 100 lat.')
