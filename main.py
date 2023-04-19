import curses

def main(stdscr):
    # Ustawiamy kursor konsoli na ukryty
    curses.curs_set(0)
    # Ustawiamy nieblokujący tryb klawiatury
    stdscr.nodelay(True)
    while True:
        # Pobieramy kod znaku naciśniętego przez użytkownika
        key = stdscr.getch()
        print(key)
        if key != curses.ERR:
            # obsługa klawiszy
            if key == ord('a'):
                stdscr.addstr(0, 0, "Klawisz 'a' został naciśnięty.")
            elif key == ord('b'):
                stdscr.addstr(0, 0, "Klawisz 'b' został naciśnięty.")
        stdscr.refresh()

# Inicjujemy konsolę
curses.wrapper(main)