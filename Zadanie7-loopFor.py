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


def los(getiteam1, getiteam2, getiteam3):
    from random import randint
    list_los = []
    for i in range(getiteam1):
        list_los.append(randint(getiteam2, getiteam3))
    return list_los


def pierwsza(getiteam):
    dzielniki = [2, 3, 4, 5, 6, 7]
    for i in dzielniki:
        if getiteam % i == 0:
            return False
        else:
            return True


# zadanie 1
while True:
    try:
        u_input = int(input('Podaj liczbe: '))
        break
    except:
        print('Podaj liczbe.')

list2 = []
for i in los(30, -50, 50):
    if i < u_input:
        list2.append(i)

print(list2)

# zadanie 2
listp = []
listnp = []

for i in los(30, -50, 50):
    if i % 2:
        listp.append(i)
    else:
        listnp.append(i)

print(f'liczby nieparzyste to: {listnp}\nLiczby parzyste to: {listp}')

#zadanie 3

u_input2 = input('Podaj liczbe: ')
print(pierwsza(u_input2))
