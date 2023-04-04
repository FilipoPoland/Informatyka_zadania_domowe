# zadanie
# Napisz program symulujacy system
# program powinien umozliwiac zalogowanie sie przez podanie odpowiednich danych
# wykonanie trzech komend:
# wyswietlenie: :D :( i dostepnych komend
# mozliwosc wylogowania, ponownego zalogowania bez restartu
# mozna:
# ograniczyc ilosc mozliwych podejsc do logowaia

from random import randint, shuffle
# Troche latwiej mi bylo zwiekszyc przejrzystosc reszty (przynajmniej moim zdaniem
# czy uzytkownik chce sie logowac


# Zdefiniowanie paru funkcji
def chec():
    c = input('Czy chcesz sie zalogowac?(t/n): ')
    if c == 't':
        return True
    else:
        return False


# wyswietlany komunikat na zadanie uzytkownika
def pomoc():
    print('Aby wyświetlić uśmiechniętą minkę wpisz: uśmiech.\n'
          'Aby wyświetlić smutną minkę wpisz: smutek.\n'
          'Aby wyświetlić prostokąt wpisz: prostokat.\n'
          'Aby obliczyć pole trapezu wpisz: trapez pole.\n'
          'Aby zagrać w grę z losowanie liczby wpisz: gra losowanie.\n'
          'Aby zagrać w kółko i krzyżyk wpisz: kółko i krzyżyk.\n'
          'Aby wyświetlić komendy wpisz: pomoc.\n'
          'Aby się wylogować wpisz: logout.\n'
          'Aby zakończyć program wpisz: wyjdz')


# pod proces rysowania prostokata na zadanie uzytkownika
def prostokat():
    # zdefiniowanie niezbednych zmiennych dla narysownia prostokata
    a = '#'
    b = ' '
    # zapytanie uztkownika o wymiary prostokata
    bok_a = int(input('Jak duży ma być bok a?'))
    bok_b = int(input('Jak duży ma być bok b?'))
    # narysowanie prostokata
    print(a * bok_a + ('\n' + a + b * (bok_a - 2) + a) * bok_b + '\n' + a * bok_a)


# oblicznie pola trapezu
def trapezpole():
    print('W celu obliczenia pola trapezu: ')
    # zapytanie o wymiary
    a = float(input('Podaj podstawę 1 trapezu: '))
    b = float(input('Podaj podstawę 2 trapezu: '))
    h = float(input('Podaj wysokość trapezu: '))

    # obliczenie pola trapezu
    print((a + b) / 2 * h)


# gra zgadywanie liczby
def gra_los():
    liczba = randint(1, 100)
    counter_los = 0
    print('Została wylosowana liczba od 1 do 100. \n Aby przerwać wpisz escape.')
    x = True
    while x:
        user_liczba = input('O jakiej liczbie myślę?')
        counter_los += 1
        if user_liczba == 'escape':
            x = False
        elif int(user_liczba) == liczba:
            x = False
            print(f'Gratulacje! Udało się po {counter_los}')
        elif int(user_liczba) > liczba:
            print('Moja liczba jest mniejsza.')
        elif int(user_liczba) < liczba:
            print('Moja liczba jest większa.')


