def zgadnij_pogode():
    liczba_nie = 0

    while True:
        odpowiedz_uzytkownika = input("Czy dzisiaj pada deszcz? (tak/nie/nie wiem): ").lower()
        
        if odpowiedz_uzytkownika == "tak":
            print(f"Gratulacje! Odpowiedziałeś poprawnie. Liczba odpowiedzi 'nie': {liczba_nie}")
            break
        elif odpowiedz_uzytkownika == "nie":
            liczba_nie += 1
            print("Niestety, to nie jest poprawna odpowiedź. Spróbuj ponownie.")
        elif odpowiedz_uzytkownika == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("Proszę, odpowiedz 'tak', 'nie' lub 'nie wiem'.")

zgadnij_pogode()
