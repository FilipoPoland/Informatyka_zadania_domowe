# zadanie
# Napisz program symulujacy system
# program powinien umozliwiac zalogowanie sie przez podanie odpowiednich danych
# wykonanie trzech komend:
# wyswietlenie: :D :( i dostepnych komend
# mozliwosc wylogowania, ponownego zalogowania bez restartu
# mozna:
# ograniczyc ilosc mozliwych podejsc do logowaia
# u mnie jako zmienna nazwana ticker

from random import randint, shuffle

# !!!! IMPORTANT !!!!
# plik z loginami i haslami jest niezbedny plik Database.py zawierajacy dwie listy oznaczone l_user oraz l_pass
# od ich zawartosci bedzie zalezalo kto moze sie zalogowac. Pozostawienie tych list pustymi jest w porzadku. Program
# pozwala ustawic nowa nazwe uzytkownika i haslo do tego konta[nie pozwala na puste haslo]
from Database import l_user, l_pass


# Troche latwiej mi bylo zwiekszyc przejrzystosc reszty (przynajmniej moim zdaniem uzywajac definiowania)
# Zdefiniowanie funkcji


# przyda sie jako komunikat czy uzytkownik chce sie logowac
def chec():
    if komenda == 'wyjdz':
        czylogowac = 'n'
    else:
        czylogowac = input('Czy chcesz sie zalogowac?(t/n): ')
    c_question = True

    while c_question:
        if czylogowac == 't':
            return True
        elif czylogowac == 'n':
            return False
        else:
            czylogowac = input('Czy chcesz sie zalogowac?(t/n): ')


# wyswietlany komunikat na zadanie uzytkownika
def pomoc():
    print(f'Aby wyświetlić uśmiechniętą minkę wpisz: uśmiech.\n'
          'Aby wyświetlić smutną minkę wpisz: smutek.\n'
          'Aby wyświetlić prostokąt wpisz: prostokat.\n'
          'Aby obliczyć pole trapezu wpisz: trapez pole.\n'
          'Aby zagrać w grę z losowanie liczby wpisz: gra losowanie.\n'
          'Aby zagrać w kółko i krzyżyk wpisz: kółko i krzyżyk.\n'
          'Aby wyświetlić pole trójkątu wpisz: trójkąt pole. \n'
          'Aby usunąć wszystkich zapamiętanych użytkowników wpisz: purge. \n'
          'Aby wyświetlić komendy wpisz: pomoc.\n'
          'Aby się wylogować wpisz: logout.\n'
          'Aby zakończyć program wpisz: wyjdz')


# dodatkowo - pod proces rysowania prostokata na zadanie uzytkownika
def prostokat():
    # zdefiniowanie niezbednych zmiennych dla narysownia prostokata
    a = '#'
    b = ' '
    # zapytanie uztkownika o wymiary prostokata
    bok_a = int(input('Jak duży ma być bok a?'))
    bok_b = int(input('Jak duży ma być bok b?'))
    # narysowanie prostokata
    print(a * bok_a + ('\n' + a + b * (bok_a - 2) + a) * bok_b + '\n' + a * bok_a)


def trojkat_pole():
    print('Wyświetlmy trójkat: ')
    h = input('Podaj wysokość: ')
    h.replace(',', '.').replace(' ', '')
    h = float(h)
    a = input('Podaj długość podstawy: ')
    a.replace(',', '.').replace(' ', '')
    a = float(a)
    pole = (a * h) / 2
    print(pole)


# dodatkowo - oblicznie pola trapezu
def trapezpole():
    print('W celu obliczenia pola trapezu: ')
    # zapytanie o wymiary
    a = float(input('Podaj podstawę 1 trapezu: '))
    b = float(input('Podaj podstawę 2 trapezu: '))
    h = float(input('Podaj wysokość trapezu: '))

    # obliczenie pola trapezu
    print((a + b) / 2 * h)


# dodatkowo - gra zgadywanie liczby
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


# dodatkowo - gra w kolko i krzyzyk
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
# aby program wiedzial o jakiej zmiennej mowie(jest w definicji chec)
komenda = ''


