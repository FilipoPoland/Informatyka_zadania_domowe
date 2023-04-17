# zadanie
# Napisz program symulujacy system
# program powinien umozliwiac zalogowanie sie przez podanie odpowiednich danych
# wykonanie trzech komend:
# wyswietlenie: :D :( i dostepnych komend
# mozliwosc wylogowania, ponownego zalogowania bez restartu
# mozna:
# ograniczyc ilosc mozliwych podejsc do logowaia
# u mnie jako zmienna nazwana ticker

l_user = 'admin'
l_pass = 'Admin'


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
          'Aby wyświetlić komendy wpisz: pomoc.\n'
          'Aby się wylogować wpisz: logout.\n'
          'Aby zakończyć program wpisz: wyjdz')


# zdefiniowanie wstepnych zmiennych
ticker = 1
# aby program wiedzial o jakiej zmiennej mowie(jest w definicji chec)
komenda = ''


while chec():
    # wyswietlenie ilosci poprzednich podejsc
    print(f'Podejście {ticker} z 5.')
    # zapytanie uzytkownika o login

    login2 = input('Podaj login: ')
    # sprawdzenie loginu
    if login2 == l_user:
        # zapytanie o haslo
        haslo = input('Podaj hasło: ')
        # sprawdzenie prawdziwosci hasla
        if haslo == l_pass:
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
                if komenda == 'pomoc':
                    pomoc()
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
