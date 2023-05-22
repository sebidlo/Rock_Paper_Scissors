import random
from os import system, name


# settings, global data to dictionary
settings_games = {
    "player_one_name" : "",
    "player_second_name" : "",
    "player_one_points" : 0,
    "player_seconds_points" : 0,
    "game_variant" : 0
}

'''
game_variant
# 1 - jeden gracz przeciwko kompterowi (komputer losuje), 
# 2 - dwóch graczy (każdy wybiera)
'''


def clear():
    '''
        define our clear function
    '''
    if name == 'nt':
        _ = system('cls')  # for windows
    else:
        _ = system('clear')  # for mac and linux(here, os.name is 'posix')


def set_settings():
    baner()
    settings_games['game_variant'] = int(input("wybierz wariant gry: "))
    print(f"wybrany wariant {settings_games['game_variant']}")
    settings_games['player_one_name'] = input("Podaj swoje imię: ")
    print(f"Witaj {settings_games['player_one_name']}")
    if settings_games['game_variant'] == 1:
        settings_games['player_second_name'] = "Komputer"
        print(f"Twoim przeciwnikiem będzie {settings_games['player_second_name']}")
        system('pause')
    else:
        settings_games['player_second_name'] = input("podaj imię drugiego graca: ")
        print(f"Witaj {settings_games['player_second_name']}")
        print("")
        print("Zaczynamy !!!")
        system('pause')
        
        
def show_results():
    print("Obecny stan gry:")
    print(f"Gracz pierwszy: {settings_games['player_one_name']}, punttów: {settings_games['player_one_points']} ")
    print(f"Gracz drugi: {settings_games['player_second_name']}, punktów: {settings_games['player_seconds_points']} ")
'''    
def count_points():
    print("liczenie wyników")
'''

def computer_movement():
    """Randomly return turn of computer 1, 2, 3."""
    turn = random.randint(1, 3)
    return turn

    
def baner_one():
    clear()
    print("Gra Kamień, Papier, Nozyce ")
    print("")
    if settings_games['player_one_points'] != 0:
        print("Statystyki:")
        show_results()


def baner():
    print("Jeśli chcesz garć z kompyterem wciśnij 1, jeśli z innym graczem wciśnij 2")


def info_window():
    # clear()
    # print("Gra Kamień, Papier, Nozyce ")
    print("Co wybierasz?")
    print("1 - Kamień, 2 - Papier, 3 - Nożyce, q - Koniec gry")
    '''
    if settings_games['player_one_points'] != 0:
        # print("Statystyki:")
        show_results()
    '''
    print("Twój wybór : ")


def schow_key(key):
    print(f"nacisnieto ....{key}")
    
def count_points(first_player_selection, second_player_selection):
    if first_player_selection == 1 and second_player_selection == 2:
        print("Gracz 1 wybrał Kamień, Gracz 2 wybrał Papier - w tej rudzie punkt zdobywa Gracz 2")        
        settings_games["player_seconds_points"] = settings_games["player_seconds_points"] + 1
    elif first_player_selection == 1 and second_player_selection == 3:
        print("Gracz 1 wybrał Kamień, Gracz 2 wybrał Nożyce - w tej rudzie punkt zdobywa Gracz 1")
        settings_games["player_one_points"] = settings_games["player_one_points"] + 1
        
    elif first_player_selection == 2 and second_player_selection == 1:
        print("Gracz 1 wybrał Papier, Gracz 2 wybrał Kamień - w tej rudzie punkt zdobywa Gracz 1")
        settings_games["player_one_points"] = settings_games["player_one_points"] + 1
    elif first_player_selection == 2 and second_player_selection == 3:
        print("Gracz 1 wybrał Papier, Gracz 2 wybrał Nożyce - w tej rudzie punkt zdobywa Gracz 2")
        settings_games["player_seconds_points"] = settings_games["player_seconds_points"] + 1
        
    elif first_player_selection == 3 and second_player_selection == 2:
        print("Gracz 1 wybrał Nożyce, Gracz 2 wybrał Papier - w tej rudzie punkt zdobywa Gracz 1")
        settings_games["player_one_points"] = settings_games["player_one_points"] + 1
    elif first_player_selection == 3 and second_player_selection == 1:
        print("Gracz 1 wybrał Nożyce, Gracz 2 wybrał Kamień - w tej rudzie punkt zdobywa Gracz 2")
        settings_games["player_seconds_points"] = settings_games["player_seconds_points"] + 1
        
    else: # first_player_selection == second_player_selection
        print("W tej rundzie mamy remis")
        



def read_key(): # -> int:
    key_1 = input("wybież wartiant ")
    return key_1


def main():
    baner_one()
    set_settings()
    clear()
    whose_move = 1 # 1 - palayer one, 2 payer second (computer)
    while True:
        clear()
        baner_one()
        info_window()
        key = read_key()
        key_2 = 0
        if key == '1':
            # clear()
            # schow_key(key)
            if whose_move == 1 and settings_games["game_variant"] == 1:
                key_2 = computer_movement()
                print(f"Losowanie {key_2}")
                
            count_points(int(key), key_2)
            show_results()
            system('pause')
        elif key == '2':
            # schow_key(key)
            if whose_move == 1 and settings_games["game_variant"] == 1:
                key_2 = computer_movement()
                print(f"Losowanie {key_2}")
                
            count_points(int(key), key_2)
            show_results()
            system('pause')
        elif key == '3':
            # schow_key(key)
            if whose_move == 1 and settings_games["game_variant"] == 1:
                key_2 = computer_movement()
                print(f"Losowanie {key_2}")
                
            count_points(int(key), key_2)
            show_results()
            system('pause')
        elif key == 'q': # ord('q'):  # 'q':
            break
        else:
            print("Wciśnij jeden z obsługiwanych klawiszy... ")
            # clear()


if __name__ == "__main__":
    main()
