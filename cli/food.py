from termcolor import colored
from random import randint

class Food:
    char = colored('@', "red")

    def __init__(self, position):
        self.position = position

    def nextPosition(self, max_x, max_y):
        return (
            randint(0, max_x-1),
            randint(0, max_y-1),
        )

    def move(self, max_x, max_y, snake):
        new_pos = self.nextPosition(max_x, max_y)
        while (new_pos in snake.body[1]):
            new_pos = self.nextPosition(max_x, max_y)
        self.position = new_pos
