from os import system, name


def clear():
    '''
        define our clear function
    '''
    if name == 'nt':
        _ = system('cls')  # for windows
    else:
        _ = system('clear')  # for mac and linux(here, os.name is 'posix')


def schow_key(key):
    print(f"nacisnieto a ....{key}")


def read_key() -> int:
    key_1 = int(input("wybież wartiant "))
    return key_1


def main():
    while True:
        key = read_key()
        if key == 1:
            # clear()
            schow_key(key)
            print("ok 1")
        else:
            print("inny")
            # clear()


if __name__ == "__main__":
    main()
