# Polecenie - wyswietl analogicz prostokat o wymiarach 9x5 ze zmiennymi i powielonymi str

# Zdefiniowanie zmiennej b - skrajne wiersze prostokata
b = ('#' * 9)
# Zdefiniowanie zmiennej a - wewnetrzne wiersze prostokata
a = ('#' + ' ' * 7 + '#' + '\n')

# Dla porownania czy prostokat dobrze sie wyswietla
'''
print('#'*9+'\n'+('#'+' '*7+'#'+'\n')*3+'#'*9)
'''

print(b + '\n' + a * 3 + b)
# zdefinowanie zmiennych dla trapezu
d = ' '
c = '#'
e = '####'
c1 = c + d * 3 + c
c2 = c + d * 5 + c
c3 = c + d * 6 + c
c4 = c + d * 7 + c
c5 = c + d * 8 + c
c6 = c + d * 9 + c
c7 = c + d * 10 + c
c8 = c * 12

# przerwa miedzy jedna a druga figura
print('\n')
# wyswietlenie trapezu
print(e + '\n' + c1 + '\n' + c2 + '\n' + c3 + '\n' + c4 +'\n' + c5 +'\n' + c6 + '\n' + c7 + '\n' + c8)

# prostokat uzytkownika
x = 0
while x<1:
    a = '#'
    b = ' '
    bok_a = int(input('Jak duży ma być bok a?'))
    bok_b = int(input('Jak duży ma być bok b?'))

    print(a * bok_a +('\n' + a + b * (bok_a - 2) +a) * bok_b + '\n' + a * bok_a)

    f = int(input('Wprowadz 0, aby kontynuować program, a 1 aby go zakończyć.'))
    x = x + f

# Filip Kozlowski
