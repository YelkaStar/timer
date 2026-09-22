from pathlib import Path
import time
import curses
words = []
numbers = []
welcome_text = "Добро пожалавать, в умный таймер version 1.0.0"
menu_text = "Функции: 1 — таймер. 2 — сумма времени. 3 — список файлов 0 - Назад\Выход."
file_names = []
def taimer(stdscr):
    start = time.perf_counter()
    while True:
        key = stdscr.getch()
        if key in {48}:
            end = time.perf_counter()
            elapsed = end - start
            file_name = time.strftime("%d-%m-%Y-%H-%M-%S")
            break
        else:
            stdscr.addstr(5, 2, "Неправельный вод. Нажми 0 что бы остановить.", curses.color_pair(1))
            stdscr.refresh()
    return elapsed, file_name

def fails():
    file_names.clear()
    for path in Path("/home/yelkastar/Desktop/python/8.9.2026").glob("*.txt"):
        file_names.append(path.name)


def summm():
    for path in Path("/home/yelkastar/Desktop/python/8.9.2026").glob("*.txt"):
        words.extend(path.read_text(encoding="utf-8").split())
        for i in range(len(words)):
            try:
                numbers.append(float(words[i]))
            except ValueError:
                continue
        words.clear()
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    numbers.clear()
    return total

def menu1(stdscr):
    col = 0
    for char in welcome_text:
        col += 1
        stdscr.addstr(0, col, char, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.10)
        stdscr.nodelay(True)
        key = stdscr.getch()
        if key in (10, 13):
            break
    stdscr.nodelay(False)
    stdscr.addstr(0, 1, welcome_text, curses.color_pair(1))

def menu2(stdscr):
    col = 0
    for char in menu_text:
        col += 1
        stdscr.addstr(2, col, char, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.10)
        stdscr.nodelay(True)
        key = stdscr.getch()
        if key in (10, 13):
            break
    stdscr.nodelay(False)
    stdscr.addstr(2, 1, menu_text, curses.color_pair(1))
    stdscr.refresh()

def menu4(stdscr):
    stdscr.clear()
    stdscr.addstr(4,1, "Таймер пошед. 0 что бы остановить")
    stdscr.refresh()
    elapsed, file_name = taimer(stdscr)
    with open(f"/home/yelkastar/Desktop/python/8.9.2026/{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(f"Прошлосссс: {elapsed:.2f} сек")
    stdscr.addstr(6, 1, f"Прошло: {elapsed:.2f} сек", curses.color_pair(1))
    stdscr.refresh()

def Main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1,curses.COLOR_GREEN,  curses.COLOR_BLACK)
    menu1(stdscr)
    while True:
        menu2(stdscr)
        key = stdscr.getch()
        if key in {49}:
            menu4(stdscr)
            stdscr.addstr(1,1, "Нажмите Enter", curses.color_pair(1))
            stdscr.getch()
            stdscr.clear()
        if key in {50}:
            stdscr.clear()
            total = summm()
            stdscr.addstr(7, 1, f"Сума {total:.2f}", curses.color_pair(1))
            stdscr.refresh()
            stdscr.addstr(5,1, "Нажмите Enter", curses.color_pair(1))
            stdscr.getch()
            stdscr.clear()
        if key in {51}:
            fails()
            stdscr.clear()
            stdscr.addstr(6,1, f"Syma {file_names}", curses.color_pair(1))
            stdscr.refresh()
            stdscr.addstr(1,1, "Нажмите Enter", curses.color_pair(1))
            stdscr.getch()
            stdscr.clear()
        if key in {48}:
            return

curses.wrapper(Main)
