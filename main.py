from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def schow_key(key):
    print(f"nacisnieto a ....{key}")
    
def read_key() -> int:
    key_1 = int(input("wybież wartiant"))
    return key_1


def main():
    while True:
        key = read_key()
        if key == 1:
            print("ok 1")
            clear()
        else:
            print("inny")
        

if __name__ == "__main__":
    main()