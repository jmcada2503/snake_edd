from collections import deque
from termcolor import colored

class Snake:

    body = [deque(), set()]
    char = colored('s', 'light_green')
    speed = 1
    direction = (0, -1)

    def __init__(self, position:tuple):
        self.body[0].append(position)
        self.body[0].append((position[0], position[1]+1))
        self.body[0].append((position[0], position[1]+2))

        self.body[1].add(position)
        self.body[1].add((position[0], position[1]+1))
        self.body[1].add((position[0], position[1]+2))

    def setDirection(self, direction):
        if (direction == 'u' and self.direction != (0,1)):
            self.direction = (0,-1)
        if (direction == 'd' and self.direction != (0,-1)):
            self.direction = (0,1)
        if (direction == 'r' and self.direction != (-1,0)):
            self.direction = (1,0)
        if (direction == 'l' and self.direction != (1,0)):
            self.direction = (-1,0)

    def nextPosition(self):
        return (
            self.body[0][0][0]+(self.direction[0]*self.speed),
            self.body[0][0][1]+(self.direction[1]*self.speed)
        )

    def checkNextPosition(self, max_x, max_y) -> bool:
        pos = self.nextPosition()
        return (
            pos[0] >= 0
            and pos[1] >= 0
            and pos[0] < max_x
            and pos[1] < max_y
            and not(pos in self.body[1])
        )

    def move(self, food_position):
        new_pos = self.nextPosition()
        if (new_pos != food_position):
            pos = self.body[0].pop()
            self.body[1].remove(pos)
        else:
            pos = False
        self.body[0].appendleft(new_pos)
        self.body[1].add(new_pos)
        return (pos, self.body[0][0])
