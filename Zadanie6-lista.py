# napisz program tworzacy liste z elemtow podanych przez uzytkownika
# lista ma posiadac 5 elemtow

list1 = []
print('Program prosi o 5 wartości które będzie próbował zrozumieć:\n'
      '- Dla tekstu, wartości logicznych poprostu go/je wprowadz,\n'
      '- Liczby należy wprowadzić używając kropki jako separatora dziesiętnego\n'
      '  w innym razie będzie zaklasyfikowana jako tekst,\n')

cusError = ''

for i in range(5):
    u_input = input(f'Podaj {i + 1} wyrażenie w liście: ')
    try:
        interpretation = int(u_input)
        list1.append(interpretation)
    except cusError:
        try:
            interpretation = float(u_input)
            list1.append(interpretation)
        except cusError:
            if u_input == 'True':
                interpretation = True
                list1.append(interpretation)
            elif u_input == 'False':
                interpretation = False
                list1.append(interpretation)
            else:
                interpretation = str(u_input)
                list1.append(interpretation)

for j in range(5):
    print(type(list1[j]))

print(list1)
