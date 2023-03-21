# zadanie domowe
# 1. zmienna z input, zwrocic co drugi znak do 6 wlacznie nastepnie wszystko

# Wersja a
x = input('Proszę podać frazę składającą się z co najmniej 8 znaków:')
print(x[1:6:2] + x[6::])
# Wersja b
x = input('Proszę podać frazę składającą się z co najmniej 8 znaków:')
print(x[0:6:2] + x[6::])

# 2. zmienna z input, wyswietl od tylu

y = input('Proszę podać frazę, która zostanie wyświetlona od tyłu:')
print(y[::-1])

# razem
y = input('Proszę podać frazę, która zostanie wyświetlona od tyłu oraz jej ostatnie 6 znaków zostanie wyświetlone '
          'ze skokiem 2:')
print(y[-1:-7:-2] + y[-7::-1])

# aby program czekal po zakonczeniu operacji
input('Naciśnij enter, aby zakończyć')
# Filip Kozlowski