# gra w kolko i krzyzyk
def kk():
    def plansza(stan):
        a = 0
        for j in range(3):
            for i1 in range(3):
                print('+', 3 * '-', sep='', end='')
            print('+')
            for i1 in range(3):
                print('|', ' ', stan[a], ' ', sep='', end='')
                a += 1
            print('|')
        for i1 in range(3):
            print('+', 3 * '-', sep='', end='')
        print('+')

    def sprawdz(getiteam, getiteam2, getiteam3):
        # for X
        if getiteam[0] == getiteam[1] == getiteam[2] == 'X':
            getiteam2.append('You won.')
            return False
        elif getiteam[3] == getiteam[4] == getiteam[5] == 'X':
            getiteam2.append('You won.')
            return False
        elif getiteam[6] == getiteam[7] == getiteam[8] == 'X':
            getiteam2.append('You won.')
            return False
        elif getiteam[0] == getiteam[4] == getiteam[8] == 'X':
            getiteam2.append('You won.')
            return False
        elif getiteam[2] == getiteam[4] == getiteam[6] == 'X':
            getiteam2.append('You won.')
            return False
        elif getiteam[0] == getiteam[3] == getiteam[6] == 0:
            getiteam2.append('You won.')
            return False
        elif getiteam[1] == getiteam[4] == getiteam[7] == 0:
            getiteam2.append('You won.')
            return False
        elif getiteam[2] == getiteam[5] == getiteam[8] == 0:
            getiteam2.append('You won.')
            return False
        # for 0
        elif getiteam[0] == getiteam[1] == getiteam[2] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[3] == getiteam[4] == getiteam[5] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[6] == getiteam[7] == getiteam[8] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[0] == getiteam[4] == getiteam[8] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[2] == getiteam[4] == getiteam[6] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[0] == getiteam[3] == getiteam[6] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[1] == getiteam[4] == getiteam[7] == 0:
            getiteam2.append('The computer won.')
            return False
        elif getiteam[2] == getiteam[5] == getiteam[8] == 0:
            getiteam2.append('The computer won.')
            return False
        elif not getiteam3:
            getiteam2.append('It is a tie')
            return False
        else:
            return True

    list1 = [' '] * 9

    list2 = []
    for i in range(9):
        list2.append(i)

    zwyciestwo = []

    x = sprawdz(list1, zwyciestwo, list2)

    while x:
        shuffle(list2)
        los = list2[0]
        del (list2[0])
        # nwm czemu to mu sie nie podoba ale dziala
        list1[los] = 0
        plansza(list1)
        x = sprawdz(list1, zwyciestwo, list2)
        if x:
            user = int(input('Podaj pole(zakres 1-9): '))
            user -= 1
            list1[user] = 'X'
            list2.remove(user)
            x = sprawdz(list1, zwyciestwo, list2)

    print(plansza(list1), '\n', zwyciestwo[0])


# zdefiniowanie wstepnych zmiennych
ticker = 1
l_user = ['admin']
l_pass = ['AdmiN']

end = True
while end:
    end = chec()
    # zapyttanie uzytkownika czy ma juz konto
    nu = input('Czy jesteś istniejącym użytkownikiem? (t/n)')
    # zdefiniowanie nowego konta
    if nu == 'n':
        # zdefiniowanie nowego loginu
        l_user.append(input('Podaj nazwę użytkownika: '))
        # zdefiniowanie hasla do nowego konta
        l_pass.append(input('Podaj hasło do konta: '))

    # wyswietlenie ilosci poprzednich podejsc
    print(f'Podejście {ticker} z 5.')
    # zapytanie uzytkownika o login
    login = input('Podaj login: ')

    # sprawdzenie loginu
    if login in l_user:
        index = l_user.index(login)
        haslo = input('Podaj hasło: ')
        # sprawdzenie prawdziwosci hasla
        if haslo in l_pass[index]:
            logged = True
            print('Poprawne logowanie')
            pomoc()
            # podczas bycia zalogowanym beda dostepne komendy opisane wewnatrz funkcji while
            while logged:
                komenda = input('Komenda: ')
                if komenda == 'uśmiech':
                    print(':)')
                if komenda == 'smutek':
                    print(':(')
                if komenda == 'prostokat':
                    prostokat()
                if komenda == 'trapez pole':
                    trapezpole()
                if komenda == 'gra losowanie':
                    gra_los()
                if komenda == 'kółko i krzyżyk':
                    kk()
                if komenda == 'pomoc':
                    pomoc()
                if komenda == 'logout':
                    logged = False
                    print('Zostałeś wylogowany.')
                if komenda == 'wyjdz':
                    end = False
        # gdy zostanie podane zle haslo
        else:
            print('Błędne hasło.')
            ticker += 1
    # aby ustawic ograniczenie podejsc i zakonczyc program
    elif ticker > 4:
        end = False
    # gdy zostanie podany zly login
    else:
        print('Błędny login.')
        ticker += 1
