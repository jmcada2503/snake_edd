import os
from termcolor import colored
import time

class Screen:
    width = 0
    height = 0
    table = []

    offset = 2
    char = '.'

    def __init__(self):
        size = os.get_terminal_size()
        self.width = size.columns-(self.offset*4)
        self.height = size.lines-(self.offset*2)
        for i in range(self.height):
            self.table.append([self.char]*self.width)

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def message(self, message):
        middle = (self.width//2, self.height//2)

        s = [
            (' '*(len(message)+6)),
            (' '+('*'*(len(message)+4))+' '),
            (" * "+message+" * "),
            (' '+('*'*(len(message)+4))+' '),
            (' '*(len(message)+6))
        ]
        l = middle[0]-((len(message)+6)//2)
        u = middle[1]-2
        for i in range(5):
            for j in range(len(message)+6):
                self.table[u+i][l+j] = colored(s[i][j], "light_magenta") if s[i][j] == '*' else s[i][j]

    def printFrame(self, points, initial_time):
        self.clear()
        print('\n'*self.offset, end='')
        for i in range(self.height):
            print(' '*(self.offset*2), end='')
            for j in range(self.width):
                print(self.table[i][j], end='')
            print()
        info_line = f" Puntos -> {points}"
        time_info = f"{round(time.time()-initial_time, 1)} <- Tiempo "
        info_line += (' '*(os.get_terminal_size().columns-len(info_line)-len(time_info)))+time_info
        print(('\n'*(self.offset-1))+info_line)
