# zadanie 1. zapytaj o dwie frazy i zamien pierwsze dwa znaki z frazy 1 do frazy 2 i vice versa
# zadanie 2. zapyta uzytkownika o imie wiek, przywitaj imieniem i powiedz ile lat zostalo mu do 100 lat
# zadanie 3. oblicz pole trojkata na podstawie podstawy i wysokosci podanych przez uzytkownika

# czesc 1
# input polacz w jeden print odzielony spacja dwa pierwsze znaki str zamien na dwa pierwsze drugiego str

# podanie frazy 1
i1 = input('Podaj fraze 1')
# podanie frazy 2
i2 = input('Podaj fraze 2')

# zastapienie pierwszych dwoch znakow pierwszego wyrazu pierwszymi dwoma z drugiego
print(i1.replace(i1[0:2], i2[0:2], 1),
      # zrobienie tego samego dla drugiej frazy
      i2.replace(i2[0:2], i1[0:2], 1))

# czesc 2
# zapytanie o imie, zdefiniowanie zmiennej
imie = input('Podaj swoje imie: ')
# zapytanie o wiek, zdefiniowanie zmiennej jako int
wiek = int(input('Podaj swój wiek: '))
# przywitanie uzytkownika z imienia i podanie ile lat zostalo mu do 100 lat
do100 = 100 - wiek
print(f'Witaj, {imie} za {do100} lat osiągniesz wiek 100 lat')

# dodatkowo
# z data urodzenia

# zapytanie o imie, zdefiniowanie zmiennej
imie = input('Podaj swoje imie: ')
# zapytanie o wiek, zdefiniowanie zmiennej jako int
wiek = int(input('Podaj swój rok urodzenia: '))
# obliczenie roku
do100 = wiek + 100
# przywitanie uzytkownika z imienia i podanie roku w ktorym osiagnie wiek 100 lat
print(f'Witaj, {imie} w {do100} osiągniesz wiek 100 lat')
# koniec dodatkowo

# czesc 3
# oblicz pole trojkata o wymiarach podanych przez uzytkownika wysokosc i podstawa
print('W celu obliczenia trójkąta...')
# zapytanie o wielkosc podstawy
a = input('Podaj wielkość podstawy: ')
# aby nie bylo blednych znakow w float
a = a.replace(',', '.')
a = a.replace(' ', '')
# nadanie klasy
a = float(a)

# zapytanie o wysokosc
h = input('Podaj wysokość')
# aby nie bylo blednych znakow w float
h = h.replace(',', '.')
h = h.replace(' ', '')
# nadanie klasy
h = float(h)

# wyswietlenie i obliczenie pola
print('Pole trójkąta:', a*h/2)

input('Naciśnij enter, aby zakończyć program')
# Filip Kozlowski
