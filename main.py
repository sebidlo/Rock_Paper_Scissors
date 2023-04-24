from os import system, name

# settings
player_one_name = ""
player_second_name = ""
player_one_points = 0
player_seconds_points = 0
game_variant = 0 
'''
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
    game_variant = int(input("wybierz wariant gry: "))
    print(f"wybrany wariant {game_variant}")
    player_one_name = input("Podaj swoje imię: ")
    print(f"Witaj {player_one_name}")
    if game_variant == 1:
        print("Twoim przeciwnikiem będzie komputer")
        system('pause')
    else:
        player_second_name = input("podaj imię drugiego graca: ")
        print(f"Witaj {player_second_name}")
        print("")
        print("Zaczynamy !!!")
        system('pause')
        
        
def show_results():
    print("Tu bedą wyniki: ...")
    
def count_points():
    print("liczenie wyników")
    
def baner():
    clear()
    print("Gra Kamień, Papier, Nozyce ")
    if player_one_points != 0:
        print("Statystyki:")
        show_results()
    
    
def info_window():
    clear()
    # print("Gra Kamień, Papier, Nozyce ")
    print("Co wybierasz?")
    print("1 - Kamień, 2 - Papier, 3 - Nożyce, q - Koniec gry")
    print("Statystyki:")
    show_results()
    print("Twój wybór : ")


def schow_key(key):
    print(f"nacisnieto a ....{key}")


def read_key(): # -> int:
    key_1 = input("wybież wartiant ")
    return key_1


def main():
    baner()
    set_settings()
    while True:
        baner()
        info_window()
        key = read_key()
        if key == '1':
            # clear()
            schow_key(key)
            print("ok 1")
        elif key == '2':
            schow_key(key)
        elif key == '3':
            schow_key(key)
        elif key == 'q': # ord('q'):  # 'q':
            break
        else:
            print("inny")
            # clear()


if __name__ == "__main__":
    main()
