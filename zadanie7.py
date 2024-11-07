import random

def zgadnij_pogode():
    odpowiedzi = ["tak", "nie"]
    prawidlowa_odpowiedz = random.choice(odpowiedzi)
    
    while True:
        odpowiedz_uzytkownika = input("Czy dzisiaj pada deszcz? (tak/nie): ").lower()
        
        if odpowiedz_uzytkownika not in odpowiedzi:
            print("Proszę, odpowiedz 'tak' lub 'nie'.")
            continue
        
        if odpowiedz_uzytkownika == prawidlowa_odpowiedz:
            print("Gratulacje! Zgadłeś poprawnie.")
            break
        else:
            print("Niestety, to nie jest poprawna odpowiedź. Spróbuj ponownie.")

zgadnij_pogode()
