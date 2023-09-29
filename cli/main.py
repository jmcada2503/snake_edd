from collections import deque
import time
from getkey import getkey, keys
from threading import Thread
import random

from snake import Snake
from screen import Screen
from food import Food

SLEEP_TIME = 0.15

screen = Screen()
snake = Snake((screen.width//2, screen.height//2))
food = Food(((screen.width//2)+3, (screen.height//2)+3))
moves = deque()

screen.table[food.position[1]][food.position[0]] = food.char
for i in snake.body[0]:
    screen.table[i[1]][i[0]] = snake.char

def playerInput():
    while input_thread_active:
        key = getkey()
        if key == keys.UP or key == 'w':
            moves.append('u')
        if key == keys.DOWN or key == 's':
            moves.append('d')
        if key == keys.RIGHT or key == 'd':
            moves.append('r')
        if key == keys.LEFT or key == 'a':
            moves.append('l')

input_thread_active = True
input_thread = Thread(target=playerInput)
input_thread.start()

points = 0
initial_time = time.time()

screen.printFrame(points, initial_time)
time.sleep(SLEEP_TIME)

mov_counter = 0
random_food_time = -1

try:
    while True:
        if (moves):
            snake.setDirection(moves.popleft())

        if (snake.checkNextPosition(screen.width, screen.height)):
            update = snake.move(food.position)
            if (update[0]):
                screen.table[update[0][1]][update[0][0]] = screen.char
            else:
                random_food_time = random.randint(0,9)
                mov_counter = 0
                points += 1
            screen.table[update[1][1]][update[1][0]] = snake.char
        else:
            break;

        if (mov_counter == random_food_time):
            food.move(screen.width, screen.height, snake)
            screen.table[food.position[1]][food.position[0]] = food.char

        screen.printFrame(points, initial_time)
        time.sleep(SLEEP_TIME)

        mov_counter += 1

    screen.clear()
    screen.message("PERDISTE EL JUEGO")
    screen.printFrame(points, initial_time)
    input_thread_active = False
    input_thread.join()
    exit()
except Exception as e:
    print("error:", e)
    input_thread.join()
