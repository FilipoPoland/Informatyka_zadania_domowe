# zadanie 1
# 30 pseudolosowych liczb
# zakres: -50, 50
# za pomoca for stworz liste
# stworz liste z elementami z poprzedniej mniejsze od tej ktora poda uzytkownik
# zadanie 2
# 30 pseudolosowych liczb
# zakres: -50, 50
# stworz dwie nowe
# pierwsza z parzystymi druga nieparzystymi
# zadanie 3
# Napisz funkcje sprawdzajaca czy liczba jest pierwsza

# funkcja losująca liczby gdzie
# getiteam1 - to ile
# getiteam2 - początek przedziału
# getiteam3 - koniec przedziału
def los(getiteam1, getiteam2, getiteam3):
    from random import randint
    list_los = []
    for i in range(getiteam1):
        list_los.append(randint(getiteam2, getiteam3))
    return list_los


# def pierwsza
def pierwsza(getiteam):
    wyniki = []
    for z in range(2, getiteam + 1):
        for j in wyniki:
            if z % j == 0:
                break
        else:
            wyniki.append(z)
    if getiteam in wyniki:
        return True
    else:
        return False


# zadanie 1
print('Zadanie 1:')
while True:
    try:
        u_input = int(input('Podaj liczbę, która ustali górną granicę dla listy liczby, które zostaną wylosowane: '))
        break
    except:
        print('- - - - - - - B Ł Ą D - - - - - - -'
              'Proszę o podanie poprawnych danych')

list2 = []
for i in los(30, -50, 50):
    if i < u_input:
        list2.append(i)

print(list2)

# zadanie 2
print('\nZadanie 2:')
listp = []
listnp = []
list_los = los(30, -50, 50)

for i in list_los:
    if i % 2 == 0:
        listp.append(i)
    else:
        listnp.append(i)

print(f'Lista losowych liczb to: {list_los}')
print(f'liczby nieparzyste to: {listnp}\nLiczby parzyste to: {listp}')

# zadanie 3
print('\nZadanie 3')
while True:
    try:
        u_input2 = int(input('Podaj liczbe, aby sprawdzić czy jest ona liczbą pierwszą: '))
        break
    except:
        print('- - - - - - - B Ł Ą D - - - - - - -'
              'Proszę o podanie poprawnych danych')

# funkcja pierwsza zwraca wartosc logiczna
if pierwsza(u_input2):
    # jezeli prawda
    print('To liczba pierwsza.')
else:
    # w innym razie
    print('To nie jest liczba pierwsza')

input('Naciśnij enter aby zakończyć program.')
