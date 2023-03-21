# input polacz w jeden print odzielony spacja dwa pierwsze znaki str zamien na dwa pierwsze drugiego str
# podanie frazy 1
i1 = input('Podaj fraze 1')
# podanie frazy 2
i2 = input('Podaj fraze 2')
# zastapienie pierwszych dwoch znakow pierwszego wyrazu pierwszymi dwoma z drugiego
# zrobienie tego samego dla drugiej frazy
print(i1.replace(i1[0:2], i2[0:2], 1), i2.replace(i2[0:2], i1[0:2], 1))

# zapytanie o imie, zdefiniowanie zmiennej
imie = input('Podaj swoje imie: ')
# zapytanie o wiek, zdefiniowanie zmiennej jako int
wiek = int(input('Podaj swój wiek: '))
# przywitanie uzytkownika z imienia i podanie ile lat zostalo mu do 100 lat
do100 = 100 - wiek
print(f'Witaj, {imie} za {do100} lat osiągniesz wiek 100 lat')

# z data urodzenia

# zapytanie o imie, zdefiniowanie zmiennej
imie = input('Podaj swoje imie: ')
# zapytanie o wiek, zdefiniowanie zmiennej jako int
wiek = int(input('Podaj swój rok urodzenia: '))
# obliczenie roku
do100 = wiek + 100
# przywitanie uzytkownika z imienia i podanie roku w ktorym osiagnie wiek 100 lat
print(f'Witaj, {imie} w {do100} osiągniesz wiek 100 lat')

# oblicz pole trojkata o wymiarach podanych przez uzytkownika wysokosc i podstawa
print('W celu obliczenia trójkąta...')
a = float(input('Podaj wielkość podstawy: '))
h = float(input('Podaj wysokość'))
print('Pole trójkąta:', a*h/2)

input('Naciśnij enter, aby zakończyć program')
# Filip Kozlowski