while chec():
    # zapytanie uzytkownika czy ma juz konto
    nu_question = True
    while nu_question:
        nu = input('Czy jesteś istniejącym użytkownikiem? (t/n)')
        if nu == 't':
            nu_question = False

        # zdefiniowanie nowego konta
        elif nu == 'n':
            # komunikat powitalny w tworzeniu nowego hasla
            print('OK! Czas stowrzyć i zapisać twoje konto')

            # petla prawdziwa dopoki uzytkownik nie poda loginu nie bedacego w istniejacej bazie
            n_user_state = True
            while n_user_state:
                # zdefiniowanie nowego loginu
                login1 = input('Podaj nazwę nowego użytkownika: ')
                # sprawdzenie czy login istnie na liscie
                if login1 not in l_user:
                    l_user.append(login1)

                    # aby nie podajac hasla nie trzeba bylo powtarzac calego procesu
                    n_pass_state = True
                    while n_pass_state:

                        # zdefiniowanie hasla do nowego konta
                        password1 = (input('Podaj hasło do nowego konta: '))

                        # warunek - gdy haslo nie jest puste wykonaj
                        if password1 != '':
                            l_pass.append(password1)
                            # zakonczenie petli while hasla
                            n_pass_state = False

                            # zapisanie obu list jako odzielny plik dzieki temu nie tracimy nowych kont
                            with open('Database.py', 'w') as file:
                                file.write('l_user = ' + str(l_user) + '\n' + 'l_pass = ' + str(l_pass) + '\n')
                            # zakonczenie petli gdy uzytkownika
                            n_user_state = False
                        else:
                            # na wypadek nie podania hasla
                            print('Hasło nie może być puste. Proszę podaj hasło.')
                else:
                    # gdy uzytkownik poda cos co nie jest inne od istniejacych na liscie
                    # l_user elementow otrzyma komunikat
                    print('Ta nazwa użytkownika istnieje. Proszę podać inną.')
            # zamkniecie petli pytania o to czy stworzyc nowego uzytkownika
            nu_question = False

    # wyswietlenie ilosci poprzednich podejsc
    print(f'Podejście {ticker} z 5.')
    # zapytanie uzytkownika o login

    login2 = input('Podaj login: ')
    # sprawdzenie loginu
    if login2 in l_user:
        # index loginu aby wiedziec ktore haslo sprawdzic
        index = l_user.index(login2)
        # zapytanie o haslo
        haslo = input('Podaj hasło: ')
        if haslo == '':
            print('Błędne hasło.')
            ticker += 1
        # sprawdzenie prawdziwosci hasla
        elif haslo in l_pass[index]:
            logged = True
            print('Poprawne logowanie')
            pomoc()
            # reset tickera, aby program mial poprawna wartosc po wylogowaniu
            ticker = 1
            # podczas bycia zalogowanym beda dostepne komendy opisane wewnatrz funkcji while
            while logged:
                komenda = input('Komenda: ')
                if komenda == 'uśmiech':
                    print(':D')
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
                if komenda == 'trójkąt pole':
                    trojkat_pole()
                if komenda == 'pomoc':
                    pomoc()
                if komenda == 'purge':
                    print('Wpisując hasło super admina usuniesz wszystkich dotychczas zapisanych użytkowników: ')
                    s_admin_pass = input()
                    # nadpisuje baze danych z haslami i loginami pustymi listami tylko przy podaniu ponizszego hasla
                    if s_admin_pass == '123Super_Trudne_Hasło_132Nie_Idzie_Jak_Masło':
                        with open('Database.py', 'w') as file:
                            file.write('l_user = []\nl_pass = []')
                if komenda == 'logout':
                    logged = False
                    print('Zostałeś wylogowany.')
                if komenda == 'wyjdz':
                    break

        # gdy zostanie podane zle haslo
        else:
            print('Błędne hasło.')
            ticker += 1

    # aby ustawic ograniczenie podejsc i zakonczyc program
    elif ticker > 4:
        break

    # gdy zostanie podany zly login
    else:
        print('Błędny login.')
        ticker += 1
